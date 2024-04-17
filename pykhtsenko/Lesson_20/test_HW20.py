
class DecorTasteError(Exception):
    pass
class DesignCalculator:

    def colour_match(self, wall_colour: str, flour_colour: str):
        if not all((isinstance(flour_colour, str), isinstance(wall_colour, str))):
            raise DecorTasteError
        if wall_colour == "Оливковый" and flour_colour == "Темный дуб":
            return "Идеально"
        elif wall_colour != flour_colour:
            return "Ну красиво же"
        else:
            return "Это печально"


import pytest
#@pytest.fixture(scope='function', autouse=True)
def design():
    return DesignCalculator()

@pytest.mark.skip
def test_invalid_input(design):
    assert design.colour_match(wall_colour="12345", flour_colour="333333") == "Идеально"

@pytest.mark.smoke
def test_ideal_colour(design):
    assert design.colour_match(wall_colour="Оливковый", flour_colour="Темный дуб") == "Идеально"

def test_beautiful_colour(design):
    assert design.colour_match(wall_colour="Белый", flour_colour="Коричневый") == "Ну красиво же"

def test_same_colour(design):
    assert design.colour_match(wall_colour="Оливковый", flour_colour="Оливковый") == "Это печально"

def test_beautiful_colour_fail(design):
   # assert design.colour_match(wall_colour="Белый", flour_colour="Коричневый") == "Ну красиво же"

def test_same_colour_fail(design):
    assert design.colour_match(wall_colour="Оливковый", flour_colour="Оливковый") == "Идеально"

@pytest.fixture
def test_without_one_sign(design):
    assert design.colour_match(wall_colour="Оливковы", flour_colour="Темный дуб") == "Идеально"

def test_other_sign(design):
   assert design.colour_match(wall_colour="Оливковый", flour_colour="Темный дуб") == "Класс"


@pytest.mark.parametrize("wall_colour, flour_colour, expected_result", [
    pytest.param("Оливковый", "Темный дуб", "Идеально"),
    pytest.param("Оливковый", "Светлый дуб", "Ну красиво же"),
    pytest.param("Красный", "Красный", "Это печально")
])
def test_param_test(wall_colour, flour_colour,  expected_result):
    assert all((wall_colour == "Оливковый"), (flour_colour == "Темный дуб"), (expected_result == "Идеально"))


