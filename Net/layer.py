import numpy as np


class Layer:
    # Initialize Layer Object
    def __init__(self, pos, num_nodes, bias, actv_func):
        
        # Number of nodes in this layer
        self.num_nodes = num_nodes
        # Layers number in network
        self.pos = pos
        
        # Input and Output Arrays
        self.input = np.zeros(self.num_nodes)
        self.output = np.zeros(self.num_nodes)
        
        # Array of Bias values per node
        self.bias = np.full(self.num_nodes, bias)
        
        # Activation Function of this layer
        self.actv_func = actv_func
        
        # Derivative of Error with respect to the output
        self.de_o = np.zeros(self.num_nodes)
        #Derivative of output with respect to the input
        self.do_i = np.zeros(self.num_nodes)
        #Derivative of input with respect to the weights
        self.di_w = np.zeros(self.num_nodes)
        
        
    
    def print(self):
        print("-------------")
        print("Layer: ", self.pos)
        print("Input: ", self.input)
        print("Output: ", self.output)
        print("Bias: ", self.bias)
        print("Activation Function: ", self.actv_func)
        print("Layer Derivatives:")
        print("\tDE_O: ",self.de_o)
        print("\tDO_I: ",self.do_i)
        print("\tDI_W: ",self.di_w)
        print("-------------")
        
        
        
        
        
      