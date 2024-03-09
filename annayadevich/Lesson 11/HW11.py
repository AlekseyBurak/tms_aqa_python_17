# with open("Harry_Potter_1.txt", "w") as f:
#     for index in range(3):
#         f.write(f"{index} -- I won't lie. \n")


def write_to_file(phrase, repeat):
    with open("Harry_Potter_1.txt", "w") as file:
        for _ in range(repeat):
            file.write(phrase + "\n")


write_to_file("I won't lie.", 3)
