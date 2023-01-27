from Net.layer import Layer
from Math.objs import Mat

class Net:
    def __init__(self, layer_format,actv_format):
        self.layer_format = layer_format
        self.actv_format = actv_format

        self.layers = []
        
        #Loop Through each Layer
        for i in range(0,len(layer_format)):
            temp_layer = Layer(i,self.layer_format[i],self.actv_format[i])
            if(i > 0):
                temp_layer.weights = Mat(self.layer_format[i-1], self.layer_format[i], ("zeroes",0,0,-1))
            else:
                temp_layer.weights = Mat(1,1,("zeroes",0,0,-1))
            self.layers.append(temp_layer)
            
    def init(self, input, exp_out):
        l0 = self.layers[0]
        #print(l0)
        for i in range(0,l0.output.rows):
            l0.output.mat[i][0] = input[i]
        #print(l0.output)
        










    def set_weights(self, l, weights):
        layer = self.layers[l]
        for i in range(0,layer.weights.rows):
            for j in range(0,layer.weights.cols):
                layer.weights.mat[i][j] = weights[i][j]
        
        