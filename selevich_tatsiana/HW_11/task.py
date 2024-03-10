FILE_NAME = "test.txt"
RESULT = "Я не буду лгать"


def write_to_file(count: int) -> None:
    """
    This function writes a string to a file n-number of times.
    :param count: number of string repetitions
    """
    with open(FILE_NAME, "w") as file:
        for i in range(count):
            file.write(f"{RESULT}\n")


write_to_file(13)
