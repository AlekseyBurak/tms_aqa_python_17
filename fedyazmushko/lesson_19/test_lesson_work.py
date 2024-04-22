import pytest


class Calc:

    def concatinate(self, a: int , b: int):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Error"



class TestPytestCalc:

    def test_pytest_calc_1(self, calc_init):
        calc = calc_init
        result = calc.concatinate(4, 2)
        assert result == 6



    def test_data_in_sql(self):
        assert True


    def test_data_in_postressql(self):
        assert True

    def test_data_in_mongo(self):
        assert True


    @pytest.mark.xfail
    def test_ios2(self):
        assert True

    @pytest.mark.e2e
    def test_e2e(self):
        assert True


    @pytest.mark.parametrize("login, password", )
    def test_skip(self, login, password):
        login = "Fzmushko"
        password = "12345"
        assert login == "Fzmushko"
        assert password == "12345"






