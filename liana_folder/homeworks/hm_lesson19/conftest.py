import pytest
from test_hm_lesson19_task_1 import Calc


@pytest.fixture(autouse=True)
def calculator_init():
    calculator = Calc()
    return calculator
