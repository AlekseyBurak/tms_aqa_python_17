import pytest
from test_hm_20 import DesignCalculator


@pytest.fixture(autouse=True)
def start_test_1():
    print("\nStart testing")
    calc = DesignCalculator()
    return calc


@pytest.fixture(scope="class", autouse=True)
def class_scope_1():
    print("\nClass setup")
    yield
    print("\nClass teardown")


@pytest.fixture(scope="module", autouse=True)
def module_scope_1():
    print("\nModule setup")
    yield
    print("\nModule teardown")
