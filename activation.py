import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

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

def leaky_ReLU(x):
    return x if x>= 0 else 0.01*x

def leaky_ReLU_derivitave(x):
    return 1 if x>=0 else 0.01


def plot_function(function,lower=-10,upper=10,step=0.5):
    cur_x=[step*i for i in range(int(-10/step),int(10/step))]
    cur_y=[function(i) for i in cur_x]
    plt.plot(cur_x,cur_y)

if __name__ == "__main__":
    plot_function(sigmoid)
    plot_function(sigmoid_derivitive)
    plt.show()