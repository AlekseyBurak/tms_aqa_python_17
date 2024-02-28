def my_dek_fun(func):

    def wrapper():
        print("начало")
        result = func()
        print ("конец")
        return result
    return wrapper

@my_dek_fun
def my_fun2():
    xx = "some for return"
    print("привет из май_фун2")
    return xx

#my_fun2()
# x_s = s.lower()
y = my_fun2()
print(y)