import unittest
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
    print("\nHe He i'm done")


@pytest.fixture(autouse=True)
def connect_to_sql():
    print("\nConnecting to SQL")
    yield
    print("\nDisconnecting to Base")


@pytest.fixture(scope="class", autouse=True)
def class_scope():
    print("\nClass setup")
    yield
    print("\nClass teardown")


class TestPytestCalc:

    def test_pytest_calc_1(self, calc_init):
        calc = calc_init
        result = calc.concatinate(4, 2)
        assert result == 7
        assert isinstance(result, int)
        assert calc.concatinate(4, 2) == 6


    def test_data_in_sql(self):
       assert True

    def test_data_in_postsql(self):
       assert True

    def test_data_in_postttl(self):
       assert False
