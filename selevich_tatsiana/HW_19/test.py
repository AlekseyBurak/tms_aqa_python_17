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


class TestAddition:

    def test_addition_return_type(self, calc_init):
        result = calc_init.calc(3, 4, "+")
        assert isinstance(result, int)

    def test_addition_positive_numbers(self, calc_init):
        assert calc_init.calc(3, 4, "+") == 7

    def test_addition_negative_numbers(self, calc_init):
        assert calc_init.calc(-3, -4, "+") == -7

    def test_addition_large_numbers(self, calc_init):
        assert calc_init.calc(1234567890, 1234567890, "+") == 2469135780

    @pytest.mark.xfail(reason="Expected fail")
    def test_addition_fractional_input_type(self, calc_init):
        result = calc_init.calc(3.5, 4, "+")
        assert isinstance(result, int)

    def test_addition_string_input_type(self, calc_init):
        with pytest.raises(TypeError):
            calc_init.calc("av", 4, "+")


class TestSubtraction:

    def test_subtraction_return_type(self, calc_init):
        result = calc_init.calc(3, 4, "-")
        assert isinstance(result, int)

    def test_subtraction_positive_numbers(self, calc_init):
        assert calc_init.calc(3, 4, "-") == -1

    def test_subtraction_negative_numbers(self, calc_init):
        assert calc_init.calc(-3, -4, "-") == 1

    def test_subtraction_large_numbers(self, calc_init):
        assert calc_init.calc(1234567890, 1234567890, "-") == 0

    @pytest.mark.xfail(reason="Expected fail")
    def test_subtraction_fractional_input_type(self, calc_init):
        result = calc_init.calc(3, 4.5, "-")
        assert isinstance(result, int)

    def test_subtraction_none_input_type(self, calc_init):
        with pytest.raises(TypeError):
            calc_init.calc(4, None, "-")


class TestMultiplication:

    def test_multiplication_return_type(self, calc_init):
        result = calc_init.calc(3, 4, "*")
        assert isinstance(result, int)

    def test_multiplication_positive_numbers(self, calc_init):
        assert calc_init.calc(3, 4, "*") == 12

    def test_multiplication_negative_numbers(self, calc_init):
        assert calc_init.calc(-3, 4, "*") == -12

    def test_multiplication_large_numbers(self, calc_init):
        assert calc_init.calc(1234567890, 1234567890, "*") == 1524157875019052100

    @pytest.mark.xfail(reason="Expected fail")
    def test_multiplication_fractional_input_type(self, calc_init):
        result = calc_init.calc(3.5, 4, "*")
        assert isinstance(result, int)

    @pytest.mark.xfail(reason="Expected fail")
    def test_multiplication_string_input_type(self, calc_init):
        result = calc_init.calc("&!$/\\^*(", 4, "*")
        assert isinstance(result, int)


class TestDivision:

    def test_division_positive_numbers(self, calc_init):
        assert calc_init.calc(10, 5, "/") == 2

    def test_division_negative_numbers(self, calc_init):
        assert calc_init.calc(-5, 5, "/") == -1

    def test_division_large_numbers(self, calc_init):
        assert calc_init.calc(1234567890, 1234567890, "/") == 1

    def test_division_by_zero(self, calc_init):
        with pytest.raises(ZeroDivisionError):
            calc_init.calc(20, 0, "/")

    def test_division_string_input_type(self, calc_init):
        with pytest.raises(TypeError):
            calc_init.calc("av", 4, "/")


class TestAdditionalCase:

    def test_arguments_number(self, calc_init):
        with pytest.raises(TypeError):
            calc_init.calc(3, 4, "/", 7)

    def test_invalid_operation(self, calc_init):
        assert calc_init.calc(3, 4, "^") == "Error"
