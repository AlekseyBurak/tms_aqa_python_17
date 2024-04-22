import pytest


class DecorTasteError(Exception):
    pass

class DesignCalculator:

    def colour_match(self, wall_colour: str, flour_colour: str):
        if not all((isinstance(flour_colour, str), isinstance(wall_colour, str))):
            raise DecorTasteError
        if wall_colour == "Olive" and flour_colour == "Dark oak":
            return "Perfect"
        elif wall_colour != flour_colour:
            return "Well, it's beautiful"
        else:
            return "Sad"


class TestDesignCalculator:

    @pytest.mark.smoke
    def test_colour_match_1(self, colour):
        assert colour.colour_match("Olive", "Dark oak") == "Perfect"

    @pytest.mark.parametrize("wall_colour, flour_colour", [
        pytest.param("Dark oak", "Oak", marks=[pytest.mark.smoke]),
        pytest.param("Oak", "Olive", marks=[pytest.mark.smoke]),
        pytest.param("Olive", "Oak", marks=[pytest.mark.critical_pass]),
        pytest.param("Oak", "Dark oak", marks=[pytest.mark.critical_pass])
        ])
    def test_colour_match_2(self, wall_colour, flour_colour, colour):
        assert colour.colour_match(wall_colour, flour_colour) == "Well, it's beautiful"

    @pytest.mark.parametrize("wall_colour, flour_colour", [
        pytest.param("Olive", "Olive", marks=[pytest.mark.smoke]),
        pytest.param("Dark oak", "Dark oak", marks=[pytest.mark.smoke]),
        pytest.param("Oak", "Oak", marks=[pytest.mark.critical_pass])
        # , pytest.param("Oak", "Dark oak", marks=[pytest.mark.critical_pass])  #specialno
        ])
    def test_colour_match_3(self, wall_colour, flour_colour, colour):
        assert colour.colour_match(wall_colour, flour_colour) == "Sad"

    @pytest.mark.parametrize("wall_colour, flour_colour", [
        pytest.param("Olive", 1, marks=[pytest.mark.critical_pass]),
        pytest.param(1, "Olive", marks=[pytest.mark.critical_pass]),
        pytest.param(1, 1, marks=[pytest.mark.critical_pass]),
        pytest.param(1.1, "Olive", marks=[pytest.mark.critical_pass]),
        pytest.param("Olive", 1.1, marks=[pytest.mark.critical_pass]),
        pytest.param(1.1, "Olive", marks=[pytest.mark.critical_pass]),
        pytest.param("Olive", None, marks=[pytest.mark.critical_pass]),
        pytest.param(None, "Olive", marks=[pytest.mark.critical_pass]),
        pytest.param("Dark oil", 1, marks=[pytest.mark.critical_pass]),
        pytest.param(1, "Dark oil", marks=[pytest.mark.critical_pass]),
        pytest.param(1, 1, marks=[pytest.mark.critical_pass]),
        pytest.param(1.1, "Dark oil", marks=[pytest.mark.critical_pass]),
        pytest.param("Dark oil", 1.1, marks=[pytest.mark.critical_pass]),
        pytest.param(1.1, "Dark oil", marks=[pytest.mark.critical_pass]),
        pytest.param("Dark oil", None, marks=[pytest.mark.critical_pass]),
        pytest.param(None, "Dark oil", marks=[pytest.mark.critical_pass]),
        ])
    def test_colour_match_4(self, wall_colour, flour_colour, colour):
        with pytest.raises(DecorTasteError):
            colour.colour_match(wall_colour, flour_colour)

    def test_without_arguments(self, colour):
        with pytest.raises(TypeError):
            colour.colour_match()