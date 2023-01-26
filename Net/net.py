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
            self.layers.append(temp_layer)
           