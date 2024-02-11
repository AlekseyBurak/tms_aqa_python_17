# task_1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
some_string = "www.my_site.com#about#news"
print(some_string.replace("#", "/"))

# task_2. Напишите программу, которая добавляет ‘ing’ к словам
some_word = input("enter some word: ")
print(some_word + "ing")

# task_3. Напишите программу которая удаляет пробел в начале и в конце строки
string_with_space = input("enter any string with space :")
print(string_with_space.strip())

# task_4. Программа просит пользователя ввести число в ограниченном диапазоне (0 -255).
# В ответ на введенное число она выдает пользователю символ код которого в таблице ASCII  соответствует введенному числу
some_number = int(input("enter any number in range 0 - 255: "))
print(chr(some_number))  # есть вопросы по кодам от 0 до 31

# task_5. Допустим пользователь будет вводить только одиночные символы (в нижнем или верхнем регистре, ТОЛЬКО латиница).
# Программа должна определить код этого символа и вывести результат.
some_symbol = input("enter symbol: ")
print(ord(some_symbol))

# task_6. Дополнить пятую задачу так чтобы выводился не просто код символа, а результат деления его квадратного корня
# на длину числа ( 100 ** 0,5 / 3  —- пример —- пускай 100 это код символа, тогда длинна числа три знака
some_symbol_2 = input("enter symbol: ")
# print(ord(some_symbol_2))
# print(len(str(ord(some_symbol_2))))
print(ord(some_symbol_2)**0.5 / len(str(ord(some_symbol_2))))

# task_7. дано четырехзначное число. Не превращая его в строку разбить на единицы, десятки, сотни и тысячи
# ( пример —- 3674 должно вывести " единицы 4, десятки 7, сотни 6, тысячи 3)
any_number = int(input("enter any number :"))
print("тысячи: ", any_number//1000, "\nсотни: ", any_number // 100 % 10,
      "\nдесятки: ", any_number // 10 % 10, "\nединицы: ", any_number % 10)


