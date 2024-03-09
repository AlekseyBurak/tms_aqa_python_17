def write_to_file(file_name, phrase, times):
    with open(file_name, 'w') as file:
        for _ in range(times):
            file.write(phrase + '\n')

write_to_file('output.txt', 'Я не буду лгать', 5)