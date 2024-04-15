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
        print("Hi i am setup")
        self.calc = Calc()

    def tearDown(self):
        print()
        print("Hi i am tear down")


    def test_addition(self):
        result = self.calc.calc(1, 2, "+")
        self.assertEqual(result, 3)

    def test_subtraction(self):
        result = self.calc.calc(2, 1, "-")
        self.assertEqual(result, 1)

    def test_multiplication(self):
        result = self.calc.calc(2, 3, "*")
        self.assertEqual(result, 6)

    def test_division(self):
        result = self.calc.calc(4, 2, "/")
        self.assertEqual(result, 2)

    def test_invalid_operation(self):
        result = self.calc.calc(4, 2, "%")
        self.assertEqual(result, "Error")
