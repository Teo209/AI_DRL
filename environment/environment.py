import math
import warnings


class Environment:
    def __init__(self, width: float = 800, height: float = 600, target: tuple[float, float] = (12.5, 500), target_radius: float = 10, max_speed: float = 5, max_steps: int = 1000):
        if width <= 3:
            raise ValueError("Window width must be bigger than 3!")
        
        if height <= 3:
            raise ValueError("Window height must be bigger than 3!")
        
        if type(target) not in [tuple, list]:
            raise TypeError(f"Invalid target. Expected tuple or list, got {type(target)}.")
        
        if len(target) != 2:
            raise ValueError(f"Invalid target. Expected 2 coordinates, got {len(target)}.")
        
        if type(target[0]) not in [int, float] or type(target[1]) not in [int, float]:
            raise TypeError(f"Target's values invalid. Expected float, got {type(target[0])} and {type(target[1])}.")
                
        target_x = max(1, min(target[0], width - 1))
        target_y = max(1, min(target[1], height - 1))
        
        if tuple(target) != (target_x, target_y):
            warnings.warn(f"Target out of bounds! Automaticaly moved to {target_x}, {target_y}.")
            
        if target_radius < 0:
            raise ValueError("Target radius must be non-negative!")
        
        if max_speed <= 0:
            raise ValueError("Max speed must be greater than 0!")
        
        if type(max_steps) is not int:
            raise TypeError(f"Max number of steps must be int, got {type(max_steps)}.")
        
        if max_steps < 1:
            raise ValueError("Max number of steps must be greater than 0!")
        
        self.window_width = width
        self.window_height = height
        
        self.position = (width / 2, height / 2)
        self.speed = (0, 0)
        
        self.target_position = (target_x, target_y)
        
        self.target_radius = target_radius
        
        self.max_speed = max_speed
        
        self.max_steps = max_steps
        self.steps = 0
        
    
    def is_success(self):
        delta_x = self.position[0] - self.target_position[0]
        delta_y = self.position[1] - self.target_position[1]
        
        distance = math.hypot(delta_x, delta_y)
        
        return distance <= self.target_radius
    
    
    def get_observation(self):
        return (
            (self.target_position[0] - self.position[0]) / self.window_width,
            (self.target_position[1] - self.position[1]) / self.window_height,
            self.speed[0] / self.max_speed,
            self.speed[1] / self.max_speed,
        )
    
    
    def reset(self):
        self.position = (self.window_width / 2, self.window_height / 2)
        self.speed = (0, 0)
        self.steps = 0
        
        return self.get_observation()


    def step(self, action: tuple[float, float]):
        if type(action) not in [tuple, list]:
            raise TypeError(f"Invalid action. Expected tuple or list, got {type(action)}.")

        if len(action) != 2:
            raise ValueError(f"Invalid action. Expected 2 values, got {len(action)}.")
        
        if type(action[0]) not in [int, float] or type(action[1]) not in [int, float]:
            raise TypeError(f"Action's values invalid. Expected float or int, got {type(action[0])} and {type(action[1])}.")
        
        
        delta_t = 1
        
        ax = max(-1, min(action[0], 1))
        ay = max(-1, min(action[1], 1))
        
        vx = self.speed[0] + ax * delta_t
        vy = self.speed[1] + ay * delta_t
        
        vx = max(-self.max_speed, min(vx, self.max_speed))
        vy = max(-self.max_speed, min(vy, self.max_speed))
        
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
        
        observation = self.get_observation()
        
        self.steps += 1
        
        reward = -1
        terminated = False
        truncated = False
        
        if self.is_success():
            reward = +100
            terminated = True
        elif self.steps >= self.max_steps:
            truncated = True
        
        return (observation, reward, terminated, truncated)
