
def write_text(count: int):
    with open("HP.txt", "w") as f:
        for i in range(1, count+1):
            f.write(f"{i} -- I must not tell lies. \n")


write_text(10)

with open("HP.txt", "r") as f:
    for line in f:
        print(line)

