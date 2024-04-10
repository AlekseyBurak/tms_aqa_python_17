import unittest


class Calc:
    @staticmethod
    def calc(a: int, b: int, operation: str):
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
        print("Start")

    def tearDown(self):
        print("End")

    @classmethod
    def setUpClass(cls):
        print("Hi i'm Class setup")

    @classmethod
    def tearDownClass(cls):
        print("Hi i'm Class tear down")

    def test_addition_return_type(self):
        self.assertIsInstance(self.calc.calc(3, 4, "+"), int)

    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.calc(3, 4, "+"), 7)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.calc(-3, -4, "+"), -7)

    def test_addition_large_numbers(self):
        self.assertEqual(self.calc.calc(1234567890, 1234567890, "+"), 2469135780)

    @unittest.expectedFailure
    def test_addition_fractional_input_type(self):
        self.assertIsInstance(self.calc.calc(3.5, 4, "+"), int)

    def test_addition_string_input_type(self):
        with self.assertRaises(TypeError):
            self.calc.calc("av", 4, "+")

    def test_subtraction_return_type(self):
        self.assertIsInstance(self.calc.calc(3, 4, "-"), int)

    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.calc(3, 4, "-"), -1)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.calc(-3, -4, "-"), 1)

    def test_subtraction_large_numbers(self):
        self.assertEqual(self.calc.calc(1234567890, 1234567890, "-"), 0)

    @unittest.expectedFailure
    def test_subtraction_fractional_input_type(self):
        self.assertIsInstance(self.calc.calc(3, 4.5, "-"), int)

    def test_subtraction_none_input_type(self):
        with self.assertRaises(TypeError):
            self.calc.calc(4, None, "-")

    def test_multiplication_return_type(self):
        self.assertIsInstance(self.calc.calc(3, 4, "*"), int)

    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.calc(3, 4, "*"), 12)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.calc(-3, 4, "*"), -12)

    def test_multiplication_large_numbers(self):
        self.assertEqual(self.calc.calc(1234567890, 1234567890, "*"), 1524157875019052100)

    @unittest.expectedFailure
    def test_multiplication_fractional_input_type(self):
        self.assertIsInstance(self.calc.calc(3.5, 4, "*"), int)

    @unittest.expectedFailure
    def test_multiplication_string_input_type(self):
        self.assertIsInstance(self.calc.calc("&!$/\\^*(", 4, "*"), int)

    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.calc(10, 5, "/"), 2)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.calc(-5, 5, "/"), -1)

    def test_division_large_numbers(self):
        self.assertEqual(self.calc.calc(1234567890, 1234567890, "/"), 1)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.calc(20, 0, "/")

    def test_division_string_input_type(self):
        with self.assertRaises(TypeError):
            self.calc.calc("av", 4, "/")

    def test_arguments_number(self):
        with self.assertRaises(TypeError):
            self.calc.calc(3, 4, "/", 7)

    def test_invalid_operation(self):
        self.assertEqual(self.calc.calc(3, 4, "^"), "Error")
