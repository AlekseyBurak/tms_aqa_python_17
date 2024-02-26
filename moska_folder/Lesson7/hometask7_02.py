
def change_list(a):
    for i in range(len(a)+1):
        if a[i] > a[i - 1]:
            return a[i]
print(change_list(a=[1, 23, 1, 8, 98]))