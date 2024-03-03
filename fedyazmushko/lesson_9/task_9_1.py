class Room:
    def __init__(self):
        self.height = float(input("Введите высоту комнаты: "))
        self.width = float(input("Введите ширину комнаты: "))
        self.depth = float(input("Введите глубину комнаты: "))
        self.floor_area = self.width * self.depth
        self.wall_area = 2 * self.height * (self.width + self.depth)

    def add_door_or_window(self, door_or_window_width, door_or_window_height):
        self.wall_area -= door_or_window_width * self.height
        self.wall_area -= door_or_window_height * self.width

    def get_working_wall_area(self):
        return self.wall_area


room = Room()
door_or_window_width = float(input("Введите ширину двери или окна: "))
door_or_window_height = float(input("Введите высоту двери или окна: "))
room.add_door_or_window(door_or_window_width, door_or_window_height)
print("Рабочая площадь стен без дверей и окон:", room.get_working_wall_area())
