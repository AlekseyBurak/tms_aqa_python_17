import pytest
from test_task1 import DesignCalculator


@pytest.fixture(autouse=True)
def colour():
    return DesignCalculator()
