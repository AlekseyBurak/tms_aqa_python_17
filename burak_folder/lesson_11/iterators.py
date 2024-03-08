import itertools

a = [10, 20, 30, 40, 50, 60]
iter(a)
iterator = a.__iter__()
print(iterator.__next__())
print(next(iterator))


for item in iter(a):
    print(item)


for item in a:
    print(item)