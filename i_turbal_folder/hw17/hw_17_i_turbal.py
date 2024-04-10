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

    def test_summ_int(self):
        """
        Позитивная проверка сумма интов
        """
        self.assertEqual(self.calc.calc(1,2, "+"), 3)

    def test_sum_str(self):
        """
        Негативная проверка операции инта и строки
        """
        with self.assertRaises(TypeError):
            self.calc.calc(3, '2', '-')


    def test_multuply_float(self): #investigate
        """
        Проверка с числом с плав. запятой
        """
        self.assertEqual(self.calc.calc(2, 3.2, "*"),6.4)

    def test_not_existed_operation(self):
        """
        Проверка выбора не валидной операции
        """
        self.assertEqual(self.calc.calc(1, 2, '%'), 'Error')

    def test_division_with_remainder(self):
        """
        Проверка деление с остатком
        """
        self.assertIsInstance(self.calc.calc(3,2, '/'), float)

    def test_division_by_zero(self):
        """
        Проверка деления на нуль
        """
        with self.assertRaises(ZeroDivisionError):
            self.calc.calc(10,0, '/')

    def test_result_is_not_str(self):
        """
        Проверка, что не возращает сторку, чисто для прикола
        """
        self.assertNotIsInstance(self.calc.calc(1, 2, "-"), str)

