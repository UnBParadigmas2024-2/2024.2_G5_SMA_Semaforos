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
    def __init__(self, model, state="red", group="vertical"):
        super().__init__(model)
        self.state = state
        self.timer = 0
        self.group = group

    def step(self):
        if self.group == "vertical":
            if self.model.vertical_state == "green":
                self.state = "green"
            elif self.model.vertical_state == "yellow":
                self.state = "yellow"
            else:
                self.state = "red"
        elif self.group == "horizontal":
            if self.model.horizontal_state == "green":
                self.state = "green"
            elif self.model.horizontal_state == "yellow":
                self.state = "yellow"
            else:
                self.state = "red"

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

        self.schedule = mesa.time.RandomActivation(self)

        self.vertical_state = "green"
        self.horizontal_state = "red"
        self.timer = 0

        self.traffic_lights = []
        for i in range(4):
            group = "vertical" if i < 2 else "horizontal"
            agent = TrafficLightAgent(model=self, state="red", group=group)
            self.traffic_lights.append(agent)

        def isStreet(width, height, x, y):
            return x != round(width/2 - 2) and x != round(width/2) and y != round(height/2 - 2) and y != round(height/2)

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

        self.grid.place_agent(self.traffic_lights[0], (round(width/2) - 3, round(height/2) - 2))
        self.grid.place_agent(self.traffic_lights[1], (round(width/2) - 2, round(height/2) + 1))
        self.grid.place_agent(self.traffic_lights[2], (round(width / 2) + 1, round(height / 2)))
        self.grid.place_agent(self.traffic_lights[3], (round(width / 2), round(height / 2) - 3))

        car = CarAgent(self, direction="n")
        self.grid.place_agent(car, (round(width/2), 0))

        for agent in self.traffic_lights + [car]:
            self.schedule.add(agent)

    def step(self):
        self.timer += 1
        if self.timer > 10:
            if self.vertical_state == "green":
                self.vertical_state = "yellow"
            elif self.vertical_state == "yellow":
                self.vertical_state = "red"
                self.horizontal_state = "green"
            elif self.horizontal_state == "green":
                self.horizontal_state = "yellow"
            elif self.horizontal_state == "yellow":
                self.horizontal_state = "red"
                self.vertical_state = "green"
            self.timer = 0

        for agent in self.traffic_lights:
            agent.step()

        self.schedule.step()