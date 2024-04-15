import pytest

class Calc:

    def concatinate(self, a: int, b: int):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Error"

@pytest.fixture()
def calc_init():
    print("\nHello from pytest")
    calc = Calc()
    yield calc
    print("\nHe He i'm done")


@pytest.fixture()
def connect_to_lesson19():
    print("\nFrom lesson19 setup")
    yield
    print("\nFrom lesson19 teardown")


# @pytest.fixture(scope="class", autouse=True)
# def class_scope():
#     print("\nClass setup")
#     yield
#     print("\nClass teardown")
#
#
# @pytest.fixture(scope="module", autouse=True)
# def module_scope():
#     print("\nModule setup")
#     yield
#     print("\nModule teardown")

# @pytest.fixture(scope="session", autouse=True)
# def session_scope():
#     print("\nSession setup")
#     yield
#     print("\nSession teardown")
