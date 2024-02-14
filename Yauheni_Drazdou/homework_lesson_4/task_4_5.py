#5 найти непарное число
l = [1, 2, 3, 2, 1]
for i in l:
    if l.count(i) == 1:
        print(i)