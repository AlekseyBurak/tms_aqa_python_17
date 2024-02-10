# Ввод одиночных символов (латиница)
import re

string = input("Введите только латинскую букву:  ")
pattern = r"[A-Za-z]"
result = re.compile(pattern)
if result.fullmatch(string):
    print(ord(string))
else:
    print("Ошибка!!!")