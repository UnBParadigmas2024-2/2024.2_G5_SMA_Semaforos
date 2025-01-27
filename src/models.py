import mesa
import random

class TrafficCell(mesa.Agent):
    def __init__(self, model, cell_type, allowed_turn=None):
        super().__init__(model)
        self.cell_type = cell_type
        self.allowed_turn = allowed_turn
    
    def step(self):
        pass

class TrafficLightAgent(mesa.Agent):
    def __init__(self, model, state="red"):
        super().__init__(model)
        self.state = state
        self.timer = 0

    def step(self):
        self.timer += 1
        if self.state == "red" and self.timer > 23:
            self.state = "green"
            self.timer = 0
        elif self.state == "green" and self.timer > 10:
            self.state = "yellow"
            self.timer = 0
        elif self.state == "yellow" and self.timer > 10:
            self.state = "red"
            self.timer = 0


class CarAgent(mesa.Agent):
    def __init__(self, model, direction):
        super().__init__(model)
        self.direction = direction
        self.path = []

    def go_straight(self):
        print(f"Car {self.unique_id} with direction {self.direction} is going straight at {self.pos}")
        if self.direction == "n":
            return (self.pos[0], self.pos[1]+1)
        
        if self.direction == "s":
            return (self.pos[0], self.pos[1]-1)
        
        if self.direction == "w":
            return (self.pos[0]-1, self.pos[1])
        
        if self.direction == "e":
            return (self.pos[0]+1, self.pos[1])
    
    def turn(self):
        print(f"Car {self.unique_id} is turning at {self.pos}")
        if self.direction == "n":
            self.direction = "e"
        elif self.direction == "s":
            self.direction = "w"
        elif self.direction == "w":
            self.direction = "n"
        elif self.direction == "e":
            self.direction = "s"
    
    def step(self):
        current_cell_contents = self.model.grid.get_cell_list_contents([self.pos])
        for agent in current_cell_contents:
            if isinstance(agent, TrafficCell) and agent.cell_type == "intersection":
                if agent.allowed_turn == self.direction:
                    action = random.choice([self.turn, None])
                    if action:
                        action()
        self.model.grid.move_agent(self, self.go_straight())
        

class TrafficModel(mesa.Model):
    def __init__(self, max_cars=12, size=17):
        super().__init__()
        self.directions = ["n","s","e","w"]
        self.max_cars = max_cars
        self.size = size
        self.cars = 0

        self.grid = mesa.space.MultiGrid(size, size, True)
        self.datacollector = mesa.DataCollector(
            model_reporters={"Lights": "n"}, agent_reporters={"State": "state"}
        )

        def isStreet(width, height, x, y):
            return x != round(width/2 - 2) and x != round(width/2) and y != round(height/2 - 2) and y != round(height/2)

        agents = [TrafficLightAgent(model=self, state="green"), 
                  TrafficLightAgent(model=self, state="red"), 
                  TrafficLightAgent(model=self, state="green"), 
                  TrafficLightAgent(model=self, state="red")]
        
        for x in range(self.grid.width):
            for y in range(self.grid.height): 
                if (isStreet(size, size, x, y)): # buildings
                    cell = TrafficCell(model=self, cell_type="building")
                    self.grid.place_agent(cell, (x, y))

                # --=-- Intersections --=--
                if (x == round(size/2) and y == round(size/2) - 2):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="n")
                    self.grid.place_agent(cell, (x, y))

                if (x == round(size/2) - 2 and y == round(size/2) - 2):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="e")
                    self.grid.place_agent(cell, (x, y))

                if (x == round(size/2) and y == round(size/2)):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="w")
                    self.grid.place_agent(cell, (x, y))

                if (x == round(size/2) - 2 and y == round(size/2)):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="s")
                    self.grid.place_agent(cell, (x, y))

                # --=-- Traffic Lights --=--
                if (x == round(size/2) - 3 and y == round(size/2) - 2):
                    self.grid.place_agent(agents[0], (x, y))

                if (x == round(size/2) - 2 and y == round(size/2) + 1):
                    self.grid.place_agent(agents[1], (x, y))

                if (x == round(size/2) + 1 and y == round(size/2)):
                    self.grid.place_agent(agents[2], (x, y))

                if (x == round(size/2) and y == round(size/2) - 3):
                    self.grid.place_agent(agents[3], (x, y))
                
        self.grid.place_agent(CarAgent(self, direction="n"), self.starting_pos("n"))
        self.cars += 1
        self.grid.place_agent(CarAgent(self, direction="s"), self.starting_pos("s"))
        self.cars += 1
        self.grid.place_agent(CarAgent(self, direction="e"), self.starting_pos("e"))
        self.cars += 1
        self.grid.place_agent(CarAgent(self, direction="w"), self.starting_pos("w"))
        self.cars += 1

    def starting_pos(self, direction):
        if direction == "s":
            return (round(self.size/2)-2, self.size-1)
        if direction == "e":
            return (0, round(self.size/2)-2)
        if direction == "n":
            return (round(self.size/2), 0)
        if direction == "w":
            return (self.size-1, round(self.size/2))
        
    def spawn_car(self, direction:str):
        cell_contents = self.grid.get_cell_list_contents([self.starting_pos(direction)])
        if not cell_contents:
            self.grid.place_agent(CarAgent(self, direction=direction), self.starting_pos(direction))
            self.cars += 1

    def step(self):
        self.datacollector.collect(self)
        self.agents.do("step")

        if self.cars < self.max_cars:
            for direction in self.directions:
                self.spawn_car(direction)
        