import random

import mesa

from src.agents.traffic_cell import TrafficCell
from src.agents.traffic_light import TrafficLightAgent
from src.agents.car import CarAgent


class PedestrianAgent(mesa.Agent):
    def __init__(self, model, direction, distraction:float):
        super().__init__(model)
        self.direction = direction
        self.distraction = distraction
        self.path = []

    def get_next_cell(self) -> tuple[int, int]:
        size = self.model.grid.width
        if self.direction == "n":
            return self.pos[0], (self.pos[1] + 1) % size

        if self.direction == "s":
            return self.pos[0], (self.pos[1] - 1) % size

        if self.direction == "w":
            return (self.pos[0] - 1) % size, self.pos[1]

        if self.direction == "e":
            return (self.pos[0] + 1) % size, self.pos[1]

    def get_left_diagonal_cell(self):
        next_cell = self.get_next_cell()
        if self.direction == "n":
            return next_cell[0]-1, next_cell[1]
        if self.direction == "s":
            return next_cell[0]+1, next_cell[1]
        if self.direction == "w":
            return next_cell[0], next_cell[1]-1
        if self.direction == "e":
            return next_cell[0], next_cell[1]+1

    def get_right_diagonal_cell(self):
        next_cell = self.get_next_cell()
        if self.direction == "n":
            return next_cell[0]+1, next_cell[1]
        if self.direction == "s":
            return next_cell[0]-1, next_cell[1]
        if self.direction == "w":
            return next_cell[0], next_cell[1]+1
        if self.direction == "e":
            return next_cell[0], next_cell[1]-1

    @staticmethod
    def is_traffic_light_red(agents_in_cell: list[mesa.Agent]) -> bool:
        for agent in agents_in_cell:
            if isinstance(agent, TrafficLightAgent) and agent.state == "red":
                return True

        return False

    @staticmethod
    def is_car_close(agents_in_cell: list[mesa.Agent]):
        for agent in agents_in_cell:
            if isinstance(agent, CarAgent):
                return True

        return False

    @staticmethod
    def is_building(agents_in_cell: list[mesa.Agent]):
        for agent in agents_in_cell:
            if isinstance(agent, TrafficCell) and agent.cell_type == "building":
                return True

        return False

    def step(self):
        if not self.pos:
            return

        print("Executing pedestrian step")
        agents_on_next_cell = self.model.grid.get_cell_list_contents([self.get_next_cell()])
        agents_on_left_diagonal_cell = self.model.grid.get_cell_list_contents([self.get_left_diagonal_cell()])
        agents_on_right_diagonal_cell = self.model.grid.get_cell_list_contents([self.get_right_diagonal_cell()])

        should_walk = (
            self.is_building(agents_on_next_cell)
            or
            (not self.is_traffic_light_red(agents_on_next_cell)
            and not self.is_car_close(agents_on_left_diagonal_cell)
            and not self.is_car_close(agents_on_right_diagonal_cell)
            and not self.is_car_close(agents_on_next_cell))
        )

        distracted_walking = random.uniform(0, 1)

        if should_walk or distracted_walking < self.distraction:
            print(f"Pedestrian will move to {self.get_next_cell()}")
            self.model.grid.move_agent(self, self.get_next_cell())