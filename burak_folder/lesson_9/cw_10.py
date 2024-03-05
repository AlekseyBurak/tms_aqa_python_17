

class Cat:

    def __init__(self):
        self.paws = 4
        self.tail = True
        self.__lives = 9

    @property
    def lives(self):
        return self.__lives


murzik = Cat()
print(murzik.lives)
