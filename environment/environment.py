class Environment:
    def __init__(self, width = 800, height = 600):
        self.window_width = width
        self.window_height = height
        
        self.position = (width / 2, height / 2)
        self.speed = (0, 0)
    
    
    def reset(self):
        self.position = (self.window_width / 2, self.window_height / 2)
        self.speed = (0, 0)
        
        return (self.position, self.speed)


    def step(self, action):
        pass
