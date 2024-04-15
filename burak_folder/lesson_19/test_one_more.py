import pytest


@pytest.fixture(autouse=True)
def should_be_2(should_be_1):
    print("\nFrom should_be_second setup")
    yield
    print("\nFrom should_be_second teardown")


@pytest.fixture(autouse=True)
def should_be_3():
    print("\nFrom should_be_third setup")
    yield
    print("\nFrom should_be_third teardown")


@pytest.fixture(autouse=True)
def should_be_1(should_be_3):
    print("\nFrom should_be_first setup")
    yield
    print("\nFrom should_be_first teardown")


@pytest.mark.parametrize("value", [
        pytest.param(1, marks=[pytest.mark.skip]),
        pytest.param(2, marks=[pytest.mark.regression]),
        pytest.param(3, marks=[pytest.mark.skip])
])
def test_complex_param(value):
    assert value == 2