# домашка на понедельник:
# 1) Напишите класс Комната. при создании должны запрашиваться параметры комнаты (высота, ширина, глубина). прямо в
# конструкторе завести переменную под площадь пола и площадь стен. Добавить функцию которая принимает размеры (ширина и высота)
# двери или окна. при подсчете площади стен окна и двери должны учитываться. Добавьте функцию которая вернула бы рабочую площадь стен
# (без дверей и окон)


class Room:

    def __init__(self, height: int, width: int, depth: int):
        self.height = height
        self.width = width
        self.depth = depth
        self.s_floor = depth * width
        self.s_walls = 2 * (depth * height + width * height)
        self.s_wd = 0

    def windows_doors(self, height: int, width: int):
        self.s_wd = height * width + self.s_wd

    def total_wall_square(self):
        return self.s_walls

    def wall_without_windows_doors(self):
        return self.s_walls - self.s_wd

    def floor(self):
        return self.s_floor


room = Room(12, 30, 5)
room.windows_doors(2, 1)
room.windows_doors(2, 2)
print('Square without windows and doors = ', room.wall_without_windows_doors())
print('Total walls square = ', room.total_wall_square())







