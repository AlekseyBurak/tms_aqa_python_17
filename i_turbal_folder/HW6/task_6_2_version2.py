def summa(x,y):
    return x + y
def minus(x,y):
    return x - y

def umn(x,y):
    return x * y

def delу(x,y):
    if y == 0:
        return "Делить на ноль нельзя"
    else:
        return x / y


print("""
    Выберите операцию:
    1. Сложнение
    2. Вычитание
    3. Умножение
    4. деление 
    5. Выход
    """)
while True:
    oper = input("ВВедите операцию")
    if oper == "5":
        break
    elif oper not in "12345":
        print("You crash my programm, Thanks, man!")
        break
    x = int(input('First number'))
    y = int(input("Second number"))
    if oper == "1":
        result = summa(x,y)
    elif oper == "2":
        result = minus(x,y)
    elif oper == "3":
        result = umn(x,y)
    elif oper == '4':
        result = delу(x,y)
    print(result)

