#Создайте список из 10 элементов,
# вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6

newList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
addItem = newList.insert(2, "What?")
deleteItem = newList.pop(5)
print(newList)