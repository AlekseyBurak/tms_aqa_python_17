import textwrap


class Tinkoff:

    def __init__(self, card_number: int, cardholder_name: str, cvv: int):
        self._card_number = card_number
        self._cardholder_name = cardholder_name
        self.__cvv = cvv

    @property
    def get_card_number(self):
        print(textwrap.wrap(str(self._card_number), 4))
        return " ".join(textwrap.wrap(str(self._card_number), 4))

    @property
    def get_cardholder_name(self):
        return self._cardholder_name

    @property
    def get_cvv(self):
        return self.__cvv


my_card = Tinkoff(1234567890123456, "AB", 123)


print(my_card.get_card_number)
print(my_card.get_cardholder_name)
print(my_card.get_cvv)


