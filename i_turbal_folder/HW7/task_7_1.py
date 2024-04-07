alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
alphabet += 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()


def encode(text: str, x: int):
    new_str = ""
    for i in text:
        position = alphabet.find(i)
        new_position = position + x
        if i.isalpha():
            new_str += alphabet[new_position]
        else:
            new_str += i
    return new_str

def decode(text: str, x: int):
    new_str = ''
    for i in text:
        position = alphabet.find(i)
        new_position = position - x
        if i.isalpha():
            new_str += alphabet[new_position]
        else:
            new_str += i
    return new_str

print( """ 
    1. Encode 
    2. Decode
    3. Exit
    """)

while True:
    choose = input("Enter option: ")
    if choose == '3':
        break
    if choose not in '123':
        print("please choose correct option")
        continue
    text = input("Enter text: ").lower()
    x = (input("Enter step"))
    if x.isalpha():
        print("Please enter number")
    if choose == '1':
        x = int(x)
        print(encode(text, x))
    if choose == '2':
        x = int(x)
        print(decode(text,x))
