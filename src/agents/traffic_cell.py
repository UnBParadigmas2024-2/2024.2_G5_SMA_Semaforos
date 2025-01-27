import mesa

class TrafficCell(mesa.Agent):
    def __init__(self, model, cell_type, allowed_turn=None):
        super().__init__(model)
        self.cell_type = cell_type
        self.allowed_turn = allowed_turn

    def step(self):
        pass