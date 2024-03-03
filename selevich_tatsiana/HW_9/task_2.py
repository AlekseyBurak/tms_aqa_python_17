class BankCard:
    def __init__(self, card_number: str, holder_name: str, cvv: str) -> None:
        """
        :param card_number: card number
        :param holder_name: holder name
        :param cvv: cvv
        """
        self.card_number = card_number
        self.holder_name = holder_name
        self.__cvv = cvv

    def get_card_number(self) -> str:
        """
        This function returns card number.
        :return: card number
        """
        return self.card_number

    def get_holder_name(self) -> str:
        """
        This function returns holder name.
        :return: holder name
        """
        return self.holder_name


card = BankCard('4721521252346313', 'Tanya', '356')
print(card.get_card_number())
print(card.get_holder_name())
