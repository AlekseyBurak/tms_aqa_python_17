print('Введите, пожалуйста, ваши значения')

x = int(input())
y = int(input())

task = (abs(x) - abs(y)) / (1 + abs(x*y))

print('Как-то так :', task)