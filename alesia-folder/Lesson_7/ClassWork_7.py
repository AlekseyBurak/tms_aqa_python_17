
# num = int(input("Input a number: "))
# def f(num: int) -> int:
#     if num < 0:
#         print("only positive numbers")
#         return
#     else:
#         l_num = list(str(num))
#         l_num.reverse()
#         reverse_num = int(''.join(l_num))
#         print(reverse_num)
#         return reverse_num
#
#
# f(num)

###

x = "Hello"

def my_fun():
    # global x
    x = "World"
    print(x)

my_fun()
print(x)


def my_f1():
    x1 = "John"

    def my_f2():
        # nonlocal x1
        x1 = "hello"
    my_f2()
    return x1


def out_f(x):
    print(f"Outer function: {x}")

    def inner_f(y):
        print(f"Inner function: {y}")
        return x + y
    return inner_f

close = out_f(10)
print(close(5))

###
# лямбда-функции

#def my_f(x):
#    return x ** 2

f = lambda x: x ** 2   # лямбда всегда что-то вернет

print(f(4))

my_list = [1, 2, 3, 4, 5, 4, 2, 8, 5, 4]
# map_str = list()
# for item in my_list:
#     map_str.append(str(item))
# = [str(item) for ]
# map_str2 = map(str, my_list)
def fun(x):
    return x ** 2 / x ** 3

# map_str3 = map(fun, my_list)
# print(list(map_str3))

# map_str4 = map(lambda x: x ** 2 / x ** 3, my_list)
# print(list(map_str4))

# my_filter = [x for x in my_list if x < 5]

def func_f(x):
    return  x < 5

my_filt = filter(lambda x: x < 5, my_list)

###
my_list_str = ["dddd", "dd", "ddd"]
filt = filter(lambda x: len(x) <= 3, my_list_str)
print(list(filt))

my_dict = {"a": 100, "b": 200, "c": 300}
my_filt_dict = filter(lambda k: k[1] < 300, my_dict.items())
print(list(my_filt_dict))

### функции высшего порядка
def my_sum(x, y):
    return x + y

def my_diff(x, y):
    return x - y
def calc(x, y, func):
    return func(x, y)

print(calc(10, 5, my_sum))
print(calc(10, 5, my_diff))

###

try:
    res = 10 / 0 # "a", 1
    print(res)
except ZeroDivisionError:
    print("no zeros")
except TypeError:
    print("Only integers")
except:
    print("smth wrong")
else:
    print("no problem")
finally:
    print("I'll work in any case")


acc = None
try:
    acc = create_acc()

finally:
    delete_acc()



my_list_1 = [1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rost = [165, 163, 162, 160, 157, 157, 155, 154]
