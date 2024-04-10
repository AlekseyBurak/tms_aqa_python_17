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
        print("Hi I am setup")
        self.calc = Calc()

    def test_addition(self):
        self.assertEqual(self.calc.calc(5, 2, "+"), 7)

    def test_subtraction(self):
        self.assertEqual(self.calc.calc(5, 2, "-"), 3)

    def test_multiplication(self):
        self.assertEqual(self.calc.calc(5, 2, "*"), 10)

    def test_division(self):
        self.assertEqual(self.calc.calc(10, 2, "/"), 5)

    def test_non_existent_operation(self):
        self.assertEqual(self.calc.calc(10, 2, "^"), "Error")

    def test_operand_not_str(self):
        self.assertEqual(self.calc.calc(10, 2, 3), "Error")

    def test_number_str(self):
        with self.assertRaises(TypeError):
            self.calc.calc(10, "2", "+")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.calc(5, 0, '/')

    @unittest.expectedFailure
    def test_division_1(self):
        self.assertEqual(self.calc.calc(10, 3, "/"), 3)

    @unittest.skip("accepts only int")
    def test_number1_float(self):
        with self.assertRaises(TypeError):
            self.calc.calc(7.2, 6.5, "+")




