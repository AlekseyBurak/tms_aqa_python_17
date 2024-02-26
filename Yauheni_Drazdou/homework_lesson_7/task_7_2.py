#задача про рост Пети

print("How many students are in a class?")
how_many_st = int(input())
a = []

print("How tall is each student?")
for i in range(how_many_st):
    rost = int(input())
    a.append(rost)
print(a)

print("How tall is Petya?")
petya = int(input())

#составляем список учеников, которые ниже Пети
c = []
for i in a:
    if i < petya:
        c.append(i)

print(f"Petya is number {(len(a) - len(c)) + 1} on the list")
