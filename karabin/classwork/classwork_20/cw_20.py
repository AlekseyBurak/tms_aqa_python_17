import pytest


#
# @pytest.mark.parametrize("login", "password",
#                          (("Aburak", 1234),
#                           ("Aburak", 2345),
#                           ("Aburak", 3456)
#                           ))
#
#
# @pytest.mark.parametrize("login, password", [
#         pytest.param("Aburak", 1234, marks=[pytest.mark.regression]),
#         pytest.param("Aburak", 2345, marks=[pytest.mark.xfail]),
#         pytest.param("Aburak", 3456, marks=[pytest.mark.xfail])
# ])
# def test_auth(login, password):
#     assert login == "Aburak"
#     assert password == 1234


@pytest.mark.parametrize("ATM", ("Alfa", "Sber", "BNB"))
@pytest.mark.parametrize("card", ("Alfa-card", "Sber-card", "BNB-card"))
@pytest.mark.parametrize("NFC", (True, False))
def test_auth(ATM, card, NFC):
    print(ATM, card, NFC)
