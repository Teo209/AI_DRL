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
