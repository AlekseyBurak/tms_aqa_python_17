



# for index in range(10):
#     my_file.write(f"{index} -- I am valuable text \n")


with open("test.log", "r") as f:
    for i in f:
        print(i)


def write(file_path, phrase, counts):
    try:
        with open(file_path, 'w') as file:
            for _ in range(counts):
                file.write(phrase + '\n')
        print(f"Фраза {phrase} записана в {file_path} – {counts} раз")

    except Exception as e:
        print(f"Ошибка {e}")


file_path = "homework.txt"
phrase = "Я не буду лгать"
counts = 10

write(file_path, phrase, counts)