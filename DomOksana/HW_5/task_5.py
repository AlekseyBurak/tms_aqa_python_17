print ("введите через запятую числа из массива: ")
a = input().split(',')
print("вот введённый массив:")
print(a)
k = len(a)
i = 0
while i < k:
    b = a[:i] + a[i+1:]
    if a[i] not in b:
        print(f"число не имеющее пары: {a[i]}")
    i += 1

print( f"короткий вариант поиска числа не имеющего пары: {min(a, key = a.count)}")