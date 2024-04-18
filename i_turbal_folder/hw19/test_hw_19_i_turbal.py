import unittest
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


@pytest.fixture()
def calc():
    yield Calc()


@pytest.mark.addition
class TestOperationPlus:

    @pytest.mark.smoke
    def test_int(self, calc):
        result = calc.calc(1,2,'+')
        assert result == 3
        assert isinstance(result, int)

    @pytest.mark.xfail
    def test_float(self, calc):
        with pytest.raises(TypeError):
            result = calc.calc(1, 2.0, '+')

    def test_str(self, calc):
        with pytest.raises(TypeError):
            result = calc.calc(1, '2', '+')


@pytest.mark.subtraction
class TestOperationMinus:

    @pytest.mark.smoke
    def test_int(self, calc):
        result = calc.calc(1,2,'-')
        assert result == -1
        assert isinstance(result, int)

    @pytest.mark.xfail
    def test_float(self, calc):
        with pytest.raises(TypeError):
            result = calc.calc(1, 2.0, '-')

    def test_str(self, calc):
        with pytest.raises(TypeError):
            result = calc.calc(1, '2', '+')

@pytest.mark.division
class TestOperationDivision:

    @pytest.mark.smoke
    def test_devision_with_remainder(self, calc):
        assert isinstance(calc.calc(3, 2, '/'), float)

    def test_devision_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.calc(1, 0, '/')

@pytest.mark.multiplication
class TestOperationMltiplication:

    def test_multiplication_int(self, calc):
        assert calc.calc(1, 0 , '*') == 0



class TestNotExistedOperation:

    def test_not_existed_operation(self, calc):
        assert calc.calc(1, 2, '%') == 'Error'





