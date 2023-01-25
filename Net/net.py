from Net.layer import Layer

class Net:
    def __init__(self, layers):
        self.layers = layers
        print(layers)
        #Loop Through each Layer
        for i in range(0,len(layers)):
            print(i)