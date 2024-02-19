import datetime
import random
#
list_integer = (i for i in range(1, 11))
# # print()
# # print(list(range(10)))
#
# # list_strings = map(str, list_integer)
# # list_integer = (str(i) for i in range(1, 11))
#
# list_people = [f"Human{index}" for index in range(1, 11)]
# list_age = [random.randint(18, 45) for _ in range(10)]
#
#
# zip_obj = zip(list_people, list_age)
# print(zip_obj)
#
# print(list(zip_obj))
# dict_from_zip = {}
# for key, value in zip_obj:
#     dict_from_zip[key] = value
#     print(dict_from_zip)

list_integers = [random.randint(1, 99) for _ in range(10)]

print(list_integers)
print(max(list_integers))
print(min(list_integers))
print(sorted(list_integers))
print(list_integers)
