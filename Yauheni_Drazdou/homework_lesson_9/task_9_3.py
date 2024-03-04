#task about card

class Card:
    def __init__(self, cardnum: int, name: str, cvv: int):
        self.cardnum = cardnum
        self.name = name
        self.__cvv = cvv

    def cardname(self):
        print(f"Here is the name on your card {self.name}")

    def cardnumber(self):
        print(f"Here is your card number {self.cardnum}")


my_card = Card(23456, "Yauheni Drazdou", 123)


print(my_card.cardnumber())
print(my_card.cardname())
print(my_card.cvv)
