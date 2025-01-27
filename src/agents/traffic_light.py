import mesa

class TrafficLightAgent(mesa.Agent):
    def __init__(self, model, state, green_timer, red_timer, yellow_timer):
        super().__init__(model)
        self.state = state
        self.yellow_timer = yellow_timer
        self.green_timer = green_timer
        self.red_timer = red_timer
        self.timer = 0

    def step(self):
        self.timer += 1
        if self.state == "red" and self.timer > self.red_timer:
            self.state = "green"
            self.timer = 0
        elif self.state == "green" and self.timer > self.green_timer:
            self.state = "yellow"
            self.timer = 0
        elif self.state == "yellow" and self.timer > self.yellow_timer:
            self.state = "red"
            self.timer = 0