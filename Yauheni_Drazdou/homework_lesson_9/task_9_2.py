#task about line
class Line:
    def __init__(self, left: float, right: float):
        self.left = left
        self.right = right

    def length(self):
        if self.right < self.left:
            print("That's impossible right point should be higher than left point")
        else:
            return self.right - self.left

line = Line(-4, -1)
print(line.length())