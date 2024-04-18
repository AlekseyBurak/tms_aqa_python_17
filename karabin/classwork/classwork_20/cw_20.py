import pytest


#
# @pytest.mark.parametrize("login", "password",
#                          (("Aburak", 1234),
#                           ("Aburak", 2345),
#                           ("Aburak", 3456)
#                           ))


# @pytest.mark.parametrize("login, password", [
#         pytest.param("Aburak", 1234, marks=[pytest.mark.regression]),
#         pytest.param("Aburak", 2345, marks=[pytest.mark.xfail]),
#         pytest.param("Aburak", 3456, marks=[pytest.mark.xfail])
# # ])
# def test_auth(login, password):
#     assert login == "Aburak"
#     assert password == 1234
#
#
@pytest.mark.parametrize("ATM", ("Alfa", "Sber", "BNB"))
@pytest.mark.parametrize("card", ("Alfa-card", "Sber-card", "BNB-card"))
@pytest.mark.parametrize("NFC", (True, False))
def test_auth(ATM, card, NFC):
    print(ATM, card, NFC)


# @pytest.mark.parametrize("login, password", [
#         pytest.param("Aburak", 1234, marks=[pytest.mark.regression]),
#         pytest.param("Aburak", 2345, marks=[pytest.mark.xfail]),
#         pytest.param("Aburak", 3456, marks=[pytest.mark.xfail])
#     ]

# import pytest
#
#
# @pytest.mark.parametrize("login, password, is_valid", [
#         pytest.param("Aburak", 1234, True, marks=[]),
#         pytest.param("Abirak", 2345, False, marks=[]),
#         pytest.param("Abirak", 3456, False, marks=[])
# ])
# def test_auth(login, password, is_valid):
#     assert (login == "Aburak") is is_valid
#     assert (password == 1234) is is_valid
#     assert (login == "Aburak") is is_valid and (password == 1234) is is_valid
#     assert all(((login == "Aburak"), (password == 1234))) is is_valid