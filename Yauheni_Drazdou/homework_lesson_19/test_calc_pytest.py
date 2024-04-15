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



def test_addition(test_init):
    calc = test_init
    result = calc.calc(5, 3, "+")
    assert result == 8

def test_standart_subtraction(test_init):
    calc = test_init
    result = calc.calc(15, 2, "-")
    assert result == 13

def test_negative_subtraction(test_init):
    calc = test_init
    result = calc.calc(0, 2, "-")
    assert result == -2

def test_multipication(test_init):
    calc = test_init
    result = calc.calc(10, 2, "*")
    assert result == 20

def test_division(test_init):
    calc = test_init
    result = calc.calc(10, 2, "/")
    assert result == 5

def test_divide_by_zero(test_init):
    with pytest.raises(ZeroDivisionError):
        calc = test_init
        calc.calc(5, 0, "/")

def test_float_input(test_init):
    with pytest.raises(TypeError):
        calc = test_init
        calc.calc(3.4, 6.2, "+")

def test_invalid_input_operation(test_init):
    calc = test_init
    result = calc.calc(3, 6, "&")
    assert result == "Error"


def test_invalid_input1(test_init):
    with pytest.raises(TypeError):
        test_init("a", 6, "+")

def test_int_result(test_init):
        calc = Calc()
        result = calc.calc(5, 3, "+")
        assert isinstance(result, int)

def test_invalid_input2(test_init):
    with pytest.raises(TypeError):
        test_init((6, 6), 4, "+")