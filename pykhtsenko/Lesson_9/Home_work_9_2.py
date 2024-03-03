# первый способ реализации

class BankCard:
   def __init__(self):
        self.card_number = int(input("Input card number"))
        self.name_cardholder = str(input("Input Name and Surnamme of the Card holder"))
        self.__code_CCV = int(input("Input code CCV"))
        print(f"Name : {self.name_cardholder} Card number:{self.card_number}")

new_BankCard = BankCard()
print(new_BankCard)



