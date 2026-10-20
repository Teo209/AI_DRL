import pygame

from environment.environment import Environment


class Renderer:
    def __init__(self, env: Environment, character_size: tuple[float, float] = (20, 20)):
        if type(character_size) not in [tuple, list]:
            raise TypeError(f"Invalid character size. Expected tuple or list, got {type(character_size)}.")
        
        if len(character_size) != 2:
            raise ValueError(f"Invalid character size. Expected 2 coordinates, got {len(character_size)}.")
                
        if type(character_size[0]) not in [int, float] or type(character_size[1]) not in [int, float]:
            raise TypeError(f"Character size's values invalid. Expected float, got {type(character_size[0])} and {type(character_size[1])}.")
        
        if character_size[0] < 1 or character_size[1] < 1:
            raise ValueError("Character size must be greater or equal than 1.")
        
        
        pygame.init()
    
        self.env = env
        self.character_size = character_size
        
        self.display = pygame.display.set_mode((env.window_width, env.window_height))
        pygame.display.set_caption("AI DRL SAC")
        self.clock = pygame.time.Clock()

        self.running = True


    def render(self):
        self.display.fill((255, 255, 217))
    
        pygame.draw.circle(self.display, (130, 130, 130), self.env.target_position, self.env.target_radius)
        pygame.draw.circle(self.display, (0, 0, 0), self.env.target_position, self.env.target_radius/5)
        
        pygame.draw.rect(self.display, (130, 255, 130), 
                         pygame.Rect(self.env.position[0] - self.character_size[0]/2 , 
                                     self.env.position[1] - self.character_size[1]/2, 
                                     *self.character_size))
        
        pygame.display.flip()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def close(self):
        pygame.quit()

