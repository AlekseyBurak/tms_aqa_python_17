
# сделайте класс Линия. При создании спрашивать левую и правую границу (-5, 10).
# добавить функцию которая вернет длину этого отрезка (в моем примере это 15)

class Line:
    def __init__(self, left_border,  right_border):
        self.left_border = left_border
        self.right_border = right_border

    def length(self):
        return abs(self.right_border - self.left_border)

leght_line = Line(4, 10)
print(f"length: {leght_line.length()}")

