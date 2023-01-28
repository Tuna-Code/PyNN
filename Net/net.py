from Net.layer import Layer
from Math.objs import Mat
import math

class Net:
    def __init__(self, layer_format,actv_format,bias):
        self.layer_format = layer_format
        self.actv_format = actv_format
        self.layers = []
        self.bias = bias
        #Loop Through each Layer
        for i in range(0,len(layer_format)):
            temp_layer = Layer(i,self.layer_format[i],self.actv_format[i],self.bias[i])
            if(i > 0):
                temp_layer.weights = Mat(self.layer_format[i], self.layer_format[i-1], ("zeroes",0,0,-1))

            else:
                temp_layer.weights = Mat(1,1,("zeroes",0,0,-1))
            self.layers.append(temp_layer)
            
    def init(self, input, exp_out):
        l0 = self.layers[0]
        #print(l0)
        for i in range(0,l0.output.rows):
            l0.output.mat[i][0] = input[i]
           
        #print(l0.output)
       # self.layers[0] = l0
        
    def activate_layer(self, layer):
        e_sum = 0
        
        
            #print(layer.input.mat[i][0])
            
            #print(val)
        if(layer.actv_func == "Sigmoid"):
            for i in range(0,layer.num_nodes):
                layer.output.mat[i][0] = self.sigmoid(layer.input.mat[i][0])
        elif(layer.actv_func == "Relu"):
            for i in range(0,layer.num_nodes):
                layer.output.mat[i][0] = self.relu(layer.input.mat[i][0])
        
        elif(layer.actv_func == "Softmax"):
           
            for i in range(0,layer.num_nodes):
               
                e_sum += math.exp(layer.input.mat[i][0])
            for i in range(0,layer.num_nodes):
                layer.output.mat[i][0] = math.exp(layer.input.mat[i][0]) / e_sum
                
        elif(layer.actv_func == "None"):
            for i in range(0,layer.num_nodes):
                layer.output.mat[i][0] = layer.input.mat[i][0]

   
    def sigmoid(self, x):
        return 1/(1 + math.exp(-x))
    
    def relu(self, x):
        return max(0.0, x)

 


    def forward_prop(self, input, exp_out):
        #
        
        for i in range(0,len(self.layers)):
            if i == 0:
                l0 = self.layers[0]
        #print(l0)
                for i in range(0,l0.output.rows):
                    l0.input.mat[i][0] = input[i]
                    l0.output = l0.input
            else:
                
                cur_layer = self.layers[i]
                prev_layer = self.layers[i-1]

                prev_output = prev_layer.output
                cur_weights = cur_layer.weights

                cur_layer.input = (cur_weights*prev_output) + cur_layer.bias
                self.activate_layer(cur_layer)
                
            #cur_layer.output = cur_layer.input
           # self.layers[i] = cur_layer





    def set_weights(self, l, weights):
        layer = self.layers[l]
        for i in range(0,layer.weights.rows):
            for j in range(0,layer.weights.cols):
                layer.weights.mat[i][j] = weights[i][j]


    def __str__(self):
        text = ""
        for i in range(0, len(self.layers)):
            text += self.layers[i].__str__()

        return text
        
        