import unittest


class Calc:
    def concatinate(self, a: int, b: int):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Error"


class TestCalc(unittest.TestCase):

    def setUp(self):
        print()
        print("Hello")
        self.calc = Calc()

    def test_1(self):
        self.assertEquals(self.calc.concatinate(3,4), 7)

    def test_2(self):
        self.assertIsInstance(self.calc.concatinate(3,4), int)

    def test_5(self):
        self.assertEquals(5, "5")

    def test_6(self):
        self.assertEquals(2 + "5", "5")