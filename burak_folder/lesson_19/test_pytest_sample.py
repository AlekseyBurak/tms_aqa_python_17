import time

import pytest

my_very_important_module = 4

class TestPytestMarks:

    @pytest.mark.smoke
    def test_smoke1(self):
        time.sleep(1)
        assert 1 == 2

    @pytest.mark.smoke
    def test_smoke2(self):
        time.sleep(1)

        assert True

    @pytest.mark.smoke
    def test_smoke3(self):
        time.sleep(1)

        assert True

    @pytest.mark.smoke
    @pytest.mark.mobile
    def test_android1(self):
        assert True

    @pytest.mark.mobile
    def test_android2(self):
        time.sleep(1)

        assert True

    def test_ios1(self):
        assert True

    def test_ios2(self):
        assert True

    @pytest.mark.e2e
    def test_e2e(self):
        assert True
