import random
import mesa

from src.agents.traffic_light import TrafficLightAgent
from src.agents.traffic_cell import TrafficCell


class CarAgent(mesa.Agent):
    def __init__(self, model, direction):
        super().__init__(model)
        self.direction = direction
        self.path = []
        self.collision = False
        self.timer = 0

    def go_straight(self):
        print(f"Car {self.unique_id} with direction {self.direction} is going straight at {self.pos}")
        size = self.model.grid.width

        if self.direction == "n":
            return self.pos[0], (self.pos[1] + 1) % size

        if self.direction == "s":
            return self.pos[0], (self.pos[1] - 1) % size

        if self.direction == "w":
            return (self.pos[0] - 1) % size, self.pos[1]

        if self.direction == "e":
            return (self.pos[0] + 1) % size, self.pos[1]

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

            from src.agents.pedestrian import PedestrianAgent # This import is to avoid circular dependency

            if isinstance(agent, PedestrianAgent):
                self.model.car_and_pedestrian_collision += 1
                self.collision = True
                agent.remove()
                self.model.grid.remove_agent(agent)
                self.model.pedestrians -= 1
        
        if self.collision:
            if self.timer < 30:
                self.timer += 1
                return
            self.remove()
            self.model.grid.remove_agent(self)
            self.model.cars -= 1
            return

        self.model.grid.move_agent(self, self.go_straight())