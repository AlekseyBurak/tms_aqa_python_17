
"""
Generators
"""
def my_generator():
    for i in range(4):
        yield i ** 2


my_g = my_generator()

g = (x ** 2 for x in range(4))


g_but_another_way = iter([x ** 2 for x in range(4)])


for i in my_g:
    print(i)

for y in g:
    print(y)

for z in g_but_another_way:
    print(z)

"""
Iterators
"""

a = [10, 20, 30, 40, 50, 60]
iter(a)
iterator = a.__iter__()
print(iterator.__next__())
print(next(iterator))


for item in iter(a):
    print(item)


for item in a:
    print(item)



"""
Work with files
'r'	открытие на чтение (является значением по умолчанию).
'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
'x'	открытие на запись, если файла не существует, иначе исключение.
'a'	открытие на дозапись, информация добавляется в конец файла.
"""
import time

with open("test.log", "r") as f:
    for _ in range(25):
        print(next(f), end='')
    # for index in range(100_000):
    #     f.write(f"{index} -- I am some valuable text. \n")



# with open("Harry_Potter_1.txt", "w") as f:
#     for index in range(3):
#         f.write(f"{index} -- I won't lie. \n")