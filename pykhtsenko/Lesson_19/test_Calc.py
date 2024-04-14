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

@pytest.fixture
def calculator():
    return Calc()

@pytest.mark.smoke
def test_addition(calculator):
    assert calculator.calc(2, 3, "+") == 5

def test_addition_negative(calculator):
    assert calculator.calc(2, 3, "+") == 10

def test_large_numbers_addition(calculator):
    assert calculator.calc(8888888888889, 1, "+") == 888888888890

def test_invalid_operand_types(calculator):
    with pytest.raises(TypeError):
        calculator.calc("15", 5, "+")
@pytest.mark.smoke
def test_subtraction(calculator):
    assert calculator.calc(5, 3, "-") == 2

def test_subtraction_negative(calculator):
    assert calculator.calc(5, 0, "-") == 2
@pytest.mark.smoke
def test_multiplication(calculator):
    assert calculator.calc(2, 3, "*") == 6

def test_multiplication_negative(calculator):
    assert calculator.calc(2, 3, "*") == 8

def test_operation_with_zero(calculator):
    assert calculator.calc(0, 8, "*") == 0
@pytest.mark.smoke
def test_division(calculator):
    assert calculator.calc(6, 3, "/") == 2

def test_division(calculator):
    assert calculator.calc(6, 8, "/") == 5

def test_division_float_result(calculator):
    assert calculator.calc(8, 3, "/") == 2.666666667

def test_division_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.calc(125, 0, "/")
@pytest.mark.skip
def test_error_message(calculator):
    assert calculator.calc(2, 3, "%") == "Error"

def test_multiplication_negative_numbers(calculator):
    assert calculator.calc(-2, 8, "*") == -16

def test_invalid_operation_type(calculator):
    assert calculator.calc(2, 3, "++") == "Error"

def test_invalid_operands(calculator):
    with pytest.raises(TypeError):
        calculator.calc(25.5, 10.5, "+")


