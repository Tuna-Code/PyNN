from Math.objs import Mat
from Net.net import Net


def createNetFromFile(path):
      file = open(path, "r")
      all_lines = file.readlines()
      layers = []
      actv_func = []
      bias = [0]
      weights_all = []
      for i in range (0,len(all_lines)):
            line = all_lines[i]
            
            # Search file for layer config statement
            if line.find("Layers=") != -1:
                  l = line.partition('[')[2][:-2]
                  layers = [eval(i) for i in l.split(',')]
                  
                  
                        
            # Search file for activation functions config statement
            elif line.find("ActivationFunctions=") != -1:
                  l = line.partition('[')[2][:-2]
                  actv_func = l.split(',')
                  
                  #vals = [eval(i) for i in l.split(',')]
                  
             # Search file for bias config statement
            elif line.find("LayerBias=") != -1:
                  l = line.partition('[')[2][:-3]
                  vals2 = l.split(',')
                  for j in vals2:
                        bias.append(float(j))                      
                 # print(bias)
                  #vals = [eval(i) for i in l.split(',')]
                  
             # Search file for activation bias config statement
            elif line.find("Weights=") != -1:
                  # Check if weights will be hard set or randomized
                  if(line[8:11] == "Set"):
                        weight_count = len(layers)-2
                        
                        weights_matrix = []
                        for j in range(i, len(all_lines)):
                              line = all_lines[j]
                              
                              if line.find("[") != -1:
                                    l = line.partition('[')[2][:-3]
                                    weight_line = l.split(',')
                                    #print(weight_line)
                                    weights = []
                                    for k in weight_line:
                                          weights.append(float(k))
                                         # print(weight)
                                    weights_matrix.append(weights)
                                    #print(weights)
                                   #print(weights_matrix)
                              if line.find(":") != -1 and len(weights_matrix) != 0:
                                    #print(weights_matrix)
                                    weights_all.append(weights_matrix)
                                    weights_matrix = []
                        #weights_all = [weight_count]
                      #  print(weights_all)
                      #  print(weights)           
                       
                        
           # elif (line.find("[") != -1:):
            #      print(line)
      
      
      net = Net(layers,actv_func, bias)
      for i in range(1,len(net.layers)):
            net.set_weights(i,weights_all[i-1])
            
                            
                  

      return net



nn = createNetFromFile("Data/simple/simple.conf")




#nn.init(input, exp_out)
#layer_format = [2,3,1]
#actv_format = ["None","Sigmoid","Sigmoid"]


input = [.1,.2,.7]
exp_out = [1,0,0]
nn.init(input, exp_out)
#input = [1,1]
#exp_out = [0]
#bias = [0,0,0]
#nn = Net(layer_format,actv_format,bias)
#w1 = [[.8,.2],
#      [.4,0.9],
 #     [.3,.5]]   
#nn.set_weights(1,w1)
#w2 = [[.3,.5,0.9]]  
#nn.set_weights(2,w2)
nn.forward_prop(input, exp_out)


print(nn)