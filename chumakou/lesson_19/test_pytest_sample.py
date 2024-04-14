import pytest


class Calc:

    def concatinate(self, a: int, b: int):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Error"


class TestPytestCalc:

    def test_pytest_calc_1(self):
        calc = Calc()
        result = calc.concatinate(4, 2)
        assert result == 6
        assert isinstance(result, int)
        assert calc.concatinate(4, 2) == 6


#python -m pytest .\burak_folder\lesson_19\test_pytest_sample.py::TestPytestCalc::test_pytest_calc_1
#python -m pytest .\chumakou\lesson_19\test_pytest_sample.py::TestPytestCalc::test_pytest_calc_1