def reverse_num(number: int) -> int:
   list_num = list(str(number))
   list_num.reverse()
   reverse_int = int(''.join(list_num))
   print(reverse_int)
   return reverse_int

reverse_num(12345)



# замыкания

def outter_function(x):
    print("Outer_function", x)
    def inner_function(y):
        print("Inne_functionr", y)
        return x + y

    return inner_function

closure = outter_function(10)
print(closure(5))



# Lambda
def my_func(x):
    return  x ** 2

f = lambda x: x ** 2
print(f(4))



my_list = [1,2,3,4,5,4,2,9,5,4]

# map_str = list()
# for item in my_list
#     map_str.append(str(item))

# def func(x):
#     return x ** 2 / x ** 3

# map_str = map(func, my_list)
# print(list(map_str))


# map_str = map(lambda x: x ** 2 / x ** 3, my_list)
# print(list(map_str))


#filtr
# my_filter = [x for x in my_list if x < 5]
# print(my_filter)

# my_filter = filter(lambda x: x < 5, my_list)
# print(list(my_filter))
#
#
# my_str_list = ["aaa", "bbbb", "cccc", "aaaaaaaaa", "aaaaaaaaaaa"]
# my_filtered_lambda = filter(lambda x: len(x) < 5, my_str_list)
# print(list(my_filtered_lambda))
#
# f = lambda a, b, c: a + b + c
# print(f(1,2,3))