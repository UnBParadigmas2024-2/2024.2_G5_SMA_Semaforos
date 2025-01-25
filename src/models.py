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
        if self.state == "red" and self.timer > 10:
            self.state = "green"
            self.timer = 0
        elif self.state == "green" and self.timer > 10:
            self.state = "yellow"
            self.timer = 0
        elif self.state == "yellow" and self.timer > 5:
            self.state = "red"
            self.timer = 0

    def create_agents(model, n):
        agents = []
        for i in range(n):
            agent = TrafficLightAgent(model=model, state="red")
            agents.append(agent)
        return agents

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
    def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.datacollector = mesa.DataCollector(
            model_reporters={"Lights": "n"}, agent_reporters={"State": "state"}
        )

        for x in range(self.grid.width):
            for y in range(self.grid.height): # buildings
                if (x<=3 and y<=3 or 
                    y==5 and x<=3 or
                    y>=7 and x<=3 or
                    y==5 and x>=7 or
                    y>=7 and x>=7 or
                    y<=3 and x>=7 or
                    x==5 and y<=3 or
                    x==5 and y>=7 or
                    x==5 and y==5):
                    cell = TrafficCell(model=self, cell_type="building")
                    self.grid.place_agent(cell, (x, y))
                    
                # Intersections
                if (x==6 and y==4):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="n")
                    self.grid.place_agent(cell, (x, y))
                if (x==4 and y==4):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="e")
                    self.grid.place_agent(cell, (x, y))
                if (x==6 and y==6):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="w")
                    self.grid.place_agent(cell, (x, y))
                if (x==4 and y==6):
                    cell = TrafficCell(model=self, cell_type="intersection", allowed_turn="s")
                    self.grid.place_agent(cell, (x, y))
        
        car = CarAgent(self, direction="n")
        self.grid.place_agent(car, (6,0))

        agents = TrafficLightAgent.create_agents(model=self, n=n)
        self.grid.place_agent(agents[0], (3, 4))
        self.grid.place_agent(agents[1], (4, 7))
        self.grid.place_agent(agents[2], (6, 3))
        self.grid.place_agent(agents[3], (7, 6))

    
    def step(self):
        self.datacollector.collect(self)
        self.agents.do("step")