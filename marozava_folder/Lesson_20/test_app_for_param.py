import pytest


class DecorTasteError(Exception):
    pass


class DesignCalculator:

    def colour_match(self, wall_colour: str, flour_colour: str):
        if not all((isinstance(flour_colour, str), isinstance(wall_colour, str))):
            raise DecorTasteError
        if wall_colour == "olive" and flour_colour == "dark oak":
            return "Perfect"
        elif wall_colour != flour_colour:
            return "Well it's beautiful"
        else:
            return "It is sad"


def test_perfect_match(calculator):
    assert calculator.colour_match("olive", "dark oak") == "Perfect"


def test_beautiful_match(calculator):
    assert calculator.colour_match("olive", "light oak") == "Well it's beautiful"


def test_sad_match(calculator):
    assert calculator.colour_match("olive", "olive") == "It is sad"


def test_invalid_input_type(calculator):
    with pytest.raises(DecorTasteError):
        calculator.colour_match(123, "dark oak")


def test_another_invalid_input_type(calculator):
    with pytest.raises(DecorTasteError):
        calculator.colour_match("olive", 123)


@pytest.mark.parametrize("wall_colour, flour_colour, expected", [
    ("olive", "dark oak", "Perfect"),
    ("olive", "light oak", "Well it's beautiful"),
    ("olive", "olive", "It is sad")
])
def test_colour_match(calculator, wall_colour, flour_colour, expected):
    assert calculator.colour_match(wall_colour, flour_colour) == expected


@pytest.mark.xfail(reason="Because")
@pytest.mark.parametrize("wall_colour, flour_colour, expected", [
    ("olive", "dark oak", "It is sad"),
    ("olive", "light oak", "Well it's beautiful"),
    ("olive", "olive", "It is sad")
])
def test_colour_match(calculator, wall_colour, flour_colour, expected):
    assert calculator.colour_match(wall_colour, flour_colour) == expected

