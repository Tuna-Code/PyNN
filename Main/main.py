from Math.objs import Mat
from Net.net import Net

 #3 entries = 3 layers
 #Each entry is node count of the layer
layer_format = [1,2,2]
actv_format = ["None","Sigmoid","Sigmoid"]

nn = Net(layer_format,actv_format)