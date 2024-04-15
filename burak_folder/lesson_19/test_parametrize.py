import pytest


@pytest.mark.parametrize("login, password, is_valid", [
        pytest.param("Aburak", 1234, True, marks=[]),
        pytest.param("Abirak", 2345, False, marks=[]),
        pytest.param("Abirak", 3456, False, marks=[])
])
def test_auth(login, password, is_valid):
    assert (login == "Aburak") is is_valid
    assert (password == 1234) is is_valid
    assert (login == "Aburak") is is_valid and (password == 1234) is is_valid
    assert all(((login == "Aburak"), (password == 1234))) is is_valid
