# task 1
print("Task 1")
s = str(input("Give me a string of symbols: "))

def f2(s1: str):
    s2 = ""
    x = 1
    for i in range(len(s1)):
        if i == len(s1)-1:
            s2 = s2 + s1[i] + str(x)
        elif s1[i] == s1[i+1]:
            x += 1
        elif x > 1:
            s2 = s2 + s1[i] + str(x)
            x = 1
        else:
            s2 = s2 + s1[i]
            x = 1
    print("I've counted repeating symbols:", s2)


f2(s)

# task 2
# print("\nTask 2")