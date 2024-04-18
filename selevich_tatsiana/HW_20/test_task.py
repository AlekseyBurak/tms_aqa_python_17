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


class TestPositiveCase:
    def test_perfect_message(self, calc_init):
        expected_message = "Идеально"
        assert calc_init.colour_match("Оливковый", "Темный дуб") == expected_message

    @pytest.mark.parametrize("wall_colour, flour_colour", [
        pytest.param("Темный дуб", "Оливковый", marks=[pytest.mark.smoke]),
        pytest.param("Оливковый", "Иной цвет", marks=[pytest.mark.regression]),
        pytest.param("Иной цвет", "Темный дуб", marks=[pytest.mark.regression])
    ])
    def test_good_message(self, wall_colour, flour_colour, calc_init):
        expected_message = "Ну красиво же"
        assert calc_init.colour_match(wall_colour, flour_colour) == expected_message

    @pytest.mark.parametrize("wall_colour, flour_colour", [
        pytest.param("Оливковый", "Оливковый", marks=[pytest.mark.smoke]),
        pytest.param("Темный дуб", "Темный дуб", marks=[pytest.mark.regression]),
        pytest.param("Иной цвет", "Иной цвет", marks=[pytest.mark.regression])
    ])
    def test_bad_message(self, wall_colour, flour_colour, calc_init):
        expected_message = "Это печально"
        assert calc_init.colour_match(wall_colour, flour_colour) == expected_message


class TestNegativeCase:
    @pytest.mark.parametrize("wall_colour, flour_colour", [
        pytest.param("Темный дуб", 5, marks=[pytest.mark.smoke]),
        pytest.param(3.4, "Оливковый", marks=[pytest.mark.smoke]),
        pytest.param(24, 36.6, marks=[pytest.mark.regression]),
        pytest.param(None, "Оливковый", marks=[pytest.mark.regression]),
        pytest.param("Темный дуб", None, marks=[pytest.mark.regression])
    ])
    def test_invalid_arguments(self, wall_colour, flour_colour, calc_init):
        with pytest.raises(DecorTasteError):
            calc_init.colour_match(wall_colour, flour_colour)

    @pytest.mark.skip(reason="not implemented")
    def test_over_arguments(self, calc_init):
        with pytest.raises(TypeError):
            calc_init.colour_match("Оливковый", "Темный дуб", "/")

    def test_without_arguments(self, calc_init):
        with pytest.raises(TypeError):
            calc_init.colour_match()
