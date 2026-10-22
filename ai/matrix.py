import numpy as np


def dense(x, weights, bias):
    return np.dot(weights, x) + bias


def relu(x):
    return np.maximum(0, x)


activation_types = {
    "relu": relu,
}


def forward(x, weights, bias, activation=None):
    z = dense(x, weights, bias)
    
    if activation is None:
        return z
    
    if activation in activation_types:
        return activation_types[activation](z)
    
    raise ValueError("Invalid activation type!")
    
