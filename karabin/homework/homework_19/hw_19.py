import pytest


class Calculator:
    def div(self, a: [int, float], b: [int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both args should be numeric")
        if b == 0:
            raise ZeroDivisionError("Can't divide by zero")
        return a / b

    def add(self, a: [int, float], b: [int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both args should be numeric")
        return a + b

    def dif(self, a: [int, float], b: [int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both args should be numeric")
        return a - b

    def mult(self, a: [int, float], b: [int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both args should be numeric")
        return a * b


@pytest.fixture()
def calc_init():
    print("\nStart")
    calc = Calculator()
    yield calc
    print("\nEnd")


class TestPytestCalc:

    def test_1(self, calc_init):
        calc = calc_init
        assert calc.add(4, 2) == 6

    def test_2(self, calc_init):
        calc = calc_init
        assert calc.dif(4, 2) == 2

    def test_3(self, calc_init):
        calc = calc_init
        assert calc.mult(5, 4) == 20

    def test_4(self, calc_init):
        calc = calc_init
        with pytest.raises(ZeroDivisionError):
            assert calc.div(5, 0)

    def test_5(self, calc_init):
        calc = calc_init
        assert isinstance(calc.dif(4, 3), int)

    def test_6(self, calc_init):
        calc = calc_init
        assert isinstance(calc.dif(4.5, 3), float)

    def test_7(self, calc_init):
        calc = calc_init
        with pytest.raises(TypeError):
            assert calc.mult(3, "f")
