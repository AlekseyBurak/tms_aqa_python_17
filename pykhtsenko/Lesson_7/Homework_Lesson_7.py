import random

def isContainText(inp_list):
    isContainText = False
    for item in inp_list:
        if item.isalpha():
            isContainText = True
            break
    return isContainText

def getUserInput(comp_list):
    isInputInProcess = True
    while isInputInProcess:
        print(f"Компьютерные цифры: {comp_list}")
        print("Введите число!")
        inp = input()
        inp_list = list(str(inp))

        if (isContainText(inp_list)):
            print(f"Нужно вводить только цифры. Попробуйте еще раз!")
            continue

        user_list = [int(item) for item in list(str(inp))]
        if (len(user_list) != 4):
            print(f"Введено {len(user_list)} цифры, нужно: 4. Попробуйте еще раз!")
            continue
        else:
            for item in user_list:
                if user_list.count(item) > 1:
                    print("Есть одинаковые, попробуйте еще раз!")
                    continue
        isInputInProcess = False

    print(f"Введенные цифры: {user_list}")

    return user_list


def isResultCorrect(comp_list, user_list):
    cows = 0;
    bulls = 0;
    for idx1, elem1 in enumerate(user_list):
        for idx2, elem2 in enumerate(comp_list):
            if (elem2 == elem1):
                if (idx1 == idx2):
                    bulls += 1
                else:
                    cows += 1

    print(f"коровы: {cows}")
    print(f"быки: {bulls}")

    if (bulls > cows):
        print(f"Быков больше,чем коров! Игра закончена!")
        return True
    else:
        print(f"Быков меньше,чем коров! Игра продолжается...")
        return False

comp_list = random.sample(range(1, 10), 4)

isGameCompleted = False
while not isGameCompleted:
    user_list = getUserInput(comp_list)
    isGameCompleted = isResultCorrect(comp_list, user_list)