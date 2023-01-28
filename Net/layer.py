from Math.objs import Mat


class Layer:
    def __init__(self, num, num_nodes, actv_func):
        prefill = ("zeroes",0,0,-1)
        self.input = Mat(num_nodes, 1, prefill)
        self.output = Mat(num_nodes, 1, prefill)
        self.bias= Mat(num_nodes, 1, prefill)
        self.actv_func = actv_func
        self.weights = [[0]]
        self.num = num
        self.num_nodes = num_nodes


    def __str__(self):
        text = "\n-------L" + str(self.num) + "-------\n"
        text += "Node Count: " + str(self.num_nodes) + " Actv Func: " + self.actv_func
        text += "\nInput:" + self.input.__str__()
        text += "\nOutput:" + self.output.__str__()
        if(self.num != 0):
            text += "\nWeights:" + self.weights.__str__()
        text += "----------------\n"
        return text