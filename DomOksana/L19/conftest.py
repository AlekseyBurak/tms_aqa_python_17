import pytest

class Calc:
    def calc(self, a: int, b: int, operation: str):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            return "Error"

@pytest.fixture(scope="function")
def calc_init():
    print("\nBegin test calc")
    calc = Calc()
    yield calc
    print("\nFinish test calc")

@pytest.fixture(scope="module", autouse=True)
def test_init():
    print("\nHi modul")
    yield
    print("\nBye modul")