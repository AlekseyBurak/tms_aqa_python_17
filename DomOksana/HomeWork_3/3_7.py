n = int(input("введите четырехзначное число: "))
print(f"единицы: {n % 10}")
print(f"десятки: {n % 100 // 10}")
print(f"десятки ещё раз: {n // 10 % 10}")
print(f"сотни: {n // 100 % 10}")
print(f"сотни ещё раз: {n % 1000 // 100}")
print(f"тысячи: {n // 1000 % 100}")
print(f"тысячи ещё раз: {n % 10000 // 1000}")
print(f"десятки тысяч: {n % 100000 // 10000}")