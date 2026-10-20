import unittest

from environment.environment import Environment


class TestEnvironment(unittest.TestCase):
    def test_initial(self):
        env = Environment()

        self.assertEqual(env.window_width, 800)
        self.assertEqual(env.window_height, 600)
        self.assertEqual(env.position, (400, 300))
        self.assertEqual(env.speed, (0, 0))

    def test_reset_observation(self):
        env = Environment(target=(100, 200))

        observation = env.reset()

        self.assertEqual(observation, ((400, 300), (0, 0), (100, 200)))
        

    def test_reset_restores_state(self):
        env = Environment(1200, 500, target=(100, 200))
        env.position = (129, 421)
        env.speed = (3, -2)
        env.steps = 90

        observation = env.reset()

        self.assertEqual(env.position, (600, 250))
        self.assertEqual(env.speed, (0, 0))
        self.assertEqual(observation, ((600, 250), (0, 0), (100, 200)))
        self.assertEqual(env.steps, 0)

    
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


    def test_step_reward(self):
        env = Environment(target=(100, 100), target_radius=10)
        env.position = (500, 200)
        step = env.step((0, 0))
        
        self.assertEqual(step[1], -1)
        self.assertFalse(step[2])
        self.assertFalse(step[3])
        
        
    def test_step_terminated(self):
        env = Environment(target=(400, 300))
        env.position = (400, 300)
        step = env.step((0, 0))
        
        self.assertEqual(step[1], 100)
        self.assertTrue(step[2])
        self.assertFalse(step[3])
        
    
    def test_target_out_of_bounds(self):
        env = Environment(target=(900, -20))
        self.assertEqual(env.target_position, (799, 1))

        env = Environment(target=(100, 200))
        self.assertEqual(env.target_position, (100, 200))

        env = Environment(target=(0, 600))
        self.assertEqual(env.target_position, (1, 599))
        
        env = Environment(target=(100, 700))
        self.assertEqual(env.target_position, (100, 599))
    
    
    def test_speed_limit_positive(self):
        env = Environment()
        env.speed = (4, 0)

        env.step((3, 0))

        self.assertEqual(env.speed, (5, 0))


    def test_speed_limit_negative(self):
        env = Environment()
        env.speed = (-4, 0)

        env.step((-3, 0))

        self.assertEqual(env.speed, (-5, 0))


    def test_speed_limit_both_axes(self):
        env = Environment()
        env.speed = (4, -4)

        env.step((3, -3))

        self.assertEqual(env.speed, (5, -5))


    def test_speed_limit_does_not_stop_movement(self):
        env = Environment()
        env.position = (400, 300)
        env.speed = (5, 0)

        env.step((2, 0))

        self.assertEqual(env.speed, (5, 0))
        self.assertEqual(env.position, (405, 300))


    def test_speed_can_decrease_from_limit(self):
        env = Environment()
        env.speed = (5, 0)

        env.step((-3, 0))

        self.assertEqual(env.speed, (2, 0))


    def test_truncated(self):
        env = Environment(max_steps=2)
        
        obs = env.step((0, 0))
        self.assertEqual(obs[3], False)
        
        obs = env.step((0, 0))
        self.assertEqual(obs[3], True)
        
    
    def test_terminated_truncated(self):
        env = Environment(target=(105, 100), target_radius=2, max_steps=2)
        env.position = (100, 100)
        
        obs = env.step((2, 0))
        self.assertEqual(obs[2], False)
        self.assertEqual(obs[3], False)
        
        obs = env.step((0, 0))
        self.assertEqual(obs[2], True)
        self.assertEqual(obs[3], False)
        
    
    def test_target_must_be_tuple_or_list(self):
        with self.assertRaises(TypeError):
            Environment(target=None)


    def test_target_coordinates_must_be_numeric(self):
        with self.assertRaises(TypeError):
            Environment(target=("abc", 200))


    def test_max_steps_must_be_integer(self):
        with self.assertRaises(TypeError):
            Environment(max_steps=2.5)
            
    
    def test_action_values_must_be_numeric(self):
        env = Environment()

        with self.assertRaises(TypeError):
            env.step(("abc", 0))

        