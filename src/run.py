from models import TrafficModel

starter_model = TrafficModel(4, 40, 40)
for i in range(15):
    starter_model.step()