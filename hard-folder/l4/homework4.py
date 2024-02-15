#1
s = input()
print(s.split())

#2
l = ['Ivan', 'Ivanou']
a = 'Minsk'
c = 'Belarus'
b = ' '.join(l)
print(f'Привет, {b}! Добро пожаловать в {a} {c}')

#3
list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(list))

#4
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list.insert(2, 77)
del list[6]
print(list)