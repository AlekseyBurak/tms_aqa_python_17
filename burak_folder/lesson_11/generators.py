

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