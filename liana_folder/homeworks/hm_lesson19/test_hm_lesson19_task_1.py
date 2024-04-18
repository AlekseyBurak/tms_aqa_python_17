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


class TestPytestCalc:

    @pytest.mark.smoke
    def test_operation_addition(self, calculator_init):
        assert calculator_init.calc(4, 2, "+") == 6

    @pytest.mark.smoke
    def test_operation_subtraction(self, calculator_init):
        assert calculator_init.calc(4, 2, "-") == 2

    @pytest.mark.smoke
    def test_operation_multiplication(self, calculator_init):
        assert calculator_init.calc(4, 2, "*") == 8

    @pytest.mark.smoke
    def test_operation_division(self, calculator_init):
        assert calculator_init.calc(4, 2, "/") == 2

    @pytest.mark.critical_pass
    def test_addition_1(self, calculator_init):
        assert calculator_init.calc(4, -10, "+") == -6

    @pytest.mark.critical_pass
    def test_addition_2(self, calculator_init):
        assert calculator_init.calc(-4, -10, "+") == -14

    @pytest.mark.critical_pass
    def test_addition_3(self, calculator_init):
        assert calculator_init.calc(10, 0, "+") == 10

    @pytest.mark.critical_pass
    def test_subtraction_1(self, calculator_init):
        assert calculator_init.calc(-10, 1, "-") == -11
    @pytest.mark.critical_pass
    def test_subtraction_2(self, calculator_init):
        assert calculator_init.calc(10, -1, "-") == 11

    @pytest.mark.critical_pass
    def test_subtraction_3(self, calculator_init):
        assert calculator_init.calc(-10, -1, "-") == -9

    @pytest.mark.critical_pass
    def test_subtraction_4(self, calculator_init):
        assert calculator_init.calc(0, -1, "-") == 1

    @pytest.mark.critical_pass
    def test_multiplication_1(self, calculator_init):
        assert calculator_init.calc(-2, 3, "*") == -6

    @pytest.mark.critical_pass
    def test_multiplication_2(self, calculator_init):
        assert calculator_init.calc(2, -3, "*") == -6

    @pytest.mark.critical_pass
    def test_multiplication_3(self, calculator_init):
        assert calculator_init.calc(-2, -3, "*") == 6

    @pytest.mark.critical_pass
    def test_multiplication_4(self, calculator_init):
        assert calculator_init.calc(2, 0, "*") == 0

    @pytest.mark.critical_pass
    def test_division_1(self, calculator_init):
        with pytest.raises(ZeroDivisionError):
            assert calculator_init.calc(2, 0, "/")

    @pytest.mark.critical_pass
    def test_division_2(self, calculator_init):
        assert calculator_init.calc(11, 2, "/") == 5.5

    @pytest.mark.critical_pass
    def test_division_3(self, calculator_init):
        assert calculator_init.calc(11, 5, " ") == "Error"

    @pytest.mark.critical_pass
    def test_division_3(self, calculator_init):
        assert calculator_init.calc(11, 5, "?") == "Error"

    @pytest.mark.critical_pass
    def test_division_3(self, calculator_init):
        assert calculator_init.calc(11, 5, "++") == "Error"

    @pytest.mark.critical_pass
    def test_operand_a_str(self, calculator_init):
        with pytest.raises(TypeError):
            assert calculator_init.calc("2", 0, "+")

    @pytest.mark.critical_pass
    def test_operand_b_str(self, calculator_init):
        with pytest.raises(TypeError):
            assert calculator_init.calc(2, "0", "+")

    @pytest.mark.critical_pass
    def test_operand_a_float(self, calculator_init):
        with pytest.raises(TypeError):
            assert calculator_init.calc(1.0, 2, "+")

    @pytest.mark.critical_pass
    def test_operand_b_float(self, calculator_init):
        with pytest.raises(TypeError):
            assert calculator_init.calc(2, 1.0, "/")






