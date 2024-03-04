
#Напишите класс Банковская Карта. При создании запрашиваются номер, имя держателя и CVV.
# Переменная с  CVV должны быть скрыта на столько на сколько позволяет питон :)
# добавить методы которые вернут номер и имя (два разных метода)

class BankCard:
    def __init__(self, card_number: int,  user_name: str, CVV: int):
        self.card_number = card_number
        self.user_name = user_name
        self.__CVV = CVV

    def get_card_number(self):
        return self.card_number

    def get_user_name(self):
        return self.user_name

    def get_cvv(self):
        return self.__CVV


card_details = BankCard(17161986966, "Anna New", 123)
print(f"Card details: {card_details.get_card_number()}, User name: {card_details.get_user_name()}")
print(f"CVV: {card_details.get_cvv()}")
