from Math.objs import Mat


class Layer:
    def __init__(self, num_nodes, actv_func):
        prefill = ("zeroes",0,0,-1)
        self.input = Mat(num_nodes, 1, prefill)
        self.output = Mat(num_nodes, 1, prefill)
        self.actv_func = actv_func


