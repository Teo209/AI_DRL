from random import sample


class ReplayBuffer:
    def __init__(self, buffer_capacity: int):
        if type(buffer_capacity) is not int:
            raise TypeError(f"Buffer capacity must be int, not {type(buffer_capacity)}.")
        
        if buffer_capacity < 1:
            raise ValueError("Buffer capacity must be greater than 0.")
        
        self.position = 0
        self.size = 0
        self.buffer_capacity = buffer_capacity
        
        # state action reward next_state done
        self.buffer = [None] * self.buffer_capacity


    def add(self, state: tuple, action: tuple, reward: float, next_state: tuple, done: bool):
        experience = (state, action, reward, next_state, done)
        
        self.buffer[self.position % self.buffer_capacity] = experience
        self.position += 1
        self.size += 1 if self.size < self.buffer_capacity else 0


    def sample(self, batch_size: int):
        if self.size < 1:
            raise ValueError("Replay buffer is empty!")
        
        if type(batch_size) is not int:
            raise TypeError(f"Batch size must be int, not {type(batch_size)}.")
        
        if batch_size <= 0:
            raise ValueError("Batch size must be positive.")
        
        if batch_size > self.size:
            raise ValueError("Batch size too large.")
        
        experiences = sample(self.buffer[0:self.size], batch_size)
        
        return experiences

