import pytest


class Calc:
    @staticmethod
    def calc(a: int, b: int, operation: str):
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
def calc_1():
    print("\nHello")
    calculator = Calc()
    yield calculator
    print("\ndone")


class TestPytestCalc:

    def test_addition(self):
        calculator = Calc()
        assert calculator.calc(2, 3, "+") == 5

    def test_addition_with_negative_numbers(self):
        calculator = Calc()
        assert calculator.calc(-2, -5, "+") == - 7

    def test_subtraction(self):
        calculator = Calc()
        assert calculator.calc(5, 2, "-") == 3

    def test_subtraction_with_negative_numbers(self):
        calculator = Calc()
        assert calculator.calc(- 5, 2, "-") == - 7

    def test_multiplication(self):
        calculator = Calc()
        assert calculator.calc(5, 2, "*") == 10

    def test_multiplication_with_negative_numbers(self):
        calculator = Calc()
        assert calculator.calc(- 5, 2, "*") == - 10

    def test_division(self):
        calculator = Calc()
        assert calculator.calc(10, 2, "/") == 5

    def test_non_existent_operation(self):
        calculator = Calc()
        assert calculator.calc(10, 2, "^") == "Error"

    def test_operand_not_str(self):
        calculator = Calc()
        assert calculator.calc(10, 2, 3) == "Error"

    def test_number_str(self):
        calculator = Calc()
        with pytest.raises(TypeError):
            calculator.calc(10, "2", "+")

    def test_division_by_zero(self):
        calculator = Calc()
        with pytest.raises(ZeroDivisionError):
            calculator.calc(5, 0, '/')

    @pytest.mark.xfail
    def test_division_1(self):
        calculator = Calc()
        assert calculator.calc(10, 3, "/") == 3
    #
    @pytest.mark.skip("accepts only int")
    def test_number1_float(self):
        calculator = Calc()
        with pytest.raises(TypeError):
            calculator.calc(7.2, 6.5, "+")
