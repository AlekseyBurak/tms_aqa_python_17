print("HomeWork 6 Task 2 - Калькулятор")
# лямбда-функция вычитания вызывается прямо в теле задачи
# операция умножения выполняется без функций
# лямбда-функции сложения
f_sum = lambda x, y : x + y
# просто функция деления
def f_del(x,y):
    if y == 0:
        return "Нельзя делить на 0"
    else:
        return x / y

# функция самого калькулятора
def kalk ():
    while True:
        komanda = input("""
        Какую операцию выполнить:
        1 - Сложение
        2 - Вычитание
        3 - Умножение
        4 - Деление
        Выберите 5 чтобы выйти из калькулятора
        Ваша команда: 
        """)
        if komanda not in list("12345"):
            print(("Неверная команда"))
            continue
        if komanda == "5":
            break
        n1 = float(input("Введите первое число: "))
        n2 = float(input("Введите второе число: "))
        if komanda == "1":
            print(f_sum(n1, n2))
        elif komanda == "2":
            print((lambda x, y : x - y) (n1, n2))
        elif komanda == "3":
            print(n1 * n2)
        elif komanda == "4":
            print(f_del(n1, n2))
            # if n2 == 0:
            #     print("Нельзя делить на 0")
            #     continue
            # print(n1 / n2)

# вызов калькулятора
kalk()

