class Line:
    def __init__(self, left_border: int, right_border: int):
        self.left_border = left_border
        self.right_border = right_border

    def segment_length(self, *args) -> int:
        if self.left_border < 0:
            segment_length = abs(self.left_border) + abs(self.right_border)
        elif 0 <= self.left_border < self.right_border:
            segment_length = self.right_border - self.left_border
        else:
            while self.left_border > self.right_border:
                print(f"left_border should be less than right_border")
                self.left_border = int(input("enter correct value for left_border: "))
                self.right_border = int(input("enter correct value for right_border: "))
            segment_length = self.right_border - self.left_border

        print(
            f"length of segment with left_border = {self.left_border} and right_border = {self.right_border} is {segment_length}")
        return segment_length


line1 = Line(25, 6)
line1.segment_length()
