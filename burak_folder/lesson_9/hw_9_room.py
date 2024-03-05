

class Room:
    """
    Class for calculating workspace of your room walls
    """

    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length
        self.flour = self.width * self.length
        self.wall_space = (self.length * self.height * 2) + (self.width * self.height * 2)
        self.doors_windows = {}

    def get_doors_or_windows(self):
        """
        Retrieves added doors and windows
        :return:
        """
        return self.doors_windows

    def clear_doors_and_windows(self):
        """
        Clear the dict with doors and windows
        :return:
        """
        self.doors_windows.clear()

    def add_doors_or_windows(self, item_name: str, item_measurements: tuple):
        """
        Add door/window to dict where key is item name and value is a tuple with measurements
        :param item_name: door or window. Must be unique
        :param item_measurements: tuple with item height and width
        :return:
        """
        self.doors_windows[item_name] = item_measurements

    def get_work_space(self):
        """
        Calculate work space with already entered doors windows
        :return:
        """
        result = self.wall_space
        for _, value in self.doors_windows.items():
            result -= value[0] * value[1]
        return result


living_room = Room(1, 1, 1)
living_room.add_doors_or_windows("door", (0.5, 0.5))
print(living_room.get_work_space())