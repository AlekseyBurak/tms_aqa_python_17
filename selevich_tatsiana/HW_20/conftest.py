import pytest
from test_task import DesignCalculator

@pytest.fixture(autouse=True)
def calc_init():
    print("\nStart test-case")
    calc = DesignCalculator()
    return calc


@pytest.fixture(scope="module", autouse=True)
def calc_module_init():
    print("\nStart test module")
    yield
    print("\nEnd test module")
