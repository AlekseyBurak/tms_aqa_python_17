import math
# ASCII symbol into number and task 6
print("Gimme a ACSII symbol")
s = str(input())
t = ord(s)
print(f"Here is the number that matches {s}\n {t}\n А вот результат "
      f"деления корня на длину числа\n {math.sqrt(t)/len(str(t))}")
