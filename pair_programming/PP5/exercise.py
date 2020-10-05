import numpy as np

# Define layer function
class Layer:
    def __init__(self, shape, actv):
        self.shape = shape
        self.actv = actv
        # Initialize weights and bias with random values
        np.random.seed(42) # Set seed
        self.weights = np.random.rand(shape[0], shape[1])
        self.bias = np.random.rand(1,shape[1])
        
    def forward(self, inputs):
        if inputs.shape != (1, self.shape[0]):
            raise Exception("Your inputs should be %s, but got %s"%((1, self.shape[0]), inputs.shape))
        return self.actv(np.dot(inputs, self.weights) + self.bias)
    
    def __str__(self):
        return "The shape of your layer is %s, and the activation function is %s. "%(self.shape, self.actv)

    def __repr__(self):
        return f'Layer of shape ({self.shape[0]},{self.shape[1]}), using activation function {repr(self.actv)}'

    def __eq__(self, other):
        # Compare shape and activation function
        return self.shape == other.shape and self.actv == other.actv

t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network

layer1 = Layer((100, 4), np.tanh) # Define layer 1
layer2 = Layer((4, 4), np.tanh) # Define layer 2

# Run through the network
h1 = layer1.forward(t) # First layer
h2 = layer2.forward(h1) # Last layer

print("Layer2 Output:", h2)
print(layer1)
print(layer1 == layer1)
layer2

# Coder: Krithika Sundararajan, Yang Xiang, Xiaohan Yang
# Sharer: Krithika Sundararajan
# Listener: Max Li