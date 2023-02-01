from Math.objs import Mat
from Net.net import Net
import csv
# Construct and return an neural network based on provided configuratio nfile
def createNetFromFile(path):
      
       
      folder_name = path.split("/")
      path = folder_name[-2] + "/" + folder_name[-1]
      print(path)
      training_input =  path + "/inputs.csv"
      conf = path + "/" + "net.conf"
      
      train_file  = open(training_input, "r")
      all_input = train_file.readlines()
      master_input = []
      for i in range (1,len(all_input)):
          cur_line = all_input[i]
          cur_input = cur_line.split(',')
          temp_input = []
          for j in cur_input:
            temp_input.append(float(j))  
          master_input.append(temp_input)  
          
          
      training_output =  path + "/outputs.csv"
      output_file  = open(training_output, "r")
      all_output = output_file.readlines()
      master_output = []
      for i in range (1,len(all_output)):
          cur_line = all_output[i]
          cur_output = cur_line.split(',')
          temp_output= []
          for j in cur_output:
            
            temp_output.append(float(j))
            
          master_output.append(temp_output)  
         
      
      file = open(conf, "r")
      all_lines = file.readlines()
      layers = []
      actv_func = []
      error_func = ""
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
                  
            # Search file for error function statement
            elif line.find("ErrorFunc=") != -1:
                  error_func  = line[10:len(line)-1]
                  
             # Search file for bias config statement
            elif line.find("LayerBias=") != -1:
                  l = line.partition('[')[2][:-3]
                  vals2 = l.split(',')
                  for j in vals2:
                        bias.append(float(j))                      
                 
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
                                    weights = []
                                    for k in weight_line:
                                          weights.append(float(k))
                                    weights_matrix.append(weights)
                              if line.find(":") != -1 and len(weights_matrix) != 0:
                                    weights_all.append(weights_matrix)
                                    weights_matrix = []
      
     # print(master_input)
      #print(master_output)
      net = Net(layers,actv_func,error_func, bias,master_input, master_output)
      for i in range(1,len(net.layers)):
            net.set_weights(i,weights_all[i-1])
            
      return net