import numpy as np


def dense(x, weights, bias):
    return np.dot(weights, x) + bias


def relu(x):
    return np.maximum(0, x)


def forward(x, weights, bias):
    z = dense(x, weights, bias)
    return relu(z)
