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

l_unpack = [1, 2, 3] #распоковка
a, b, c = l_unpack
print(b)



import random

# list_for_example = [1, 21342, "text", 0.9, .9, 1_000_000, None, True, False, [1, 2], (1, 4), {1, 2}, {1: "a"}]
# text = "05:02:1997 - text with a lot of bucov"

#
# print(l)
# print(l1)


# def foo(n: int):
#     print(n ** 2)
#
#
# def bar(n: int):
#     print(n ** 3)
#
# l = [foo, bar]
# # PUT PATCH
#
# for func in l:
#     func(2)


# l = [3, 2, 1]
# new_l = l
# new_l.reverse()
# print(new_l)
# print(l)

# l = [3, 2, 1]
# print(l.copy())



# l = [3, 2, 1, 5, 8]
# print(l.sort())
# print(l)
#
#
# l = [1, 2, 3]
# print(l.sort(reverse=True))
# print(l)

# cars = ['Ford', 'BMW', 'Volvo']
#
# cars.sort()
# print(cars)


# def my_func(e):
#     return len(e)
#
#
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
#
# cars.sort(key=my_func)
# print(cars)

# l_cut = [1, 2, 3, 4, 5, 6]
# print(l_cut[::-1])
# print(l_cut[::2])
# print(l_cut[2:4])
# print(l_cut[4:2])
# print(l_cut[4:2:-1])


# a = [1, 2, 3]
# c = a
# b = [1, 2, 3]
# a = 1
# b = 1
# print(a == b)
# print(a is c)
# print(True is True)
# print(True == True)
#
# print(a == b)
# print(a is b)


# l = [1, 2, 3, 3, 4, 5]
# l.append(16)
# l.append("text")
# l.append([1, 2, 3])
# l.append(None)
# print(f"this line will add smth to list {l.append('hello from f-strng')}")
# print(l)


# print(type(()))
# print(type((1, )))
# t = () Why not?

# print(type([]))
# print(type([1]))
# l = [] Why Ok?

# print(type({}))
# print(type({1}))


# l_unpack = (1, 2, 3, 4, 5, 6, 7, 8)
# a, b, c, *rest = l_unpack
# print(a)
# print(rest)
# print(c)

# text = "this is long string"
# splited = text.split()
# splited[0], splited[2] = splited[2], splited[0]
# new_text = ' '.join(splited)
# print(splited)
# print(new_text)


# l_unpack = [1, 2, 3]
# a, *_ = l_unpack
# print(a)
# print(_)

# s = {1, 2, 3, 4, 5}
# new_s = s.copy()
# s.add(6)
# print(len(s))
# s.clear()
# print(s)
# fr_set = frozenset(s)
# print(type(fr_set))
# # set_1 = {1, 2, 3, [4, 5]}
# set_2 = {1, 2, 3, (4, 5), 1, 2,3, 34}
# print(set_2)

# ord_set = {1, 2, 0.1, True, False, (1, 2), (.1, 2), (True, 1)} # note check True False 0 1
# # Note
# ord_set_zero = {0, 1, 2, True, False} # note check True False 0 1
# ord_set_no_zero = {1, 2, True, False} # note check True False 0 1
# print(ord_set_zero)
# print(ord_set_no_zero)



# Панграмма
# Эй, жлоб! Где туз? Прячь юных съёмщиц в шкаф.
# Pack my box with five dozen liquor jugs
# print(ord_set)
# ord_set.pop()
# print(ord_set)
# ord_set.remove(1)
# print(ord_set)

# a = b = 10
# print(a)
# print(b)
# a = 5
# print(a)
# print(b)
#
# a = b = [1, 2]
# print(a)
# print(b)
# a = [2, 3]
# print(a)
# print(b)

# a = [1, 2]
# b = a
# print(a)
# print(b)
# a = [2, 3]
# print(a)
# print(b)

# a = [1, 2]
# b = a
# print(a)
# print(b)
# a.append(3)
# print(a)
# print(b)

# a = b = [1, 2]
# print(a)
# print(b)
# a.append(3)
# print(a)
# print(b)

# for i in range(1, 5):
#     print(i)
#     if i == 2:
#         print("ups..")
#         break
# else:
#     print("all fine")
# i = 0
# while i < 6:
#     print(i)
#     i += 1
#     if i == 2:
#         print("ups..")
#         break
# else:
#     print("all fine")

# try:
#     print("this is try")
#     # raise TypeError
#     # raise ValueError
# except TypeError:
#     print("TypeError was raised")
# except:
#     print("oups")
# else:
#     print("I'll work if everything was fine")
# finally:
#     print("i'll work in the end")

# a = {1: "1",
#      2: "2",
#      3: "3"}
# a[4] = "4"
# print()
# print(a)
# print(a.popitem())
# a.update({5: "5"})
# a.update([(6, "6"), (7, "7")])
# a.update(a="10")
# print(a)


# dict_1 = {
#     "apple": 10,
#     "banana": 8,
#     "pear": 18,
# }
#
# l = ["text", "wrong text", "no text"]


# num = 0
#
# while num < 8:
#
#     print(f"{num}, Less then 8")
#     num = num + 1
#

# dt = {"a": 1, "b": 2}