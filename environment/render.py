import pygame

from environment.environment import Environment


class Renderer:
    def __init__(self, env: Environment):
        pygame.init()
    
        self.env = env
        
        self.display = pygame.display.set_mode((env.window_width, env.window_height))
        pygame.display.set_caption("AI DRL SAC")
        self.clock = pygame.time.Clock()

        self.running = True


    def render(self):
        self.display.fill((51, 255, 255))
    
        pygame.draw.circle(self.display, (130, 130, 130), self.env.target_position, self.env.target_radius)
        pygame.draw.circle(self.display, (0, 0, 0), self.env.target_position, 2)
        
        pygame.draw.rect(self.display, (130, 255, 130), pygame.Rect(self.env.position[0] - 10 , self.env.position[1] - 10, 20, 20))
        
        pygame.display.flip()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def close(self):
        pygame.quit()

