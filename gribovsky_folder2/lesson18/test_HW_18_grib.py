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
        print("*****start test******")
        self.calc = Calc()

    def tearDown(self):
        print()
        print("*****end test******")

    @classmethod
    def setUpClass(cls):
        print("start test run")

    @classmethod
    def tearDownClass(cls):
        print("end test run")

    def test_addition(self):
        """Проверяем сложение"""
        self.assertEqual(self.calc.calc(2, 5, "+"), 7)

    def test_subtraction(self):
        """Проверяем вычитание"""
        self.assertEqual(self.calc.calc(2, 5, "-"), -3)

    def test_multiplication(self):
        """Проверяем умножение"""
        self.assertEqual(self.calc.calc(2, 5, "*"), 10)

    def test_division(self):
        """Проверяем деление"""
        self.assertEqual(self.calc.calc(2, 5, "/"), 0.4)

    def test_1(self):
        """Проверяем невалидную операцию"""
        self.assertEqual(self.calc.calc(2, 5, ""), "Error")

    def test_2(self):
        """Проверяем негативный сценарий сравнения со строкой"""
        self.assertEqual(self.calc.calc(2, 5, "-"), "-3")

    def test_3(self):
        """Проверяем возвращение строке при невалидной операции"""
        self.assertIsInstance(self.calc.calc(2, 5, ""), str)

    def test_4(self):
        """Проверяем возврат числа при позитивном сценарии"""
        self.assertIsInstance(self.calc.calc(2, 5, "+"), int)

    @unittest.skip("just for demo purpose")
    def test_5(self):
        self.assertEqual(self.calc.calc("5", "2", "*"), "Error")

    @unittest.expectedFailure
    def test_6(self):
        self.assertEqual(self.calc.calc(), "Error")

    def test_7(self):
        """Проверяем деление на ноль"""
        with self.assertRaises(ZeroDivisionError):
            (self.calc.calc(2, 0, "/"))


