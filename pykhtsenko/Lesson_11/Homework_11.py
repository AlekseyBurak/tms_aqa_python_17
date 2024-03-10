def write_to_file(file_name, phrase, count):
    with open(file_name, 'w') as file:
        for _ in range(count):
            file.write(phrase + '\n')

write_to_file('text.txt', 'Я не буду лгать!!!', 25)