import pytest
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

class TestDesignCalc:

    @pytest.mark.parametrize(("wall_colour", "flour_colour", "result"), [
        ("Оливковый", "Темный дуб", "Идеально"),
        ("Оливковый", "Красный", "Ну красиво же"),
        ("Оливковый", "Оливковый", "Это печально"),
        ("Red", "Red", "Это печально")
    ])
    def test_colors(self, wall_colour, flour_colour, result):
        colors = DesignCalculator()
        assert colors.colour_match(wall_colour, flour_colour) == result

    @pytest.mark.parametrize(("wall_colour", "flour_colour"), [
        (1, 2),
        ("Оливковый", 7),
        (0.4, "Red"),
        (("Blue", "White"), ("Blue", "White"))
        ])
    def test_wrong_decor_error(self, wall_colour, flour_colour):
        result = DesignCalculator()
        with pytest.raises(DecorTasteError):
            result.colour_match(wall_colour, flour_colour)

    @pytest.mark.xfail(reason="No colours chosen") #уточнить на уроке по поводу пустых полей
    def test_empty_spaces(self):
        result = DesignCalculator()
        with pytest.raises(ValueError):
            result.colour_match("", "")

