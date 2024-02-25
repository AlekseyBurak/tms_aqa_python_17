def fun_1():
    print("введите числа через пробел и нажмите ввод")
    lst_1 = [int(i) for i in input().split()]
    lst = []
    if lst_1[1] < lst_1[0]:
        lst.append(lst_1[0])
    for ind in range(len(lst_1)):
        if lst_1[ind] > lst_1[ind - 1]:
            lst.append(lst_1[ind])
    print(lst)


fun_1()