def punishment(amount: int):
    """

    :param amount: number of records
    :return: file with records
    """
    with open("Harry_Potter.txt", "a") as f:
        for i in range(amount):
            f.write(f"{i+1}. I must not tell lies\n")


punishment(7)
