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
    def __init__(self, size=17, seed=None):
        super().__init__(seed=seed)
        width = size
        height = size
        self.grid = mesa.space.MultiGrid(width, height, True)
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
            for y in range(self.grid.height): # buildings
                # -- street in height
                if (isStreet(width, height, x, y)):
                    cell = TrafficCell(model=self, cell_type="building")
                    self.grid.place_agent(cell, (x, y))

                # --=-- Intersections --=--
                if (x == round(width/2) and y == round(height/2) - 2):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="n")
                    self.grid.place_agent(cell, (x, y))
                if (x == round(width/2) - 2 and y == round(height/2) - 2):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="e")
                    self.grid.place_agent(cell, (x, y))
                if (x == round(width/2) and y == round(height/2)):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="w")
                    self.grid.place_agent(cell, (x, y))
                if (x == round(width/2) - 2 and y == round(height/2)):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="s")
                    self.grid.place_agent(cell, (x, y))

                # --=-- Traffic Lights --=--
                if (x == round(width/2) - 3 and y == round(height/2) - 2):
                    self.grid.place_agent(agents[0], (x, y))

                if (x == round(width/2) - 2 and y == round(height/2) + 1):
                    self.grid.place_agent(agents[1], (x, y))

                if (x == round(width/2) + 1 and y == round(height/2)):
                    self.grid.place_agent(agents[2], (x, y))

                if (x == round(width/2) and y == round(height/2) - 3):
                    self.grid.place_agent(agents[3], (x, y))
                
        self.grid.place_agent(CarAgent(self, direction="n"), (round(width/2), 0))
        self.grid.place_agent(CarAgent(self, direction="s"), (round(width/2)-2, height-1))
        self.grid.place_agent(CarAgent(self, direction="e"), (0, round(width/2)-2))
        self.grid.place_agent(CarAgent(self, direction="w"), (height-1, round(width/2)))

    def step(self):
        self.datacollector.collect(self)
        self.agents.do("step")