from models import TrafficModel

starter_model = TrafficModel(4)
for i in range(15):
    starter_model.step()