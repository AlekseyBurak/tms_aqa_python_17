# Списки
# #l = []
# #l = list()
# l = [1, 3443, "text", 0.9, None, True, False, [1, 2], (1, 3), {1, 4}]
# l1 = list("text") # разбило по буквам
# print(l)
# print(l1)

#l = [1, 3443, "text", 0.9, None, True, False, [1, 2], (1, 3), {1, 4}]
#text = "text"
#print(l[-10]) # получить что-то из списка
#print(l[2:5]) #получить данные из промежутка
#print(l[5:2:-1]) #получить данные из промежутка через шаг (список перевернулся)

# l = [3, 2, 1]
# new_l = l.copy()
# print(l.copy())

# l = [3, 2, 1]
# new_l = l.copy()
# new_l.reverse()
# print(new_l)
# print(l)

# l = [3, 2, 1, 5,8] #сортировка
# print(l.sort(reverse=True))
# print(l)

# l = [3, 3, 3, 2, 1]
# l.append(4) добавляет в список
# l.insert(0, 4) добавить на определенную позицию
# l.remove(3) удаляет
# l.clear() очистка
# print(l.count()) узнать что в списке
# print(l)

# print(type(()))
# print(type((1)))

l_unpack = [1, 2, 3] распоковка
a, b, c = l_unpack
print(b)