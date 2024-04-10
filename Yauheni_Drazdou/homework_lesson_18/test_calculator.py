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
        print("\nTest result:")
        self.calc = Calc()


    def test1_calc_addition(self):
        self.assertEqual(self.calc.calc(10, 5, "+"), 15)

    def test2_calc_subtraction(self):
        self.assertEqual(self.calc.calc(5, 6, "-"), -1)

    def test3_calc_multiplication(self):
        self.assertEqual(self.calc.calc(10, 5, "*"), 50)

    def test4_calc_division(self):
        self.assertEqual(self.calc.calc(10, 5, "/"), 2)

    def test_5_invalid_operation(self):
        self.assertEqual(self.calc.calc(4, 5, "&"), "Error")


   #expected error
    def test6_calc_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.calc(3, 0, "/")

    def test7_float_input(self):
        with self.assertRaises(TypeError):
            self.calc.calc(3.4, 6.6, "+")

    def test8_more_then_two_args(self):
        with self.assertRaises(TypeError):
            self.calc.calc((3, 4), 6, "+")

    def test_9_int_result(self):
        self.assertIsInstance(self.calc.calc(3, 4, "+"), int)

