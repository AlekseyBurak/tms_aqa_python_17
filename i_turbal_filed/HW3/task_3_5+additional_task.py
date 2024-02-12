"""
Закоментен  вариант с объявления переменных, внизу без, просто решил сделать два способа и посмотреть
на скорость выполнениня кода
"""
# import time
# start_time = time.time()
#
# enteredSymbol = input("Enter your symbol" + " ")
# numberOfSymbol = int(ord(enteredSymbol))
# counterForCode = len(str(numberOfSymbol))
# print("Your symbol is number ", numberOfSymbol, "in ASCII")
# print("And now you can see magic", numberOfSymbol**0.5/counterForCode)
#
# end_time = time.time()  # время окончания выполнения
# execution_time = end_time - start_time  # вычисляем время выполнения
#
# print(f"Время выполнения программы: {execution_time} секунд") #2.427628517150879


import time
start_time = time.time()

enteredSymbol = input("Enter your symbol" + " ")

print("Your symbol is number ", ord(enteredSymbol), "in ASCII")
print("And now you can see magic", ord(enteredSymbol)**0.5/len(str(ord(enteredSymbol))))

end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения программы: {execution_time} секунд") #2.213710069656372