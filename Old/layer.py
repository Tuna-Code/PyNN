from Math.objs import Mat
import math

class Layer:
    # Initialize Layer Object
    def __init__(self, num, num_nodes, actv_func, b):
        prefill = ("zeroes",0,0,-1)
        self.input = Mat(num_nodes, 1, prefill)
        self.output = Mat(num_nodes, 1, prefill)
        self.bias= Mat(num_nodes, 1, prefill)
        self.actv_func = actv_func
        self.weights = [[0]]
        self.weight_adjs = [[0]]
        self.num = num
        self.num_nodes = num_nodes
        #Derivative of Error with respect to the output
        self.de_o = Mat(num_nodes, 1, prefill)
        #Derivative of output with respect to the input
        self.do_i = Mat(num_nodes, 1, prefill)
        #Derivative of input with respect to the weights
        self.di_w = None
        for i in range(0,num_nodes):
            self.bias.mat[i][0] = b
    
    def sigmoid(self, x):
        return 1/(1 + math.exp(-x))
    
    def relu(self, x):
        return max(0.0, x)
    
        
        
        
    def activate_layer(self):
        e_sum = 0
            #print(layer.input.mat[i][0])
            
            #print(val)
        if(self.actv_func == "Sigmoid"):
            for i in range(0,self.num_nodes):
                self.output.mat[i][0] = self.sigmoid(self.input.mat[i][0])
        elif(self.actv_func == "Relu"):
            for i in range(0,self.num_nodes):
                self.output.mat[i][0] = self.relu(self.input.mat[i][0])
        
        elif(self.actv_func == "Softmax"):
           
            for i in range(0,self.num_nodes):
               
                e_sum += math.exp(self.input.mat[i][0])
            for i in range(0,self.num_nodes):
                self.output.mat[i][0] = math.exp(self.input.mat[i][0]) / e_sum
                
        elif(self.actv_func == "None"):
            for i in range(0,self.num_nodes):
                self.output.mat[i][0] = self.input.mat[i][0]
      

    def __str__(self):
        text = "-------L" + str(self.num) + "-------\n"
        text += "Node Count: " + str(self.num_nodes) + " Actv Func: " + self.actv_func
        text += "\nInput:" + self.input.__str__()
        text += "\nOutput:" + self.output.__str__()
        if(self.num != 0):
            text += "\nWeights:" + self.weights.__str__()
        text += "----------------\n"
        return text