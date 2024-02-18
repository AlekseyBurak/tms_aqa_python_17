import random

list_people = [f"Human{index}" for index in range(1, 11)]
list_age = [random.randint(18, 45) for _ in range(10)]


zip_obj = zip(list_people, list_age)
print(zip_obj)

print(list(zip_obj))
dict_from_zip = {}

for key, value in zip_obj:
    dict_from_zip[key] = value

print()
print(dict_from_zip)