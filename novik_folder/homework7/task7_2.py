new_list = [1, 5, 2, 4, 3]
def count_func(new_list):
    for items in range(1, len(new_list)):
        new_list[items] = int(new_list[items])
        if int(new_list[items]) > int(new_list[items-1]):
            print(new_list[items])

print(count_func([1, 5, 2, 4, 6]))