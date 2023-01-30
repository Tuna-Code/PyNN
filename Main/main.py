from Net.net import Net
import net_helper
import os

from GUI.gui import GUI


os.system("clear")



#gui = GUI()
#gui.mainloop()
#net_file = gui.file_select()

net_file = "/home/tuna/coding/PyNN/Data/simple"
nn = net_helper.createNetFromFile(net_file)





nn.forward_prop()





print(nn)