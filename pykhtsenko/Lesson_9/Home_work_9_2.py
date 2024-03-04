# первый способ реализации

#class BankCard:
  # def __init__(self):
        #self.card_number = int(input("Input card number"))
       # self.name_cardholder = str(input("Input Name and Surnamme of the Card holder"))
        #self.__code_CCV = int(input("Input code CCV"))
       # print(f"Name : {self.name_cardholder} Card number:{self.card_number}")

#new_BankCard = BankCard()
#print(new_BankCard)

# второй способ
class BankCard:
    def __init__(self, card_number, name_cardholder, code_CCV):
        self.card_number = card_number
        self.name_cardholder = name_cardholder
        self.__code_CCV = code_CCV
    def get_card_number(self):
        return self.card_number
    def get_name_cardholder(self):
        return self.name_cardholder
BankCard1 = BankCard("5555 8888 4444 5555", "Peter Pen", "123")
print(BankCard1.get_card_number())
print(BankCard1.get_name_cardholder())


