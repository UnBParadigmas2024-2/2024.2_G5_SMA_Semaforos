import mesa
from mesa.visualization import SolaraViz, make_space_component
from models import *

def agent_portrayal(agent):
    if isinstance(agent, TrafficLightAgent):
        if agent.state == "red":
            color = "red"
        elif agent.state == "green":
            color = "green"
        elif agent.state == "yellow":
            color = "yellow"
        return {"color": color, "shape": "circle", "r": 0.5}
    elif isinstance(agent, CarAgent):
        return {"color": "blue", "shape": "rect", "w": 0.5, "h": 0.5}
    elif isinstance(agent, TrafficCell):
        if agent.cell_type == "building":
            return {"color": "gray", "shape": "rect", "w": 1, "h": 1}
        elif agent.cell_type == "intersection":
            return {"color": "white", "shape": "rect", "w": 1, "h": 1}


model_params = {
    "n": 4,
    "width": 10,
    "height": 10,
}

tr_model = TrafficModel(n=4, width=11, height=11)

SpaceGraph = make_space_component(agent_portrayal)

page = SolaraViz(
    tr_model,
    components=[SpaceGraph],
    model_params=model_params,
    name="Model",
)