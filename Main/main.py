from Math.objs import Mat
from Net.net import Net
import net_helper
import os
from GUI.gui import Gui
os.system("clear")


gui = Gui()


net_file = gui.file_select()


nn = net_helper.createNetFromFile(net_file)





nn.forward_prop()



#nn.forward_prop(input, exp_out)


print(nn)