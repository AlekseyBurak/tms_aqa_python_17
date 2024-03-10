# Написать функцию которая будет писать в файл фразу "Я не буду лгать". Писать должна столько сколько нужно
# (сколько попросим в аргументах функции).

def save_to_file(filename, phrase, count):
    with open(filename, 'w') as file:
        for _ in range(count):
            file.write(phrase + '\n')


save_to_file("Harry.txt", "Я не буду лгать!!!", 5)
print(save_to_file())
