import unittest

from environment.environment import Environment


class TestEnvironment(unittest.TestCase):
    def test_initial(self):
        env = Environment()

        self.assertEqual(env.window_width, 800)
        self.assertEqual(env.window_height, 600)
        self.assertEqual(env.position, (400, 300))
        self.assertEqual(env.speed, (0, 0))

    def test_reset(self):
        env = Environment(1200, 500)
        env.position = (129, 921)
        env.speed = (1, 3)

        reset = env.reset()
        self.assertEqual(reset, ((600, 250), (0, 0)))
        
        self.assertEqual(env.position, (600, 250))
        self.assertEqual(env.speed, (0, 0))
        
    def test_step(self):
        env = Environment(800, 600)
        
        env.step((1, 0))
        
        self.assertEqual(env.speed, (1, 0))
        self.assertEqual(env.position, (401, 300))
        
        env.step((1, 0))
        self.assertEqual(env.speed, (2, 0))
        self.assertEqual(env.position, (403, 300))
        
        
    def test_move_from_edge(self):
        env = Environment(800, 600)
               
        env.position = (0, 300)
        env.speed = (0, 0)
        
        env.step((1, 0))
        
        self.assertEqual(env.position, (1, 300))
        self.assertEqual(env.speed, (1, 0))


    def test_edge_detection(self):
        env = Environment(800, 600)
        
        env.position = (799, 300)
        env.speed = (1, 0)

        env.step((1, 0))
        self.assertEqual(env.position, (800, 300))
        self.assertEqual(env.speed, (0, 0))
    
    
    def test_move_along_edge(self):
        env = Environment(800, 600)

        env.position = (800, 300)
        env.speed = (0, 0)

        env.step((0, 1))

        self.assertEqual(env.position, (800, 301))
        self.assertEqual(env.speed, (0, 1))
    
    
    def test_success(self):
        env = Environment(target=(100, 100), target_radius=10)
        
        env.position = (100, 100)
        self.assertTrue(env.is_success())
        
        env.position = (106, 108)
        self.assertTrue(env.is_success())
        
        env.position = (111, 100)
        self.assertFalse(env.is_success())

    
    def test_target_out_of_bounds(self):
        env = Environment(target=(900, -20))
        self.assertEqual(env.target_position, (799, 1))

        env = Environment(target=(100, 200))
        self.assertEqual(env.target_position, (100, 200))

        env = Environment(target=(0, 600))
        self.assertEqual(env.target_position, (1, 599))
        
        env = Environment(target=(100, 700))
        self.assertEqual(env.target_position, (100, 599))

