a = input().split()
for i in range(len(a)):
    c=a[:i]+a[i+1:]
    if a[i] not in c:
        print(a[i])