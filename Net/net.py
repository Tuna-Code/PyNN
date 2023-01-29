from Net.layer import Layer
from Math.objs import Mat
import math

class Net:
    #Initialize Net object
    def __init__(self, layer_format,actv_format,bias,training_inputs, training_outputs):
        self.layer_format = layer_format
        self.actv_format = actv_format
        self.layers = []
        self.bias = bias
        self.training_inputs = training_inputs
        self.training_outputs = training_outputs
        self.exp_out = Mat(3,1,("zeroes",0,0,-1))
        self.output = []
        
        
        #Loop Through each Layer
        for i in range(0,len(layer_format)):
            temp_layer = Layer(i,self.layer_format[i],self.actv_format[i],self.bias[i])
            if(i > 0):
                temp_layer.weights = Mat(self.layer_format[i], self.layer_format[i-1], ("zeroes",0,0,-1))

            else:
                temp_layer.weights = Mat(1,1,("zeroes",0,0,-1))
            self.layers.append(temp_layer)
    
    # Load inputs and expected outputs and propegte outward
    def forward_prop(self):
        #
        i = 0
        input = self.training_inputs[i]
        output = self.training_outputs[i]
        
        output_layer = self.layers[len(self.layers)-1]
        for i in range(0,output_layer.output.rows):
            self.exp_out.mat[i][0] = output[i]
            
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
                cur_layer.activate_layer()
        self.output = self.layers[len(self.layers)-1].output       
            #cur_layer.output = cur_layer.input
           # self.layers[i] = cur_layer
        
        print("\nFinal Output:\n" + self.output.__str__() + "\n\nExpected Output:" + self.exp_out.__str__())
  


    # If weights need to be manually set
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
        
        