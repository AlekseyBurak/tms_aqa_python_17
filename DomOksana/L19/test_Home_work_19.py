import pytest

class TestPytestCalc:
    def test1_pytest_add(self, calc_init):
        result = calc_init.calc(1, 2, "+")
        assert result == 3
        assert isinstance(result, int)
        assert result in (1, 2, 3)

    def test2_pytest_minus(self, calc_init):
        result = calc_init.calc(1, 2, "-")
        assert result == -3
        assert isinstance(result, int)
        assert result not in (2, 3, 4)

    def test3_pytest_mult(self, calc_init):
        result = calc_init.calc(2, 3, "*")
        assert result == 6
        assert isinstance(result, int)

    def test4_pytest_div(self, calc_init):
        result = calc_init.calc(6, 2, "/")
        assert result == 3
        assert isinstance(result, float)

    def test5_pytest_invalid(self, calc_init):
        result = calc_init.calc(3, 6, "&")
        assert result == "Error"

    def test6_pytest_div_0(self, calc_init):
        with pytest.raises(ZeroDivisionError):
            calc_init.calc(1, 0, "/")

    def test7_pytest_tip(self, calc_init):
        with pytest.raises(TypeError):
            calc_init(1.0, 0.2, "+")

    def test8_pytest_tip2(self, calc_init):
        with pytest.raises(TypeError):
            calc_init("a", 6, "+")
