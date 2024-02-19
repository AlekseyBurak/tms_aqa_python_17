import datetime
import random
import time
# делаем список из цифр
# list_integer = [i for i in range(1,11)]
# print(list_integer)
#
# print(list(range(5,51,5)))

# делаем список из строк
# list_integer = [str(i) for i in range(1,11)]
# print(list_integer)
#
#
# list_integer = [i for i in range(1,11)]
# list_string = map (str, list_integer)
# print(type(list_string))

list_people = [f"Human{index}" for index in range(1, 11)]
list_age = [random.randint(18, 45) for _ in range(10)]


zip_obj = zip(list_people, list_age)
print(zip_obj)

print(list(zip_obj))

dict_from_zip = {}

for key, value in list (zip_obj):
    dict_from_zip[key] = value
print()
print(dict_from_zip)
dict_from_zip.update (zip_obj)
print(dict_from_zip)
# hfyljv
import random

from datetime import datetime


print(random.randint(1, 2))
print(datetime.now())



