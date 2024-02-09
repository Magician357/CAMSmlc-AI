import numpy as np
import random

class cnn:
    def __init__(self,layer_lengths,activation_function):
        self.weights=[
            np.random.randn(i) for i in layer_lengths # create lists of random numbers
        ]
        self.biases=[
            np.zeros(i) for i in layer_lengths # create lists of zeroes
        ]
        self.activation_function=activation_function

test=cnn([1,2,3])
print(test.weights)
print(test.biases)