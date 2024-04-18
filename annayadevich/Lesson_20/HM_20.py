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


class TestPytestDesignCalculator:

    def test_successful_message_1(self):
        calculator = DesignCalculator()
        successful_message = "Идеально"
        assert calculator.colour_match("Оливковый", "Темный дуб") == successful_message

    def test_successful_message_2(self):
        calculator = DesignCalculator()
        successful_message = "Ну красиво же"
        assert calculator.colour_match("Оливковый", "Серый") == successful_message

    def test_error_message(self):
        calculator = DesignCalculator()
        error_message = "Это печально"
        assert calculator.colour_match("Оливковый", "Оливковый") == error_message

    #
    @pytest.mark.skip(reason="accepts only str")
    def test_invalid_value(self):
        calculator = DesignCalculator()
        with pytest.raises(TypeError):
            calculator.colour_match(33313, 332.33)

    @pytest.mark.parametrize("wall_colour, flour_colour, message_1", [
        pytest.param("Оливковый", "Темный дуб", "Идеально", marks=[pytest.mark.smoke]),
        pytest.param("Оливковый", "Серый", "Ну красиво же", marks=[pytest.mark.smoke]),
        pytest.param("Серый", "Серый", "Это печально", marks=[pytest.mark.new_features_testing])
    ])
    def test_param_test(self, wall_colour, flour_colour, message_1):
        print(wall_colour, flour_colour, message_1)
