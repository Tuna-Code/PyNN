from Net.net import Net
import net_helper
import os

from GUI.gui import GUI


os.system("clear")




#net_file = gui.file_select()

net_file = "/home/tuna/coding/PyNN/Data/mattmazur"

nn = net_helper.createNetFromFile(net_file)
#print(nn.exp_out)




nn.forward_prop()
nn.back_prop()
#gui = GUI(nn)
#gui.mainloop()


#print(nn.exp_out)
#print(nn)