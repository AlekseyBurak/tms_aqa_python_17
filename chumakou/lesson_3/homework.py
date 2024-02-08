# <-- 1 задание -->
website = "www.my_site.com#about"
print(website.replace("#", "/"))

# <-- 2 задание -->
text_adding = "Alex"
print(text_adding + " ing")


# <-- 3 задание -->
string = "    Тут пробел вначале и тут в конце     "
print(f"Без пробелов – {string.strip()}")
print(f"С пробелами – {string}")


# <-- 3 задание (через функцию) -->
def delete_spaces(string):
    cleaned_string = string.strip()
    return cleaned_string

my_text = "    Тут пробел вначале и тут в конце     "
result = delete_spaces(my_text)

print("Исходная строка:", my_text)
print("Строка без пробелов:", result)


# <-- 4 задание -->
number = int(input("Введите число от 0 до 255: "))

if 0 <= number <= 255:
    symbol = chr(number)
    print(f"Символ ASCII для числа {number}: {symbol}")
else:
    print("Введенное число не находится в допустимом диапазоне.")



# <-- 5 задание -->
enter_symbol = input("Введите символ: ")

if len(enter_symbol) == 1 and enter_symbol.isalpha():
    symbol_code = ord(enter_symbol)
    print(f"Код ASCII для символа '{enter_symbol}': {symbol_code}")
else:
    print("Введите только одиночный символ")
