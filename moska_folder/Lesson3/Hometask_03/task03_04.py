# Программа просит пользователя ввести число в ограниченном диапазоне (0 -255).
# В ответ на введенное число она
# выдает пользователю символ код которого в таблице ASCII соответствует введенному числу.

#a = input("Please enter numbers from 0 to 255:\n")

abc = int(input("Input number\n"))
ed = abc % 10
des = abc % 100 // 10
sotki = abc % 1000 // 100

if sotki == 0: print("")
elif sotki > 0: print((ord(str(sotki))))

if des == 0: print("")
elif des > 0: print((ord(str(des))))

if ed == 0: print("")
elif ed > 0: print((ord(str(ed))))
