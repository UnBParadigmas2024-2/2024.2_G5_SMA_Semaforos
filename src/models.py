import mesa
import numpy as np
import pandas as pd

class TrafficLightAgent(mesa.Agent):
    def __init__(self, model, state="red"):
        super().__init__(model)
        self.state = state
        self.timer = 0

    def switch_state(self):
        self.timer += 1
        print(f"Eu sou o agente: {str(self.unique_id)}, estou {self.state}, e meu timer é {self.timer}.")
        if self.timer > 10:
            self.state = "green" if self.state == "red" else "red"
            self.timer = 0

class TrafficModel(mesa.Model):
    def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.datacollector = mesa.DataCollector(
            model_reporters={"Lights": "n"}, agent_reporters={"State": "state"}
        )
        agents = TrafficLightAgent.create_agents(model=self, n=n)
        x = self.rng.integers(0, self.grid.width, size=(n,))
        y = self.rng.integers(0, self.grid.height, size=(n,))
        for a, i, j in zip(agents, x, y):
            # Add the agent to a random grid cell
            self.grid.place_agent(a, (i, j))
    
    def step(self):
        self.datacollector.collect(self)
        self.agents.do("switch_state")
