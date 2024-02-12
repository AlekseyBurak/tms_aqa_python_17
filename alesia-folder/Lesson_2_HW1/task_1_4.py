#import math
from scipy. stats import gmean
import statistics

d = int(input("Введи число: "))
e = int(input("Введи еще одно число: "))

# print("Среднее арифметическое =", (e + d) / 2,
#       "\nСреднее геометрическое =", math.sqrt(d*e))

print("Среднее арифметическое =", statistics.mean([d, e]),
      "\nСреднее геометрическое =", gmean([d, e]))
