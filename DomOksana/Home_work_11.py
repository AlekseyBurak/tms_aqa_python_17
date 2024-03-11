def write_phrase_to_file(raz):
    with open('output.txt', 'w') as file:
        for _ in range(raz):
            file.write("Я не буду лгать\n")

write_phrase_to_file(5)