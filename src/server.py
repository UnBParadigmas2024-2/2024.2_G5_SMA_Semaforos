import solara
import mesa
from mesa.visualization import SolaraViz, make_space_component
from models import *

car_count = solara.reactive(1)
traffic_light_time = solara.reactive(4)
map_size = solara.reactive(11)

def agent_portrayal(agent):
    if isinstance(agent, TrafficCell):
        if agent.cell_type == "building":
            return {"color": "tab:gray", "marker": "s", "zorder": 0}
        if agent.cell_type == "intersection":
            return {"color": "white", "marker": "s", "zorder": -1} 
    if isinstance(agent, TrafficLightAgent):
        if agent.state == "green":
            color = "green"
        elif agent.state == "yellow":
            color = "yellow"
        else:
            color = "red"
        return {"color": color, "size": 50, "zorder": 1}
    if isinstance(agent, CarAgent):
        return {"color": "tab:blue", "zorder": 0}

model_params = {
    "n": 4,
    "width": 40,
    "height": 40,
}

tr_model = TrafficModel(n=4, width=40, height=40)

SpaceGraph = make_space_component(agent_portrayal)

@solara.component
def ParameterInputs():
    solara.InputInt("Quantidade de carros", value=car_count)
    solara.InputInt("Tempo do semáforo (segundos)", value=traffic_light_time)
    solara.InputInt("Tamanho do mapa", value=map_size)
    solara.Markdown(f"**Parâmetros atuais:**\n\n- Quantidade de carros: {car_count.value}\n- Tempo do semáforo: {traffic_light_time.value} segundos\n- Tamanho do mapa: {map_size.value}x{map_size.value}")

@solara.component
def Page():
    with solara.Columns([1, 3]):
        with solara.Column():
            ParameterInputs()
        with solara.Column():
            SolaraViz(
                tr_model,
                components=[SpaceGraph],
                model_params=model_params,
                name="Model",
            )
