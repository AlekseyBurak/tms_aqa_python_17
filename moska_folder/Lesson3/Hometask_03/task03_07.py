# дано четырехзначное число. Не превращая его в строку разбить на единицы,
# десятки, сотни и тысячи( пример —- 3674 должно вывести " единицы 4,
# десятки 7, сотни 6, тысячи 3


number = int(input('Please input 4 digit number:\n'))
units = number % 10
dozens = number % 100 // 10
hundreds = number % 1000 // 100
thousands = number % 10000 // 1000
print("Дано четырехзначное число: " + str(number) + "\nЕдиницы " + str(units) + ", десятки " + str(dozens) + ", сотни "
      + str(hundreds) + ", тысячи " + str(thousands))
