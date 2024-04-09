# дано четырехзначное число. Не превращая его в строку разбить на единицы, десятки,
# сотни и тысячи( пример —- 3674 должно вывести " единицы 4, десятки 7, сотни 6, тысячи 3
import math

while True:
    try:
        enteredValue = int(input("Enter a four digit number" + " "))
        if enteredValue > 999 or enteredValue < 9999:
            # while enteredValue > 0:
            #     print(enteredValue % 10)
            #     enteredValue //= 10

            print("Единицы:", enteredValue % 10)
            enteredValue = enteredValue // 10
            print("Десятные:", enteredValue % 10)
            enteredValue = enteredValue // 10
            print("Сотые:", enteredValue % 10)
            enteredValue = enteredValue // 10
            print("Тысячные:", enteredValue)

        else:
            print("Try again")
        break
    except ValueError:
        print("PLease enter numbers")