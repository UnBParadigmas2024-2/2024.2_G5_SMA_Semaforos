from mesa.visualization import SolaraViz, make_space_component
from models import *


def agent_portrayal(agent):
    if isinstance(agent, TrafficLightAgent): # Semaforos
        if agent.state == "red":
            color = "tab:red"
        elif agent.state == "green":
            color = "tab:green"
        elif agent.state == "yellow":
            color = "tab:orange"
        return {"color": color, "size":50, "zorder": 1}
    
    elif isinstance(agent, CarAgent): # Carros
        return {"color": "tab:blue", "marker": "h", "zorder": 0}
    
    elif isinstance(agent, TrafficCell): # Terreno
        if agent.cell_type == "building":
            return {"color": "tab:gray", "marker": "s", "zorder": 0}
        
        elif agent.cell_type == "intersection":
            return {"marker": "", "zorder": -1}


model_params = {
    "max_cars": {
        "type": "SliderInt",
        "value": 6,
        "label": "Quantidade de carros",
        "min": 4,
        "max": 40,
        "step": 1,
    },
    "size": {
        "type": "SliderInt",
        "value": 17,
        "label": "Tamanho do mapa",
        "min": 11,
        "max": 30,
        "step": 1,
    },
    "green_timer": {
        "type": "SliderInt",
        "value": 10,
        "label": "Tempo do semáforo verde",
        "min": 5,
        "max": 100,
        "step": 1,
    }, 
    "red_timer":{
        "type": "SliderInt",
        "value": 20,
        "label": "Tempo do semáforo vermelho",
        "min": 5,
        "max": 100,
        "step": 1,
    }, 
    "yellow_timer":{
        "type": "SliderInt",
        "value": 5,
        "label": "Tempo do semáforo amarelo",
        "min": 5,
        "max": 100,
        "step": 1,
    }
}

tr_model = TrafficModel()
spaceGraph = make_space_component(agent_portrayal)

page = SolaraViz(
    tr_model,
    components=[spaceGraph],
    model_params=model_params,
    name="Modelo de tráfego",
)