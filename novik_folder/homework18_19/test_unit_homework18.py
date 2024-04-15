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

    def test_sum(self):
       self.assertEqual(self.calc.calc(3, 4, "+"), 7)

    def test_sum_greater(self):
        self.assertGreater(self.calc.calc(3, 5, "+"), 7)

    def test_sum_isnot(self):
        self.assertIsNot(self.calc.calc(4, 1, "+"), "error")

    def test_subtraction(self):
        self.assertEqual(self.calc.calc(0, 10, "-"), -10)

    def test_multiply(self):
        self.assertEqual(self.calc.calc(1, 2, "*"), 2)

    def test_divide(self):
        self.assertEqual(self.calc.calc(9,3,"/"), 3)

    def test_is_int(self):
        self.assertIsInstance(self.calc.calc(9, 1, "-"), int)

    def test_object_double(self):
        self.assertRaises(self.calc.calc(8.1, 2, "+"), TypeError)

    def test_is_not_int(self):
        self.assertNotIsInstance(self.calc.calc(9, 1, "-"), str)

    def test_invalid_operation(self):
        self.assertIs(self.calc.calc(9,3, 1), "Error")

    def test_invalid_object(self):
        self.assertEqual(self.calc.calc("la", 3, 1), "Error")

    def test_no_operation(self):
        self.assertRaises(self.calc.calc(2, 4), TypeError)

    def test_divide_0(self):
        self.assertRaises(self.calc.calc(9,0,"/"), ZeroDivisionError)