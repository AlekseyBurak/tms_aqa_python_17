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
def test_init():
    print("\nTest result:")
    calc = Calc()
    yield calc

@pytest.fixture(scope="module", autouse=True)
def calc_init():
    print("\nHi, lets test the calc")
    yield
    print("\nTest is done")