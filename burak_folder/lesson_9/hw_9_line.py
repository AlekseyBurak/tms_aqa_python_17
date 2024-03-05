import math


class Line:

    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def calculate_distance(self):
        return math.dist([self.point_1, 0], [self.point_2, 0])


line = Line(-10, 5)
print(line.calculate_distance())
