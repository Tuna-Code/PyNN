from Math.objs import Mat
from Net.net import Net

 #3 entries = 3 layers
 #Each entry is node count of the layer
layer_format = [3,2,2]
actv_format = ["None","Sigmoid","Sigmoid"]

nn = Net(layer_format,actv_format)

input = [1,4,5]
exp_out = [0.1, 0.05]
nn.init(input, exp_out)

w1 = [[0.1,0.2],
      [0.3,0.4],    
       [0.5,0.6] ]
nn.set_weights(1,w1)

w2 = [[0.7,0.8],
      [0.9,0.1]]
nn.set_weights(2,w2)

print(nn.layers[1].weights)


print(nn.layers[1].weights.mat[1])
