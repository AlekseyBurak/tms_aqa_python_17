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


@pytest.fixture(autouse=True)
def calc_init():
    calc = Calc()
    yield calc


class TestPytestCalc:

    def test_sum(self, calc_init):
        calc = calc_init
        result = calc.calc(4,2, "+")
        assert result == 6

    def test_sum_greater(self, calc_init):
        calc = calc_init
        result = calc.calc(6, 2, "+")
        assert result >= 7

    def test_sum_negative(self, calc_init):
        calc = calc_init
        result = calc.calc(1, 2, "11211")
        assert result == "Error"

    def test_subtraction(self,calc_init):
        calc = calc_init
        result = calc.calc(0, 12, "-")
        assert result == -12

    def test_multiply(self, calc_init):
        calc = calc_init
        result = calc.calc(9, 2, "*")
        assert result == 18

    def test_divide(self, calc_init):
        calc = calc_init
        result = calc.calc(9, 9, "/")
        assert result == 1

    def test_divide_0(self, calc_init):
        calc = calc_init
        with pytest.raises(ZeroDivisionError):
            result = calc.calc(9, 0, "/")

    def test_odject_double(self,calc_init):
        calc = calc_init
        result = calc.calc(8.0, 9, "*")
        assert result == "Error"

    def test_invalid_object(self,calc_init):
        calc = calc_init
        with pytest.raises(NameError):
            result = calc.calc(lalala, 9, "-")

    def test_no_operation(self, calc_init):
        calc = calc_init
        with pytest.raises(TypeError):
            result = calc.calc(8.0, 9)