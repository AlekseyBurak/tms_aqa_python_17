class Lin:
    def init(self, lev, prav):
        # Проверяю, что левая граница не дальше правой
        if lev > prav:
            # raise ValueError("Левая граница должна быть меньше или равна правой")
            print("Левая граница должна быть меньше или равна правой")
            return
        self.lev = lev
        self.prav = prav

    def dlina(self):
        return self.prav - self.lev

l = Lin()
l.init(5, 25)
d = l.dlina()
print(d)
