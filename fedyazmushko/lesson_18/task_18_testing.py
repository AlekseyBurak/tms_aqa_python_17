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


class TestApplication(unittest.TestCase):

    def setUp(self):
        print()
        print("i'm setUp")
        self.calc = Calc()

    def tearDown(self):
        print()
        print("i'm tearDown")


    def test_1(self):
        self.assertEqual(self.calc.calc(6, 2, "+"), 8)

    def test_2(self):
        self.assertEqual(self.calc.calc(6, 2, "-"), 4)

    def test_3(self):
        self.assertEqual(self.calc.calc(6, 2, "*"), 12)

    def test_4(self):
        self.assertEqual(self.calc.calc(6, 2, "/"), 3)

    def test_5(self):
        self.assertIsInstance(self.calc.calc(6, 2, "+"), (int, str))

    # def test_6(self):
    #     with self.assertRaises(TypeError):
    #         self.calc.calc(6, 2, 54)
    # С этим немного не разобрался)
    # ...