#1) сделайте класс Линия. При создании спрашивать левую и правую границу (-5, 10). д
# обавить функцию которая вернет длину этого отрезка (в моем примере это 15)


# class Line:
#     def __init__(self, left: int, right: int):
#         self.left = left
#         self.righ = right
#
#     def length(self):
#         return self.left + self.righ
#
#
#
# line = Line(1,2)
# print(line.length())

#2) Напишите класс Банковская Карта. При создании запрашиваются номер, имя держателя и CVV.
# Переменная с  CVV должны быть
# скрыта на столько на сколько позволяет питон :)
# добавить методы которые вернут номер и имя (два разных метода)

# class DebitCard:
#     def __init__(self):
#         self.name = input("Enter name: ")
#         self.number = input("Enter number: ")
#         self.__cvv = input("Enter CVV: ")
#     def retunr_name(self):
#         return self.name
#     def return_number(self):
#         return self.number
#
#
# my_card = DebitCard()
# print(my_card.retunr_name())
# print(my_card.return_number())

#Напишите класс Комната. при создании должны запрашиваться параметры комнаты (высота, ширина, глубина).
# прямо в конструкторе завести переменную под площадь пола и площадь стен. +
# Добавить функцию которая принимает размеры (ширина и высота) двери или окна.
# при подсчете площади стен окна и двери должны учитываться.
# Добавьте функцию которая вернула бы рабочую площадь стен (

class Room:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth
        self.floor_area = self.width * self.depth
        self.wall_area = 2 * (self.height * self.width) + 2 * (self.height * self.depth)

    def door_and_window(self, door_width, door_height, window_widht, window_height):
        self.wall_area -= (door_width * door_height) + (window_widht *window_height)
        return self.wall_area



my_rum =Room(3,7,10)
print(my_rum.wall_area)
print(my_rum.door_and_window(1,1,1,1))