# домашка на понедельник:
# 1) Напишите класс Комната. при создании должны запрашиваться параметры комнаты (высота, ширина, глубина).
# прямо в конструкторе завести переменную под площадь пола и площадь стен.
# Добавить функцию которая принимает размеры (ширина и высота) двери или окна.
# при подсчете площади стен окна и двери должны учитываться.
# Добавьте функцию которая вернула бы рабочую площадь стен (без дверей и окон)

# class My_room:
#
#     def __init__(self):
#         self.area_of_the_walls = None
#         self.height_wall = float(input("Enter the height of the wall: "))
#         self.length_wall_1 = float(input("Enter the length of the first wall: "))
#         self.length_wall_2 = float(input("Enter the length of the second wall: "))
#         self.height_window = float(input("Enter the height of the window: "))
#         self.width_window = float(input("Enter the width of the window: "))
#         self.height_door = float(input("Enter the height of the door: "))
#         self.width_door = float(input("Enter the width of the door: "))
#         self.area_of_the_room = self.length_wall_1 * self.length_wall_2
#         self.area_of_the_walls = (2 * (self.length_wall_1 * self.height_wall) +
#                                   2 * (self.length_wall_2 * self.height_wall))
#
#     def area_without_holes(self):
#         self.area_of_the_walls = (self.area_of_the_walls - (self.height_window * self.width_window) -
#                                   (self.width_door * self.height_door))
#         return self.area_of_the_walls
#
#
# room = My_room()
# print(room.area_of_the_walls)
# print(room.area_without_holes())

# 1) сделайте класс Линия. При создании спрашивать левую и правую границу (-5, 10).
# добавить функцию которая вернет длину этого отрезка (в моем примере это 15)

# class Line:
#
#     def __init__(self):
#         self.distance = None
#         self.left_point = float(input("Enter left point: "))
#         self.right_point = float(input("Enter right point: "))
#
#     def len_of_line(self):
#         self.distance = abs(self.left_point) + abs(self.right_point)
#         return self.distance
#
#
# line = Line()
# print(line.len_of_line())


# 2) Напишите класс Банковская Карта.При  создании запрашиваются   номер, имя держателя
# и  CVV.Переменная  с  CVV должны  быть  скрыта  на столько на сколько позволяет питон:) добавить
# методы которые   вернут   номер и   имя(два разных метода)

class My_card:

    def __init__(self):
        self.b_number = None
        self.CVV = None
        self.bankcard_number = input("Bankcard_number: ")
        self.CVV_code = input("CVV_code: ")

    @property
    def card_number(self):
        count = len(self.bankcard_number)
        if count == 16:
            return "".join(self.bankcard_number)
        else:
            print("Try again")

    @property
    def __secret_code(self):
        count = len(self.CVV_code)
        if count == 3:
            self.CVV = "".join(self.CVV_code)
        else:
            print("Try again")
        return self.CVV


card = My_card()
print(f"Your bankcard number:", card.card_number[:4], card.card_number[4:8],
      card.card_number[8:12], card.card_number[12:16], sep=' ')
print(f"Your CVV:", card._My_card__secret_code, sep=' ')
