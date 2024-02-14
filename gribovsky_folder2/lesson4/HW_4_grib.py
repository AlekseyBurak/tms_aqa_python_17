# task1. Перевести строку в список.
# Пример — "Robin Singh" => ["Robin", “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

any_string = input("enter any string :")
splitted_string = any_string.split()
print(splitted_string)
#
# task2. Дан список: l=[‘Ivan’, ‘Ivanou’], и 2 строки: а=Minsk, с=Belarus.
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

l = ["Ivan", "Ivanou"]
a = "Minsk"
c = "Belarus"
print(f"Привет {' '.join(l)}! Добро пожаловать в {a} {c}")
#
# task3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"

lst_1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
stroka = ' '.join(lst_1)
print(stroka, "\n", type(stroka))

# task4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
lst_2 = [elem for elem in range(10)]
print(lst_2)
lst_2[2] = int(input("new value: "))
lst_2.pop(6)
print(lst_2)

# task5. Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного:
# [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
#
lst = [1, 5, 2, 9, 2, 9, 1, 0, 66]
for elem in lst:
    if lst.count(elem) == 1:
        print(elem)

"""второй вариант"""
for i in range(len(lst)):
    if lst[i] not in lst[i+1:] and lst[i] not in lst[:i]:
        print(lst[i])
#
# task6. 6) Дан текст, который содержит различные английские буквы и знаки препинания.
# Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a".
# Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите.
# Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
#
text = "This is great text! With some,.:; and other ?-/."
text_example = "abcdefghijklmnopqrstuvwxyz"  # текст для сравнения и отделения знаков препинания
s = ""
# получаем строку из одних только букв
for i in text.lower():
    if i in text_example:
        s = s + i
a = s[0]  # искомая буква
counter = 0
for ind in range(len(s)):
    if s.count(s[ind]) >= counter:
        a = s[ind]
        counter = s.count(s[ind])
        if s.count(s[ind]) == s.count(s[ind - 1]) == counter and ord(s[ind-1]) < ord(s[ind]):
            a = s[ind-1]
print(f"Letter {a} appears {counter} times")




