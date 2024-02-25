#Петя в строю
def petya(stroi: list, a: int):
    place = 0
    for i in range(len(stroi)):
        if stroi[i] >= a:
            place += 1
    print(f"Петя номер {place} в строю")


petya([165, 163, 162, 160, 157, 157, 155, 154], int(input('Введите рост Пети:\n')))


#элемент больше предыдущего
def spisok1():
    spisok = [int(i) for i in input('Введите числа списка\n').split()]
    new_spisok = []
    for i in range (len(spisok)):
        if spisok[i] > spisok[i-1]:
            new_spisok.append(spisok[i])
    print(new_spisok)


spisok1()
