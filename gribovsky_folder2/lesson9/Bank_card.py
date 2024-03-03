class BankCard:
    def __init__(self, card_number: int, owner_name: str, cvv: int):
        self.card_number = card_number
        self.owner_name = owner_name
        self.__cvv = cvv

    def card_info(self) -> str:
        return f"{self.owner_name} is owner card with {self.card_number} number"

    def set_number(self, number):
        self.card_number = number

    def get_number(self):
        return self.card_number

    def set_name(self, name):
        self.owner_name = name

    def get_name(self):
        return self.owner_name

    def set_cvv(self, cvv):
        self.__cvv = cvv

    def get_cvv(self):
        return self.__cvv


card1 = BankCard(1236545, "Ivan Ivanov", 125)
print(card1.card_info())
print(card1.get_cvv(), "первый способ получить cvv")
print(card1._BankCard__cvv, "второй способ получить cvv")
