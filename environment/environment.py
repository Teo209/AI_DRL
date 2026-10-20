import math


class Environment:
    def __init__(self, width = 800, height = 600, target = (12.5, 500), target_radius = 5):
        self.window_width = width
        self.window_height = height
        
        self.position = (width / 2, height / 2)
        self.speed = (0, 0)
        
        self.target_position = target
        self.target_radius = target_radius
        
    
    def is_success(self):
        delta_x = self.position[0] - self.target_position[0]
        delta_y = self.position[1] - self.target_position[1]
        
        distance = math.hypot(delta_x, delta_y)
        
        return distance <= self.target_radius
    
    
    def reset(self):
        self.position = (self.window_width / 2, self.window_height / 2)
        self.speed = (0, 0)
        
        return (self.position, self.speed)


    def step(self, action):
        delta_t = 1
        
        vx = self.speed[0] + action[0] * delta_t
        vy = self.speed[1] + action[1] * delta_t
        
        x = self.position[0] + vx * delta_t
        y = self.position[1] + vy * delta_t
        
        if x <= 0 or x >= self.window_width:       
            x = max(0, min(x, self.window_width))
            vx = 0
        
        if y <= 0 or y >= self.window_height:
            y = max(0, min(y, self.window_height))
            vy = 0
        
        self.speed = (vx, vy)
        self.position = (x, y)
