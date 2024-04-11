import unittest


class Calc:
    def calc(self, a: int, b: int, operation: str):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            return "Error"


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    @classmethod
    def tearDownClass(cls):
        print("End")

    def test_1(self):
        self.assertIsInstance(self.calc.calc(3, 5, "*"), int)

    @unittest.expectedFailure
    def test_2(self):
        self.assertEqual(self.calc.calc(6,10, "+"), 16)

    @unittest.expectedFailure
    def test_3(self):
        self.assertFalse(self.calc.calc(3.0, 2, "*"), "Error")

    @unittest.expectedFailure
    def test_4(self):
        self.assertFalse(self.calc.calc(3, 7, "*"), 22)

    def test_5(self):
        self.assertLessEqual(self.calc.calc(10, 3, "*"), 32)

    @unittest.expectedFailure
    def test_6(self):
        self.assertDictEqual(self.calc.calc(18, 9, "-"), 9, 1)

