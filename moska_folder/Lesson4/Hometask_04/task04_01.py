# 1) Перевести строку в список. Пример — "Robin Singh" => ["Robin”, “Singh"] —-
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

a = str(input("Input string\n"))
print(list(a.split(' ')))