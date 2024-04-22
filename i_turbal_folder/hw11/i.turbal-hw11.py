def write_text(count):
    with open('file1.txt', 'w') as file:
        for i in range(count):
            file.write("I think Harry Potter is overrated, please don't hate me\n")

write_text(15)
