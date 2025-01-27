import mesa
import random

from src.agents.car import CarAgent
from src.agents.pedestrian import PedestrianAgent
from src.agents.traffic_cell import TrafficCell
from src.agents.traffic_light import TrafficLightAgent
        

class TrafficModel(mesa.Model):
    def __init__(self, max_cars=12, max_pedestrians=12, size=17, green_timer=10, red_timer=20, yellow_timer=5):
        self.directions = ["n","s","e","w"]
        self.max_cars = max_cars
        self.max_pedestrians = max_pedestrians
        self.size = size
        self.cars = 0
        self.pedestrians = 0
        self.car_and_pedestrian_collision = 0

        self.grid = mesa.space.MultiGrid(size, size, True)
        self.datacollector = mesa.DataCollector(
            model_reporters={"num_of_cars": "self.cars",
                             "num_of_pedestrians": "self.pedestrians",
                             "num_of_collisions": "self.car_and_pedestrian_collision"},
            agent_reporters={"State": "state"}
        )

        self.place_traffic_lights(green_timer, red_timer, yellow_timer)
        self.place_intersections()
        self.place_buildings()

        for direction in self.directions:
            self.spawn_car(direction)
            self.spawn_pedestrian(direction)

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
            return round(self.size / 2) - 2, self.size - 1
        if direction == "e":
            return 0, round(self.size / 2) - 2
        if direction == "n":
            return round(self.size / 2), 0
        if direction == "w":
            return self.size - 1, round(self.size / 2)

    def pedestrian_starting_pos(self, direction):
        if direction == "s":
            return random.choice([(round(self.size / 2) - 3, self.size - 1), (round(self.size / 2) + 1, self.size - 1)])
        if direction == "e":
            return random.choice([(0, round(self.size / 2) - 3), (0, round(self.size / 2) + 1)])
        if direction == "n":
            return random.choice([(round(self.size / 2) - 3, 0), (round(self.size / 2) + 1, 0)])
        if direction == "w":
            return random.choice([(self.size - 1, round(self.size / 2) - 3), (self.size - 1, round(self.size / 2) + 1)])
        
    def spawn_car(self, direction:str):
        cell_contents = self.grid.get_cell_list_contents([self.starting_pos(direction)])
        if not cell_contents:
            self.grid.place_agent(CarAgent(self, direction=direction), self.starting_pos(direction))
            self.cars += 1

    def spawn_pedestrian(self, direction: str):
        starting_pos = self.pedestrian_starting_pos(direction)

        print(f"Pedestrian being spawned at {starting_pos}")
        self.grid.place_agent(PedestrianAgent(self, direction=direction), starting_pos)
        self.pedestrians += 1

    def step(self):
        self.datacollector.collect(self)
        self.agents.do("step")

        if self.cars < self.max_cars:
            for direction in self.directions:
                self.spawn_car(direction)

        if self.pedestrians < self.max_pedestrians:
            print(f"Pedestrians count: {self.pedestrians}, max pedestrians {self.max_pedestrians}")
            for direction in self.directions:
                self.spawn_pedestrian(direction)
        