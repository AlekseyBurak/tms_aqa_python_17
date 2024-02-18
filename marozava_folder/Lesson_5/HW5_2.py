# Задача с бутылками из крепкого орешка 3. Есть два ведра - 3 литра и 5 литров. Нужно чтобы в одном из ведер оказалось 4 литра ровно.
# Написать программу, которая спрашивает у пользователя что-куда нужно переливать из предложенных вариантов (перелить из малого
# в большое — из большоего в малое — вылить воду из малого — вылить из большого — налить доверху в малое — налить доверху в большое).
# при успешном решении сообщить об этом в консоли


max_bucket3 = 3
max_bucket5 = 5
current_bucket_3 = 0
current_bucket_5 = 0
while True:
    print(f'Трёхлитровое ведро содержит {current_bucket_3}l \n'
          f'Пятилитровое ведро содержит {current_bucket_5}l')
    print('Выберите команду: 1. Перелить из малого в большое \n'
          '2. Из большоего в малое \n'
          '3. Вылить воду из малого \n'
          '4. Вылить воду из большого \n'
          '5. Налить доверху в малое \n'
          '6. Налить доверху в большое \n')
    command = int(input())
    if command == 1:
        if current_bucket_5 == max_bucket5:
            print('Большое ведро уже полное')
            continue
        empty_space5 = max_bucket5 - current_bucket_5
        if empty_space5 >= current_bucket_3:
            current_bucket_5 = current_bucket_5 + current_bucket_3
            current_bucket_3 = 0
        else:
            current_bucket_5 = 5
            current_bucket_3 = current_bucket_3 - empty_space5
    elif command == 2:
        if current_bucket_3 == max_bucket3:
            print('Малое ведро уже полное')
            continue
        empty_space3 = max_bucket3 - current_bucket_3
        if empty_space3 >= current_bucket_5:
            current_bucket_3 = current_bucket_3 + current_bucket_5
            current_bucket_5 = 0
        else:
            current_bucket_3 = 3
            current_bucket_5 = current_bucket_5 - empty_space3
    elif command == 3:
        current_bucket_3 = 0
    elif command == 4:
        current_bucket_5 = 0
    elif command == 5:
        current_bucket_3 = max_bucket3
    elif command == 6:
        current_bucket_5 = max_bucket5

    if current_bucket_5 == 4:
        print('Условие выполнено. В ведре 4 литра')
        break









