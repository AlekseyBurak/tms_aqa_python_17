import pytest
from test import Calc


@pytest.fixture(autouse=True)
def calc_init():
    print("\nStart test-case")
    calc = Calc()
    return calc


@pytest.fixture(scope="class", autouse=True)
def calc_init2():
    print("\nStart test suit")
    yield
    print("\nEnd test suit")
