import pytest

@pytest.mark.parametrize("ATM", ("Alfa", "Sber", "Prior"))
@pytest.mark.parametrize("card", ("Alfa-card", "Sber-card", "Prior-card"))
@pytest.mark.parametrize("NFC", (True, False))
def test_auth(ATM, card, NFC):
    print(ATM, card, NFC)