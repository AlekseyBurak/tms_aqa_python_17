import pytest


class DecorTasteError(Exception):
    pass


class DesignCalculator:

    @staticmethod
    def colour_match(wall_colour: str, flour_colour: str):
        if not all((isinstance(flour_colour, str), isinstance(wall_colour, str))):
            raise DecorTasteError
        if wall_colour == "Оливковый" and flour_colour == "Темный дуб":
            return "Идеально"
        elif wall_colour != flour_colour:
            return "Ну красиво же"
        else:
            return "Это печально"


class TestColour:

    @pytest.mark.parametrize(("wall_colour", "flour_colour", "result"), [
        ("Оливковый", "Темный дуб", "Идеально"),
        ("Оливковый", "Графит", "Ну красиво же"),
        ("Розовый", "Розовый", "Это печально")
    ])
    def test_1(self, wall_colour, flour_colour, result):
        colour = DesignCalculator()
        assert colour.colour_match(wall_colour, flour_colour) == result

    def test_2(self):
        colour = DesignCalculator()
        assert colour.colour_match("Оливковый","Темный дуб") == "Идеально"

    def test_3(self):
        colour = DesignCalculator()
        assert colour.colour_match("Розовый", "Розовый") == "Это печально"
