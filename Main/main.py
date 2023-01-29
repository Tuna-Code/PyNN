from Math.objs import Mat
from Net.net import Net
import net_helper





nn = net_helper.createNetFromFile("Data/simple/simple.conf")




nn.forward_prop()



#nn.forward_prop(input, exp_out)


