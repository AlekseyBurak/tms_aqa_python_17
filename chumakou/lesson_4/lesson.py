# 1

stroka = "Robin Singh"
print(stroka.split())


# 2

l = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"
print(f"“Привет, {l[0]} {l[1]}! Добро пожаловать в {city} {country}”")


# 3

string_join = ["I", "love", "arrays", "they", "are", "my", "favorite"]
string_join = ' '.join(string_join)
print(string_join)


# 4

elements = [i for i in range(1,11)]
elements.insert(2, "new_element")
print(elements)
delete_element = elements.pop(6)
print(elements)


