class Line:
    def __init__(self):
        self.right_border = int(input("Input right border"))
        self.left_border = int(input("Input left border"))

    def length(self):
        return abs(self.right_border - self.left_border)

sum_line = Line()
print("length:", sum_line.length())




