import pytest

@pytest.fixture()
def calc_init():
    print("\nHello from pytest")
    calc = Calc()
    return calc
    print("\nHe He i'm done")

@pytest.fixture(autouse=True)
def connect_to_sql():
    print("\n kdslklsjdkkds")
    yield
    print("\ndisconnect to sql")
@pytest.fixture(scope="class", autouse=True)
def class_scope():
    print("\nClass setup")
    yield
    print("\nClass teardown")
@pytest.fixture(scope="session", autouse=True)
def class_scope():
    print("\nsession setup")
    yield
    print("\nSession teardown")