from Math.objs import Mat
from Net.net import Net

 #3 entries = 3 layers
 #Each entry is node count of the layer

#layer_format = [3,2,2]
#actv_format = ["None","Sigmoid","Sigmoid"]

layer_format = [2,2,2]
actv_format = ["None","Sigmoid","Sigmoid"]



input = [0.5,0.3]
exp_out = [0.05, 0.95]
bias = [0.25,0.25]
nn = Net(layer_format,actv_format,bias)
nn.init(input, exp_out)


#w1= [[0.1,0.3,0.5],
#      [0.2,0.4,0.6]]

w1 = [[0.1,0.2],
      [0.13,0.4]]    
nn.set_weights(1,w1)

#w2 = [[0.7,0.8],
#      [0.9,0.1]]
w2 = [[0.5,0.7],
      [0.6,0.8]]

nn.set_weights(2,w2)



nn.init(input, exp_out)
nn.forward_prop()

print(nn)