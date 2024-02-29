n = str(input())
alfavit = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(n)):
    if n[i] in alfavit:
        n[i] == n[i+3]
        print(n[i])
