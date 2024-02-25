user_number = 1111


def verification():
    global user_number
    while True:
        if user_number.isdigit() and not len(list(user_number)) != 4:
            # print("User entered valid number")
            break
        else:
            print("Your number is invalid. Enter new number")
            user_number = input("введите 4-значное число с неповторяющимися цифрами и нажмите ввод: ")


def cow_bulls(x: int):
    global user_number
    lst_1 = list(map(int, str(x)))
    lst_2 = []
    counter_bikov = 0
    counter_korov = 0
    while lst_1 != lst_2:
        user_number = input("введите 4-значное число с неповторяющимися цифрами и нажмите ввод: ")
        verification()
        lst_2 = list(map(int, str(user_number)))
        for i in range(len(lst_2)):
            if lst_2[i] in lst_1 and lst_2[i] == lst_1[i]:
                counter_bikov += 1
            elif lst_2[i] in lst_1 and lst_2[i] != lst_1[i]:
                counter_korov += 1
        print(
            f'{counter_bikov} бык' if counter_bikov == 1 else f'{counter_bikov} быков' if counter_bikov == 0 else f'{counter_bikov} быка',
            f'{counter_korov} корова' if counter_korov == 1 else f'{counter_korov} коров' if counter_korov == 0 else f'{counter_korov} коровы')
        counter_korov = 0
        counter_bikov = 0
    print(f'Ты победил, было загадано число {x}')


cow_bulls(1234)


