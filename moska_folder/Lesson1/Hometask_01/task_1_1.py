counter = 0
for i in range(1, 11):
    n = int(input())
    if n % 2 == 0:
        counter += 1
if counter == 10:
    print('YES')
else:
    print('NO')