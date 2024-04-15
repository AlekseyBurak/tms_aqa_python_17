def calc(a: int, b: int):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return "Error"


def test_1():
    if calc(3 , 4) == 7:
        print("OK")
    else:
        print("No OK")


def test_2():
    if calc(3.0 , 4) == "Error":
        print("OK")
    else:
        print("No OK")

def test_3():
    if calc(-4 , "5") == "Error":
        print("OK")
    else:
        print("No OK")

def test_4():
    if calc(-4 , (1, 2)) == "Error":
        print("OK")
    else:
        print("No OK")


test_1()
test_2()
test_3()
test_4()


