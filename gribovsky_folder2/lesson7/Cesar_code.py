def encode(message: str, sdvig: int):
    encoding_string = ""
    for letters in message:
        encoding_string += chr(ord(letters) + sdvig)
    print(f" зашифрованная строка = {encoding_string}")


def decode(enc_message: str, sdvig: int):
    decoding_string = ""
    for i in enc_message:
        decoding_string += chr(ord(i) - sdvig)
    print(f" дешифрованная строка = {decoding_string}")


encode("this is a test string", 5)
decode("ymnx%nx%f%yjxy%xywnsl", 5)
