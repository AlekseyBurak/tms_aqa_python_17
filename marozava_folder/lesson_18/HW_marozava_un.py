import unittest


class Calc:

    def operations(self, a: int, b: int, operation: str):
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
        self.assertEqual(self.calc.operations(5, 4, "+"), 9)

    def test_2(self):
        self.assertIsInstance(self.calc.operations(5, 4, "+"), int)

    def test_3(self):
        self.assertEqual(self.calc.operations(5, 3, "-"), 2)

    def test_4(self):
        self.assertIsInstance(self.calc.operations(5, 3, "-"), int)

    def test_5(self):
        self.assertEqual(self.calc.operations(3, 3, "*"), 9)

    def test_6(self):
        self.assertIsInstance(self.calc.operations(3, 3, "-"), int)

    def test_7(self):
        self.assertEqual(self.calc.operations(9, 3, "/"), 3)

    def test_8(self):
        self.assertIsInstance(self.calc.operations(9, 3, "/"), float)

    @unittest.expectedFailure
    def test_9(self):
        self.calc.operations(9, 0, "/")

    @unittest.expectedFailure
    def test_10(self):
        self.assertFalse(self.calc.operations(4.0, 2, "*"), "Error")




