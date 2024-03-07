class Room:
    def __init__(self, h, w, g):
        self.h = h
        self.w = w
        self.g = g

    def razmer(self):
        if self.h <= 0 or self.w <= 0 or self.g <= 0:
            raise ValueError("Параметры комнаты должны быть положительными")
        # Нахожу площадь пола и площадь стен
        self.s_pola = self.w * self.g
        self.s_sten = 2 * ((self.h * self.w) + (self.h * self.g))
        # это двери и окна на потом
        self.d_and_w = []

komnata = Room(2, 3, 5)
komnata.razmer()
print(f"площадь пола: {komnata.s_pola} \n"
   f"площадь стен: {komnata.s_sten}")