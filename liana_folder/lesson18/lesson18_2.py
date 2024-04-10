import unittest


class Calc:
    def concatinate(self, a: int, b: int):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Error"


class TestCalc(unittest.TestCase):
    def test_1(self):
        calc = Calc()
        self.assertEqual(calc.concatinate(3, 4), 7)

    def test_2(self):
        calc = Calc()
        self.assertIsInstance(calc.concatinate(3, 4), int)

    def test_3(self):
        calc = Calc()
        self.assertIsInstance(calc.concatinate(3.2, 4.0), "Error")

    def test_4(self):
        calc = Calc()
        self.assertEqual(calc.concatinate(3.0, 4, "Error"))

    def test_5(self):
        calc = Calc()
        with self.assertRaises(ValueError):
            calc.concatinate(3,4, 6 )

