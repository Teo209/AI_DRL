from environment.environment import Environment
from environment.render import Renderer

environment = Environment(800, 600, (200, 350), 20, 5, 1000)
renderer = Renderer(environment, (40, 40))


while renderer.running:
    renderer.handle_events()
    
    renderer.render()

    renderer.clock.tick(60)
    

renderer.close()
