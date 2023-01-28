from Net.layer import Layer
from Math.objs import Mat

class Net:
    def __init__(self, layer_format,actv_format, bias):
        self.layer_format = layer_format
        self.actv_format = actv_format
        self.bias = bias
        self.layers = []
        
        #Loop Through each Layer
        for i in range(0,len(layer_format)):
            temp_layer = Layer(i,self.layer_format[i],self.actv_format[i])
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
        

    def forward_prop(self):
        for i in range(1,len(self.layers)):
            cur_layer = self.layers[i]
            prev_layer = self.layers[i-1]

            prev_output = prev_layer.output
            cur_weights = cur_layer.weights

            cur_layer.input = (cur_weights*prev_output)
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
        
        