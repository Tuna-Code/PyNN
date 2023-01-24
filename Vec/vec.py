class Vector:
  def __init__(self, rows, cols, prefill):
    self.rows = rows
    self.cols = cols
    self.row = []
    self.col = []
    for i in range(0,rows):
        for j in range(0,cols):
            print("Pos: " + str(i) + " " + str(j))
            if(prefill=="zero"):
                self.row.append(0)
            else:
                self.row.append(1)
        self.col.append(self.row)
        self.row = []


v1 = Vector(3,5,"zerro")
print(v1.col)