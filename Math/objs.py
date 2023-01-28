import random



    
class Mat:
  # Rows = num of rows, cols, etc
  # Prefill: If str 'zeroes' initialize all zeroes
  # If type is touple, look for asking for random and range in touple
    def __init__(self, rows, cols, prefill):
        self.rows = rows
        self.cols = cols
        self.row = []
        self.mat = []
        self.prefill = prefill
        # Check if we init random matrix range
        if type(prefill) is tuple and prefill[0] == "rand":
            for i in range(0,rows):
                for j in range(0,cols):
                    self.row.append(random.uniform(prefill[1],prefill[2]))
                self.mat.append(self.row)
                self.row = []
                
           
        # Check if we init zero matrix
        elif type(prefill) is tuple and prefill[0] == "zeroes":
            
            for i in range(0,rows):
                for j in range(0,cols):
                    self.row.append(0)
                self.mat.append(self.row)
                self.row = []
            
                
    def __str__(self):
        text = "\nRows: "+ str(self.rows) +" Cols: "+ str(self.cols) +" Precision: "+ str(self.prefill[3])+"\n["
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                if(self.prefill[3] >= 0 and self.prefill[3] <=18):
                    val = str(round(self.mat[i][j],self.prefill[3]))
                else:
                    val = str(self.mat[i][j])
                if(i >0 and j==0):
                    if self.mat[i][j] >= 0:
                        text = text + " "
                        
                if(j == self.cols-1):
                    text = text + val
                else:
                    text = text + val + ", "
            if(j == self.cols-1 and i !=self.rows-1):   
                text = text + "\n"
        text = text + "]\n"  
        return text
            
    def __mul__(self, other):
        if(self.cols != other.rows):
            print("\n Invalid Matrix Product Dimensions!\n")
            #return None
        if self.prefill[3] >= other.prefill[3]:
            precision = self.prefill[3]
        else:
            precision = other.prefill[3]
        result = Mat(self.rows,other.cols,("zeroes",0,0,precision))
        for i in range(0,self.rows):
            for j in range(0,other.cols):
                for k in range(0,other.rows):
                    result.mat[i][j] += self.mat[i][k] * other.mat[k][j]
                
        return result
    def __add__(self, other):
        
        if(self.rows == other.rows and self.cols == other.cols):
            if self.prefill[3] >= other.prefill[3]:
                precision = self.prefill[3]
            else:
                precision = other.prefill[3]
            result = Mat(self.rows,self.cols,("zeroes",0,0,precision))
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                        result.mat[i][j] = self.mat[i][j] + other.mat[i][j]
        else:
            print("\n Invalid Matrix Addition Dimensions!\n")
            return None
        return result
    
    def __sub__(self, other):
        
        if(self.rows == other.rows and self.cols == other.cols):
            if self.prefill[3] >= other.prefill[3]:
                precision = self.prefill[3]
            else:
                precision = other.prefill[3]
            result = Mat(self.rows,self.cols,("zeroes",0,0,precision))
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                        result.mat[i][j] = self.mat[i][j] - other.mat[i][j]
        else:
            print("\n Invalid Matrix Subtraction Dimensions!\n")
            return None
        return result
    
    def __rmul__(self, other):
        if(type(other) is int or type(other) is float):
            result = Mat(self.rows,self.cols,("zeroes",0,0,self.prefill[3]))
            for i in range(0,self.rows):
                for j in range(0,self.cols):
                    result.mat[i][j] = self.mat[i][j]*other
        return result
       
        
""" class Vec:
  # Rows = num of rows, cols, etc
  # Prefill: If str 'zeroes' initialize all zeroes
  # If type is touple, look for asking for random and range in touple
    def __init__(self, len, prefill):
        self.len = len
        self.vec = []
        self.prefill = prefill
        # Check if we init random matrix range
        if type(prefill) is tuple and prefill[0] == "rand":
            for j in range(0,len):
                self.vec.append(random.uniform(prefill[1],prefill[2]))
        
                

    def __str__(self):
        text = "\nVector:\nLength: "+ str(self.len) +" Precision: "+ str(self.prefill[3])+"\n["
        for i in range(0,self.len):
            if(self.prefill[3] >= 0 and self.prefill[3] <=18):
                #val = str(round(self.vec[i]),self.prefill[3])
                val = str(round(self.vec[i],self.prefill[3]))
            else:
                val = str(self.vec[i])
            if(i != self.len-1):
                text = text + val + ", "
            else:
                text = text + val
        text = text + "]\n"
        return text """
        


