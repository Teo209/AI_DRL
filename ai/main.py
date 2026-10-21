from environment.environment import Environment
from environment.render import Renderer

environment = Environment(800, 600, (70, 76), 20, 5, 1000)
renderer = Renderer(environment, (40, 40))

observation = environment.reset()

done = False
try:
    while renderer.running and not done:
        renderer.handle_events()
        
        dx, dy, vx, vy = observation
        
        ax = observation[0] / (abs(observation[0]) * 0.5 + 0.0001) / environment.max_speed
        ay = observation[1] / (abs(observation[1]) * 0.5 + 0.0001) / environment.max_speed
        
        action = [ax, ay]
        
        observation, reward, terminated, truncated = environment.step(action)
        print("\n" + str(environment.steps) + "   Observation    |   Reward  |   Terminated  |   Truncated")
        print(observation, reward, terminated, truncated)
        
        done = terminated or truncated
        
        renderer.render()
        renderer.clock.tick(60)

finally:
    renderer.close()
