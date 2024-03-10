def open_file():
    with open("hehe.txt", "r") as my_file:
        for line in my_file:
            print(line)


# open_file()

def write_file(n):
    with open("hehe.txt", "w") as my_file:
        for i in range(n):
            my_file.write("I won't lie. \n")


# write_file(5)


def write_new_file(my_file, n):
    try:
        with open(my_file, "x") as my_file:
            for i in range(n):
                my_file.write("I won't lie. \n")
    except FileExistsError:
        print("File already exists.")


# write_new_file("hehe.txt", 6)


def new_row_in_file(n):

    with open("hehe.txt", "a") as my_file:
        for i in range(n):
            my_file.write("I won't lie. \n")


# new_row_in_file(2)
