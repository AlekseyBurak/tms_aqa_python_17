class Room:
    def razmer(self, h, w, g):
        if h <= 0 or w <= 0 or g <= 0:
            print("Параметры комнаты должны быть положительными")
            return
        self.h = h
        self.w = w
        self.g = g
#Нахожу площадь пола и площадь стен
        self.s_pola = w * g
        self.s_sten = 2 * ((h * w) + (h * g))
# это двери и окна на потом
        self.d_and_w = []

    def proem(self, h, w):
        if w <= 0 or h <= 0:
            raise ValueError("Размеры двери или окна должны быть положительными")
        if w > self.w or h > self.h:
            raise ValueError ("Дверь или окно не должны быть больше стены")
        self.d_and_w.append((h,w)) #добавила размеры проёма

    def work_s(self):
        s_proem = 0 # это общая площадь проёмов
        for x_proem in self.d_and_w:
            s_proem += x_proem[0] * x_proem[1]
        # Вычитаем площадь дверей и окон из площади стен
        return self.s_sten - s_proem

komnata = Room()
komnata.razmer(2, 3, 4)
print(f"площадь пола: {komnata.s_pola} \n"
    f"площадь стен: {komnata.s_sten}")
komnata.proem(1, 2.2) #это окно
komnata.proem(2, 0.9) #это дверь
print(f"размеры проемов: {komnata.d_and_w}")
print(f"рабочая площадь: {komnata.work_s()}")