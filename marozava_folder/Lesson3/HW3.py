import math

# Задание 1
# 1) Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

# Решение:

# string1 = 'www.my_site.com#about'
# replacement = string1.replace('#', '/')
# print(replacement)

# Задание 2
# 2) Напишите программу, которая добавляет ‘ing’ к словам

# Решение:

# verb = input('Enter any verb: ')
# ending = verb + "ing"
# print(f'Verb in the present continuous: {ending}')

# Задание 3
# Напишите программу которая удаляет пробел в начале и в конце строки

# Решение:

# word = input('Enter any word: ')
# with_spaces = "    " + word + "    "
# print(with_spaces)
# del_spaces = with_spaces.strip()
# print(del_spaces)

# Комментарий: можно сразу вводить с пробелами, но я сделала так, чтобы можно было точно видеть вводимые пробелы.

# Задание 4
# Программа просит пользователя ввести число в ограниченном диапазоне (0 -255).
# В ответ на введенное число она выдает пользователю символ код которого в таблице ASCII  соответствует введенному числу.

# Решение:

# number = int(input('Enter any number from 0 to 255 from the table ASCII: '))
# if number < 0 or number > 255:
#     print('Enter correct number: 0 - 255')
# else:
#     symbol = chr(number)
#     print(symbol)



# Задание 5
# 5) четвертое задание только наоборот. Допустим пользователь будет вводить только одиночные символы
# (в нижнем или верхнем регистре, ТОЛЬКО латиница). Программа должна определить код этого символа и вывести результат.
# +
# Задание 6
# 6) Дополнить пятую задачу так чтобы выводился не просто код символа, а результат деления его квадратного
# корня на длину числа ( 100 ** 0,5 / 3  —- пример —- пускай 100 это код символа, тогда длинна числа три знака

# Решение:

# symbol = input('Enter any symbol: ')
# if len(symbol) > 1:
#     print('Enter one symbol!')
# else:
#     code = ord(symbol)
#     print(f'Code of symbol ASCII: {code}')

#     result = math.sqrt(code) / len(str(code))
#     print(f'Code after math calculations: {result}')

# Задание 7
# дано четырехзначное число. Не превращая его в строку разбить на единицы, десятки, сотни и тысячи
# ( пример —- 3674 должно вывести " единицы 4, десятки 7, сотни 6, тысячи 3

# Решение:

# number = int(input('Please enter 4-digit number: '))
# thousand = number // 1000
# hundred = number % 1000 // 100
# ten = number % 100 // 10
# one = number % 10
# print(f'Тысячи - {thousand}\nСотни - {hundred}\nДесятки - {ten}\nЕдиницы — {one}')