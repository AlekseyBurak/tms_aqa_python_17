class BankCard:
    def zakaz_card(self, card_holder, card_number, cvv):
        self.card_holder = card_holder
        self._card_number = card_number
        self.__cvv = cvv

    def get_card_holder(self):
        return self.card_holder


    def get_card_number(self):
        return self._card_number

k = BankCard()
k.zakaz_card("Oksana", 123456789, 333)
print(k.get_card_holder())
print(k.get_card_number())
