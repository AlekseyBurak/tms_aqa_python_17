import pytest
from test_hw_less_20 import DecorTasteError, DesignCalculator


@pytest.fixture(scope="class", autouse=True)
def class_end_init():
    yield
    print("\nTests are done")

@pytest.fixture(scope="function", autouse=True)
def func_init():
    print("\nTest above is")
    yield
