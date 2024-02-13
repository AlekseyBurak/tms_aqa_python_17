# task 1 - перевести строку в список
string1 = 'Success does not come to you! You go to it.'
my_list = string1.split()
print(my_list)

# task 2
# Дан список: l=[‘Ivan’, ‘Ivanou’], и 2 строки: а=Minsk, с=Belarus.
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

l = ['Ivan', 'Ivanov']
s1 = 'Minsk'
s2 = 'Belarus'
result = f"Привет, {l[0]} {l[1]}! Добро пожаловать в {s1} {s2}"
print(result)

# task 3 - перевести список в строку
my_list = ['Success', 'does', 'not', 'come', 'to', 'you!', 'You', 'go', 'to', 'it.']
my_string = ' '.join(my_list)
print(my_string)

# task 4 - cоздать список из 10 элементов, вставить на 3-ю позицию новое значение,
# и удалить элемент из списка под индексом 6
my_list = ['1', '2', '3', '4', '5', 'new', '7', '8', '9', '10']
my_list.insert(2, 33)
print(my_list)
del my_list[6]
print(my_list)


