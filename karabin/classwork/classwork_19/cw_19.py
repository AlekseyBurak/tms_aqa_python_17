import pytest


class Calc:

    def concatinate(self, a: int, b: int):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Error"


@pytest.fixture()
def calc_init():
    print("\nHello from pytest")
    calc = Calc()
    yield calc
    print("\nHe he i'm done")


@pytest.fixture(autouse=True)
def connect_to_sql():
    print("\nConnecting to SQL Data Base")
    yield
    print("\nDisConnecting from SQL Data Base")


@pytest.fixture(scope="class", autouse=True)
def class_scope():
    print("\nClass setup")
    yield
    print("\nClass teardown")


class TestPytestCalc:

    def test_pytest_calc_1(self, calc_init):
        calc = calc_init
        result = calc.concatinate(4, 2)
        assert result == 6
        assert isinstance(result, int)
        assert calc.concatinate(4, 2) == 6

    # def test_data_in_sql(self):
    #     assert True
    #
    # def test_data_in_postgressql(self):
    #     assert True
    #
    # def test_data_in_mongo(self):
    #     assert True
