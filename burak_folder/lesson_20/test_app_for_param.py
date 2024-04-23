import pytest


class DecorTasteError(Exception):
    pass


class DesignCalculator:

    def colour_match(self, wall_colour: str, flour_colour: str):
        if not all((isinstance(flour_colour, str), isinstance(wall_colour, str))):
            raise DecorTasteError
        if wall_colour == "Оливковый" and flour_colour == "Тёмный дуб":
            return "Идеально"
        elif wall_colour != flour_colour:
            return "Ну красиво же"
        else:
            return "Это печально"


@pytest.mark.parametrize("wall_colour", ("Оливковый", "Темный дуб", "Розовый"))
@pytest.mark.parametrize("flour_colour", ("Оливковый", "Темный дуб", "Розовый"))
def test_param(wall_colour, flour_colour):
    calc = DesignCalculator()
    # if isinstance(wall_colour, str) is False or isinstance(flour_colour, str) is False:
    #     with pytest.raises(DecorTasteError):
    result = calc.colour_match(wall_colour, flour_colour)
    if wall_colour == "Оливковый" and flour_colour == "Темный дуб":
        assert result == "Идеально", f"{wall_colour=} {flour_colour=}"
    elif wall_colour != flour_colour:
        assert result == "Ну красиво же", f"{wall_colour=} {flour_colour=}"
    else:
        assert result == "Это печально", f"{wall_colour=} {flour_colour=}"
