home_list = [1, 5, 2, 4, 3]
home_list1 = [1, 2, 3, 4, 5]

result_list = []
result_list1 = []


for i in range(1, len(home_list)):
    if home_list[i] > home_list[i-1]:
        result_list.append(home_list[i])

print(result_list)

for i in range(1, len(home_list1)):
    if home_list[i] != home_list[i-1]:
        result_list1.append(home_list1[i])

print(result_list1)




def flatten_nested_array(nested_array):
    flat_list = []
    i = 0
    while i < len(nested_array):
        if isinstance(nested_array[i], list):
            print(nested_array[:i])
            print(nested_array[i])
            print(nested_array[i+1:])
            nested_array = nested_array[:i] + nested_array[i] + nested_array[i+1:]
        else:
            i += 1

    for item in nested_array:
        flat_list.append(item)

    return flat_list

nested_array = [1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]]]




