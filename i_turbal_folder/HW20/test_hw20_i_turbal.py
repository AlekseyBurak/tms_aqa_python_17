import pytest
import application



class TestSmoke:
    @pytest.mark.parametrize("wall_colour, flour_colour, message", [
        pytest.param('Оливковый', 'Темный дуб', 'Идеально'),
        pytest.param('Темный дуб', 'Оливковый', 'Ну красиво же'),
        pytest.param('Темный дуб', 'Темный дуб', 'Это печально'),
        pytest.param('Темный дуб', 'Оливковый', 'Это печально', marks=[pytest.mark.skip]),
    ])
    def test_smoke(self, app, wall_colour, flour_colour, message):
        result = app.colour_match(wall_colour, flour_colour)
        assert result == message

class TestNegativeCase:
    @pytest.mark.negativecase
    def test_int(self, app):
        with pytest.raises(application.DecorTasteError):
            app.colour_match('123', 123)
