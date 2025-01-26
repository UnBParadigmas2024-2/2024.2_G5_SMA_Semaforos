import solara
import mesa
from mesa.visualization import SolaraViz, make_space_component
from models import *

car_count = solara.reactive(1)
traffic_light_time = solara.reactive(4)
map_size = solara.reactive(11)

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
