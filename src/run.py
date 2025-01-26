from models import TrafficModel

starter_model = TrafficModel(4, 11, 11)
for i in range(15):
    starter_model.step()