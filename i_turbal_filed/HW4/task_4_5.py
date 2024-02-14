#Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
#Напишите программу, которая будет выводить уникальное число

numbersString = input("Enter your numbers by spaces:" + " ") #Вводим значение
numberList = numbersString.split() # Преобразуем введнную строку в массив
uniqueElements = [] # Объявляем пустой список для записи найденных совпадений
for num in numberList: # перебор элементов массива
    if numberList.count(num) == 1: # проверяем является ли элемент уникальным
        uniqueElements.append(num) # если да, то записываем

if not uniqueElements:
    print("Your array doesn't have uniqueElements")
else:
    print(uniqueElements)





