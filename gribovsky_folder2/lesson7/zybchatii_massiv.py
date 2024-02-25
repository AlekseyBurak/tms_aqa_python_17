x = [1, 2, [3, 4, [5, 6], 7], [8, [9, [1011]]]]
lst = []
map_str = [str(i) for i in x]
print(map_str)
for i in map_str:
    if len(i) == 1:
        lst.append(i)
    # print(lst)
    else:
        a = [str(j) for j in i]
        print(a)
        for ind in range(len(a)):
            if a[ind].isdigit():
                b = ''
                b += a[ind]
                lst.append(b)
                break
            if a[ind].isdigit() and not a[ind+1].isdigit() and not a[ind-1].isdigit():
                lst.append(a[ind])

print(lst)
