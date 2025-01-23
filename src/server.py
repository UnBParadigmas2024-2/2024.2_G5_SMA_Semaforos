import mesa
from mesa.visualization import SolaraViz, make_plot_component, make_space_component
from models import TrafficModel, TrafficLightAgent

def agent_portrayal(agent):
    color = "tab:red" if agent.state == "red" else "tab:green"
    return {"color": color, "size": 50}

model_params = {
    "n": 10,
    "width": 10,
    "height": 10,
}

tr_model = TrafficModel(n=10, width=10, height=10)

SpaceGraph = make_space_component(agent_portrayal)

page = SolaraViz(
    tr_model,
    components=[SpaceGraph],
    model_params=model_params,
    name="Model",
)