# задача про быков и коров реализованная с функциями
# для ускорения проверки принимаются 3-хзначние числа
import random
#функция проверки правильности ввода числа
def proverka(a):
    rez = False
    while rez != True:
        if len(set(a)) != 3:
            print("Принимается 3-хзначное число с разными цифрами")
            a = list(input("Введите ваше число: "))
        if len(a) != 3:
            print("Принимается 3-хзначное число с разными цифрами")
            a = list(input("Введите ваше число: "))
        elif len(set(a)) == len(a) == 3:
            rez = True
    return a

#функция подсчеты быков и коров в числе
def podschet(my, x):
    kor = 0
    bik = 0
    c = list(range(10))
    for c in my:
        if c in x:
            if my.index(c) == x.index(c):
                bik += 1
            else:
                kor += 1
    return print(f"текущий результат коров {kor} и быков {bik}")


cifr = list(range(10))
x_num = [str(cifr.pop(random.randrange(0, len(cifr)))) for _ in range(3)]

while True:
    my_num = list(input("Введите ваше число: "))
    proverka(my_num)
    podschet(my_num, x_num)
    if my_num == x_num:
        print("Вы угадали!")
        break
