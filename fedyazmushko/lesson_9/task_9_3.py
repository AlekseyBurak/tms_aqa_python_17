class BankCard:
    def __init__(self):
        self.card_number = int(input("Введите номер вашей карты: "))
        self.cardholder_name = str(input("Введите имя держателя карты: "))
        self.__CVV = int(input("Введите CVV код: "))

    def get_card_number(self):
        return self.card_number

    def get_cardholder_name(self):
        return self.cardholder_name

card = BankCard()
print("Номер карты: ", card.get_card_number())
print("Имя держателя: ", card.get_cardholder_name())
