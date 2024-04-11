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

class TestCaclulatorMethods(unittest.TestCase):

    def setUp(self):
        self.calculator = Calc()
        print("set up...")

    def test_operation_addition(self):
        self.assertEqual(self.calculator.calc(1, 2, "+"), 3)

    def test_operation_subtraction(self):
        self.assertEqual(self.calculator.calc(2, 1, "-"), 1)

    def test_operation_multiplication(self):
        self.assertEqual(self.calculator.calc(2, 3, "*"), 6)

    def test_operation_division(self):
        self.assertEqual(self.calculator.calc(10, 5, "/"), 2)

    def test_addition_1(self):
        self.assertEqual(self.calculator.calc(5, -10, "+"), -5)

    def test_addition_2(self):
        self.assertEqual(self.calculator.calc(-5, -10, "+"), -15)

    def test_subtraction_1(self):
        self.assertEqual(self.calculator.calc(-10, -1, "-"), -9)

    def test_subtraction_2(self):
        self.assertEqual(self.calculator.calc(-10, 1, "-"), -11)

    def test_subtraction_3(self):
        self.assertEqual(self.calculator.calc(10, -1, "-"), 11)

    def test_multiplication_1(self):
        self.assertEqual(self.calculator.calc(-1, 1, "*"), -1)

    def test_multiplication_2(self):
        self.assertEqual(self.calculator.calc(1, 0, "*"), 0)

    def test_division_1(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calc(1, 0, "/")

    def test_division_2(self):
        self.assertNotEqual(self.calculator.calc(11, 2, "/"), 5)

    def test_operation_1(self):
        self.assertEqual(self.calculator.calc(1, 0, "?"), "Error")

    def test_operation_2(self):
        self.assertEqual(self.calculator.calc(1, 0, " "), "Error")

    def test_operation_3(self):
        self.assertEqual(self.calculator.calc(1, 0, "++"), "Error")

    def test_operand_a_str(self):
        with self.assertRaises(TypeError):
            self.calculator.calc("1", 0, "+")

    def test_operand_b_str(self):
        with self.assertRaises(TypeError):
            self.calculator.calc(1, "0", "+")

    def test_operand_not_str(self):
        self.assertEqual(self.calculator.calc(1, 0, 1), "Error")

    @unittest.skip("know issue")
    def test_operand_a_float(self):
        with self.assertRaises(TypeError):
            self.calculator.calc(1.0, 0, "+")

    @unittest.skip("know issue")
    def test_operand_b_float(self):
        with self.assertRaises(TypeError):
            self.calculator.calc(1, 1.1, "+")