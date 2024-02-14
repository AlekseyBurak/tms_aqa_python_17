#Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6

array_1 = ["My", "project", "lalala", "complex", "complicated", "e2e", "but", "I", "can", "handle"]
array_1.insert(3, "is")
#del array_1[6] OR
array_1.remove("e2e")
print(array_1)