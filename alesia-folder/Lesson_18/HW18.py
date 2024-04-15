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
        print("\nHi I'm setup")
        self.calc = Calc()

    def tearDown(self):
        print("Hello I'm teardown")

    def test_equal_sum(self):
        self.assertEqual(self.calc.calc(3, 4, "+"), 7)
    def test_return_int(self):
        self.assertIsInstance(self.calc.calc(3, 4, "+"), int)
    def test_negative_less_0(self):
        self.assertLess(self.calc.calc(-3, -4, "+"), 0)
    def test_not_str(self):
        self.assertIsNot(self.calc.calc(3, 4, "+"), str)
    def test_is_in(self):
        self.assertIn(self.calc.calc(3, 4, "+"), (6, 7, 8))
    def test_equal_diff(self):
        self.assertEqual(self.calc.calc(3, 4, "-"), -1)
    def test_not_equal(self):
        self.assertNotEqual(self.calc.calc(3, 4, "-"), 3)
    def test_not_in(self):
        self.assertNotIn(self.calc.calc(3, 4, "-"), (1, 2, 0))
    def test_equal_mult(self):
        self.assertEqual(self.calc.calc(3, 4, "*"), 12)
    def test_greater(self):
        self.assertGreater(self.calc.calc(3, 4, "*"), 3)
    def test_equal_division(self):
        self.assertEqual(self.calc.calc(4, 2, "/"), 2)

