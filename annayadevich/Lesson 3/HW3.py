# task 1 - замена части строки
string = "www.my_site.com#about"
print(string.replace("#", "/"))

# task 2
a = input("enter the verb: ")
ing_form = a + "ing"
print(f"verb = ing '{a}' - это '{ing_form}'.")

# task 3 - удаление пробелов в начале и конце строки
text = "   Knowledge is power   "
new_text = text.strip()
print(new_text)

# task 4
def my_function():
     return chr(int(input("Enter a number from 0 to 255: ")))
print(f"the character corresponding to the entered number: {my_function()}")

# task 7
num = int(input("введите четырехзначное число: "))
digit1 = num // 1000
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
print(f"единицы {digit4}, десятки {digit3}, сотни {digit2}, тысячи {digit1}")