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
    def __init__(self, model, state, green_timer, red_timer, yellow_timer):
        super().__init__(model)
        self.state = state
        self.yellow_timer = yellow_timer
        self.green_timer = green_timer
        self.red_timer = red_timer
        self.timer = 0

    def step(self):
        self.timer += 1
        if self.state == "red" and self.timer > self.red_timer:
            self.state = "green"
            self.timer = 0
        elif self.state == "green" and self.timer > self.green_timer:
            self.state = "yellow"
            self.timer = 0
        elif self.state == "yellow" and self.timer > self.yellow_timer:
            self.state = "red"
            self.timer = 0


class CarAgent(mesa.Agent):
    def __init__(self, model, direction):
        super().__init__(model)
        self.direction = direction
        self.path = []

    def go_straight(self):
        print(f"Car {self.unique_id} with direction {self.direction} is going straight at {self.pos}")
        size = self.model.grid.width

        if self.direction == "n":
            return (self.pos[0], (self.pos[1]+1) % size)
        
        if self.direction == "s":
            return (self.pos[0], (self.pos[1]-1) % size)
        
        if self.direction == "w":
            return ((self.pos[0]-1) % size, self.pos[1])
        
        if self.direction == "e":
            return ((self.pos[0]+1) % size, self.pos[1])
    
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
        next_position = self.go_straight()
        next_cell_contents = self.model.grid.get_cell_list_contents([next_position])

        for agent in next_cell_contents:
            if isinstance(agent, TrafficLightAgent):
                if agent.state == "red":
                    print(f"Car {self.unique_id} is waiting at {self.pos} for green light")
                    return
            
            if isinstance(agent, CarAgent):
                return
            
                
        for agent in current_cell_contents:
            if isinstance(agent, TrafficCell) and agent.cell_type == "intersection":
                if agent.allowed_turn == self.direction:
                    action = random.choice([self.turn, None])
                    if action:
                        action()
        self.model.grid.move_agent(self, self.go_straight())
        

class TrafficModel(mesa.Model):
    def __init__(self, max_cars=12, size=17, green_timer=10, red_timer=20, yellow_timer=5):
        super().__init__()
        self.directions = ["n","s","e","w"]
        self.max_cars = max_cars
        self.size = size
        self.cars = 0

        self.grid = mesa.space.MultiGrid(size, size, True)
        self.datacollector = mesa.DataCollector(
            model_reporters={"num_of_cars": "self.cars"}, agent_reporters={"State": "state"}
        )

        self.place_traffic_lights(green_timer, red_timer, yellow_timer)
        self.place_intersections()
        self.place_buildings()

        for direction in self.directions:
            self.spawn_car(direction)

    def place_traffic_lights(self, green_timer, red_timer, yellow_timer):
        # western traffic light
        x = round(self.size/2) - 3 
        y = round(self.size/2) - 2
        self.grid.place_agent(TrafficLightAgent(self, "green", green_timer, red_timer, yellow_timer), (x, y))

        # northern traffic light
        x = round(self.size/2) - 2
        y = round(self.size/2) + 1
        self.grid.place_agent(TrafficLightAgent(self, "red", green_timer, red_timer, yellow_timer), (x, y))

        # eastern traffic light
        x = round(self.size/2) + 1 
        y = round(self.size/2)
        self.grid.place_agent(TrafficLightAgent(self, "green", green_timer, red_timer, yellow_timer), (x, y))

        # southern traffic light
        x = round(self.size/2)
        y = round(self.size/2) - 3
        self.grid.place_agent(TrafficLightAgent(self, "red", green_timer, red_timer, yellow_timer), (x, y))
    
    def place_intersections(self):
        x = round(self.size/2)
        y = round(self.size/2)
        self.grid.place_agent(
            TrafficCell(model=self, cell_type="intersection", allowed_turn="w"), (x, y))
        
        x = round(self.size/2) - 2
        y = round(self.size/2)
        self.grid.place_agent(
            TrafficCell(model=self, cell_type="intersection", allowed_turn="s"), (x, y))
        
        x = round(self.size/2)
        y = round(self.size/2) - 2
        self.grid.place_agent(
            TrafficCell(model=self, cell_type="intersection", allowed_turn="n"), (x, y))

        x = round(self.size/2) - 2
        y = round(self.size/2) - 2
        self.grid.place_agent(
            TrafficCell(model=self, cell_type="intersection", allowed_turn="e"), (x, y))

    def place_buildings(self):
        def isBuilding(size, x, y):
            return (x != round(size/2 - 2) 
                and x != round(size/2) 
                and y != round(size/2 - 2)
                and y != round(size/2))
    
        for x in range(self.size):
            for y in range(self.size): 
                if (isBuilding(self.size, x, y)):
                    cell = TrafficCell(model=self, cell_type="building")
                    self.grid.place_agent(cell, (x, y))

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
        