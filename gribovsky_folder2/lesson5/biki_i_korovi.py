# Быки и коровы

number = 1234  # загаданное число
lst_1 = [int(i) for i in str(number)]
lst_2 = []
counter_bikov = 0
counter_korov = 0
while lst_1 != lst_2:
    lst_2 = [int(i) for i in input("введите 4-значное число с неповторяющимися цифрами и нажмите ввод: ")]
    if len(lst_2) == 4:
        for i in range(len(lst_2)):
            if lst_2[i] in lst_1 and lst_2[i] == lst_1[i]:
                counter_bikov += 1
            elif lst_2[i] in lst_1 and lst_2[i] != lst_1[i]:
                counter_korov += 1
        print(f'{counter_bikov} бык' if counter_bikov == 1 else f'{counter_bikov} быков' if counter_bikov == 0 else f'{counter_bikov} быка',
            f'{counter_korov} корова' if counter_korov == 1 else f'{counter_korov} коров' if counter_korov == 0 else f'{counter_korov} коровы')
        counter_korov = 0
        counter_bikov = 0
    else:
        print("Введено не 4-значное число")
print(f'Ты победил, было загадано число {number}')
