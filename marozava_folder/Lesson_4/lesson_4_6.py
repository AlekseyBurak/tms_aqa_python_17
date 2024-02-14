# Дан текст, который содержит различные английские буквы
# и знаки препинания. Вам необходимо найти самую частую букву в тексте.
# Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения,
# так что при подсчете считайте, что "A" == "a". Убедитесь,
# что вы не считайте знаки препинания, цифры и пробелы, а только буквы.

# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква,
# которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
# !!! Задача для меня очень была сложная, делала ее с помощью и объяснением.

import string

text = "eValentine's Day (or Saint Valentine's Day) is a holiday that, in the United States, takes place on February 14e"
letters = dict()
for l in text:
    l = l.lower()
    if l in string.ascii_letters:
        if l in letters:
            value = letters.get(l) + 1
            letters[l] = value
        else:
            letters[l] = 1
print(letters)
max_value = 0
max_value_letter = None
for l in letters:
    if letters.get(l) > max_value or letters.get(l) == max_value and l < max_value_letter:
        max_value_letter = l
        max_value = letters.get(l)

print(f'{max_value} {max_value_letter}')



