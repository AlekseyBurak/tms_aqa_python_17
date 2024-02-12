# ввод числа пользователем в диапазоне 0-255

a = 0
b = 255
user_print = int(input('Введите число от 0 до 255: '))
if user_print < a or user_print > b:
    print("Ошибка! Введите число от 0 до 255")
else:
    print(chr(user_print))
