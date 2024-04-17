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


@pytest.mark.skip
class TestMarks:
    @pytest.mark.regression
    def test_regress(self):
        print("This test case is in regression scope")

    @pytest.mark.smoke
    def test_regress(self):
        print("This test case is in regression scope")


@pytest.fixture(scope="module", autouse=True)
def module_test_design():
    print("\nStart test design")
    yield
    print("\nEnd test design")


@pytest.fixture(scope="class", autouse=True)
def class_test_design():
    print("\nStart class test")
    yield
    print("\nEnd class test")


@pytest.fixture(autouse=True)
def calc_init():
    print("\nStart test case")
    calc = DesignCalculator()
    yield calc
    print("\nEnd test case")


class TestInputData:
    @pytest.mark.regression
    def test_correct_data(self, calc_init):
        result = calc_init.colour_match("black", "pink")
        assert isinstance(result, str)

    @pytest.mark.smoke
    def test_correct_error(self, calc_init):
        with pytest.raises(DecorTasteError):
            result = calc_init.colour_match("black", 2)

    @pytest.mark.xfail(reason="waiting XPASS")
    def test_xpass(self, calc_init):
        result = calc_init.colour_match("black", "")
        assert isinstance(result, str)

    @pytest.mark.xfail(reason="waiting XFAILED")
    def test_xfail(self, calc_init):
        result = calc_init.colour_match("black", [])
        assert isinstance(result, str)


class TestDesign:

    @pytest.mark.smoke
    def test_ideal_case(self, calc_init):
        result = calc_init.colour_match("Оливковый", "Темный дуб")
        assert result == "Идеально"

    def test_ug(self, calc_init):
        result = calc_init.colour_match("Коричневый", "Коричневый")
        assert result == "Это печально"

    def test_ok_case(self, calc_init):
        result = calc_init.colour_match("White", "Blue")
        assert result == "Ну красиво же"

    @pytest.mark.parametrize("wall_color, flour_color", [
        pytest.param("Black", "Black", marks=[pytest.mark.regression]),
        pytest.param("White", "Pink", marks=[pytest.mark.smoke]),
        pytest.param(5, 3456, marks=[pytest.mark.xfail])
    ])
    def test_common_cases(self, wall_color, flour_color):
        assert wall_color != flour_color

    @pytest.mark.parametrize("wall_color, flour_color, result", [
        ("Оливковый", "Темный дуб", False),
        ("White", "Pink", True),
        ("Black", "Black", False),
        ("Red", "Red", True)
    ])
    def test_maybe_krasivo(self, wall_color, flour_color, result):
        if wall_color == "Оливковый" and flour_color == "Темный дуб":
            print("===============", "Идеально", "===============", sep="\n")
        else:
            assert (flour_color != wall_color) == result





