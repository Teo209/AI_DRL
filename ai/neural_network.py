from math import sqrt

import numpy as np

from .matrix import forward


class NeuralNetwork:
    def __init__(self, neurons, input_size):
        if type(neurons) not in [list, tuple]:
            raise TypeError(f"Invalid neurons list. Expected tuple or list, got {type(neurons)}.")
        if len(neurons) <= 0:
            raise ValueError("There should be 1 or more layers of neurons!")
        for i in neurons:
            if type(i) is not int:
                raise TypeError("The number of neurons should be an integer!")
            if i <= 0:
                raise ValueError("There should be 1 or more neurons on every layer!")
        
        if type(input_size) is not int:
            raise TypeError("The number of inputs should be an integer!")
        if input_size <= 0:
            raise ValueError("There should be 1 or more inputs!")
        
        self.layers = len(neurons)
        self.neurons = neurons
        self.input_size = input_size
        
        self.weights = [np.random.randn(neurons[0], input_size) * sqrt(2/input_size)]
        self.biases = [np.zeros(neurons[0])]
        for layer in range(1, self.layers):
            input_vals = neurons[layer - 1]
            self.weights.append(np.random.randn(neurons[layer], input_vals) * sqrt(2/input_vals))
            self.biases.append(np.zeros(neurons[layer]))


    def predict(self, x, activation = None):
        if activation is None:
            activation = ["relu"] * (self.layers - 1)
            activation.append(None)
        
        if len(activation) != self.layers:
            raise ValueError("Activation count must match layer count!")
        
        for layer in range(self.layers):
            x = forward(x, self.weights[layer], self.biases[layer], activation[layer])
                
        return x
