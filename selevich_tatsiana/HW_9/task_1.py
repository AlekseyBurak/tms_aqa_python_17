class Line:
    def __init__(self, left_border: float, right_border: float) -> None:
        """
        :param left_border: left border of the line
        :param right_border: right border of the line
        """
        self.left_border = left_border
        self.right_border = right_border

    def get_length(self) -> float:
        """
        This function determines the length of the line.
        :return: line length
        """
        return self.right_border - self.left_border


line = Line(3.1, 5.9)
print(line.get_length())
