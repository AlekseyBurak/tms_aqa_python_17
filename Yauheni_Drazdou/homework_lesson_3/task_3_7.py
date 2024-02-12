# task 7 how many thousand hundreds tens etc
print("Gimme four digit number")
s = int(input())
a = s // 1000
b = (s - a * 1000) // 100
c = (s - a * 1000 - b * 100) //10
d = (s - a * 1000 - b * 100 - c * 10)
print(f"Digit consists:\n{a} thousads\n"
      f"{b} hundreds\n{c} tens\n{d} singles")