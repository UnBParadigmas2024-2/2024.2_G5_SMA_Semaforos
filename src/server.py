import mesa
from mesa.visualization import SolaraViz, make_space_component
from models import *

def agent_portrayal(agent):
    if isinstance(agent, TrafficCell):
        if agent.cell_type == "building":
            return {"color": "tab:gray", "marker": "s", "zorder": 0}
        if agent.cell_type == "intersection":
            return {"color": "white", "marker": "s", "zorder": -1} 
    if isinstance(agent, TrafficLightAgent):
        color = "tab:red" if agent.state == "red" else "tab:green"
        return {"color": color, "size": 50, "zorder": 1}
    if isinstance(agent, CarAgent):
        return {"color": "tab:blue", "zorder": 0}

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