import numpy as np

def sigmoid(x):
    return (1/(1 + np.exp(-x)))

def sigmoid_derivitive(x):
    return sigmoid(x)*(1-sigmoid(x))

def tanh(x):
    return(2/(1 + np.exp(-2*x))) -1

def tanh_derivitive(x):
    return 1-(tanh(x)**2)

def ReLU(x):
    return x if x>=0 else 0

def ReLU_derivitave(x):
    return 1 if x>=0 else 0