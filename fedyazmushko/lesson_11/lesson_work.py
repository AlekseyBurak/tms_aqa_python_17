def myyy_generator():
    for i in "string":
        yield i

def my_func():
    for i in "string":
        return i

g = myyy_generator()
f = my_func()
print(my_func())
print(my_func())
