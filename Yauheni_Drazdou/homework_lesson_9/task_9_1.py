#task about room's size
class Room:
    def __init__(self, name: str, height: float, width: float, length: float):
        self.name = name
        self.height = height
        self.width = width
        self.length = length
        self.floor = width * length
        self.walls = height * (2 * (width + length))

    def useful_walls(self, okno_width: float, okno_height: float,
                      dver_width: float, dver_height: float):
        """
                             this function defines parametrs of door's and window's size
                             and counts useful square
                             :param okno_width: width of the window
                             :param okno_height: height of the window
                             :param dver_width: width of the door
                             :param dver_height: height of the door
                             :return: usefull square of the walls
                             """
        self.walls -= okno_width * okno_height + dver_width * dver_height


zal = Room("Zal", 3, 5.3, 4.1)
print(zal.walls)
zal.useful_walls(1.2, 1.5, 1.5, 2.3)
print(zal.walls)