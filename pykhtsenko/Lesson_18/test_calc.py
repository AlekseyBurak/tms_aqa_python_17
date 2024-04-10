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


import unittest
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_addition(self):
        result = self.calc.calc(3, 2, "+")
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calc.calc(3, 2, "-")
        self.assertEqual(result, 1)

    def test_multiplication(self):
        result = self.calc.calc(3, 2, "*")
        self.assertEqual(result, 6)

    def test_division(self):
        result = self.calc.calc(6, 2, "/")
        self.assertEqual(result, 3)

    def test_invalid_operation(self):
        result = self.calc.calc(3, 2, "%")
        self.assertEqual(result, "Error")

    def test_addition_negative_numbers(self):
        result = self.calc.calc(-3, 2, "+")
        self.assertEqual(result, -1)

    def test_subtraction_negative_numbers(self):
        result = self.calc.calc(-3, -2, "-")
        self.assertEqual(result, -1)

    def test_multiplication_negative_numbers(self):
        result = self.calc.calc(-3, 2, "*")
        self.assertEqual(result, -6)

    def test_division_negative_numbers(self):
        result = self.calc.calc(-6, 2, "/")
        self.assertEqual(result, -3)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.calc(6, 0, "/")

    def test_not_int(self):
        result = self.calc.calc(5.0, 2, "+")
        self.assertEqual(result, -3.0)


if __name__ == '__main__':
    unittest.main()