class Line:
    def __init__(self, left_border, right_border):
        self.left_border = left_border
        self.right_border = right_border

    __init__(left_border=-5, right_border=10)

    def get_length(self):
        return abs(self.right_border - self.left_border)

line = Line()
print("Длина отрезка: ", line.get_length())