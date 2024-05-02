import pytest
from test_app_for_param import DesignCalculator


@pytest.fixture
def calculator():
    return DesignCalculator()
