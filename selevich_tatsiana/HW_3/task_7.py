number = int(input("Введите четырехзначное число: "))
print(f"Единицы {number % 10}, десятки {number % 100 // 10}, сотни {number // 100 % 10}, тысячи {number // 1000}")
