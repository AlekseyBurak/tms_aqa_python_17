import pytest

from fedyazmushko.lesson_19.test_lesson_work import Calc

@pytest.fixture()
def calc_init():
    print("\nHello from pytest")
    calc = Calc()
    yield calc
    print("\nHe He i'm done")


@pytest.fixture(autouse=True)
def connect_to_sql():
    print("\nConnecting to SQL Data Base")
    yield
    print("\nConnecting from SQL Data Base")


@pytest.fixture(scope="class", autouse=True)
def class_scope():
    print("\nClass setup")
    yield
    print("\nClass teardown")


@pytest.fixture(scope="module", autouse=True)
def module_scope():
    print("\nModule setup")
    yield
    print("\nModule teardown")


@pytest.fixture(scope="session", autouse=True)
def session_scope():
    print("\nSession setup")
    yield
    print("\nSession teardown")