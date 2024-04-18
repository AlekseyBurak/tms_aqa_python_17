import pytest
@pytest.fixture
def calculator():
    return DesignCalculator()

@pytest.fixture
def olive_wall_colour():
    return "Оливковый"

@pytest.fixture
def dark_wood_flour_colour():
    return "Темный дуб"

@pytest.fixture
def light_wood_flour_colour():
    return "Светлый дуб"

@pytest.fixture
def green_wall_and_floor_colour():
    return "Зеленый"

@pytest.fixture
def invalid_input():
    return 123456