import pytest



# @pytest.mark.parametrize("login, password", (
#         ("Fzmushko", 1234), ("Fzmushko", 12345)))

@pytest.mark.parametrize("ATM", ("Alfa", "Sber"))
@pytest.mark.parametrize("card", ("Alfa-card", "Sber-card", "BNB-card"))
@pytest.mark.parametrize("NFC", (True, False))
def test_auth(ATM, card, NFC):
    print(ATM, card)


