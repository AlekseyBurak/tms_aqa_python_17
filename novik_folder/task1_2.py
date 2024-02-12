x = int(input("Enter your number \n"))
y = int(input("Enter your number \n"))
x_mod = abs(x)
y_mod = abs(y)
x_y_mod = abs(x*y)

result = (x_mod - y_mod) / (1 + x_y_mod)

print(f'Your multiply result is {result}')