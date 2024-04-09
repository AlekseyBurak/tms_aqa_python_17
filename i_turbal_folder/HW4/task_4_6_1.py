#Дан текст, который содержит различные английские буквы и знаки препинания.
# Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
#При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте,
# что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
#Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква,
# которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".

import re

yourText = input("Enter your string: ").lower() # Сразу приводим к одному регистрау
counterOfLetters = {} # словаь буквы и количество ее повторения
if re.search("[а-яА-Я]", yourText):
    print("Please enter Latin")
else:
    yourText = re.sub(r"\W", "", yourText) # удаляем знаки и пробелы
    yourText = re.sub(r"\d", "", yourText) # удаляем цифры
    for letter in yourText:
        if letter in counterOfLetters:
            counterOfLetters[letter] += 1
        else:
            counterOfLetters[letter] = 1

print(counterOfLetters)
mostPopularLetter = sorted(counterOfLetters.items(), key= lambda x: (-x[1], x[0]))[0][0]
print(f"Letter {mostPopularLetter} was repeated {counterOfLetters[mostPopularLetter]}")




