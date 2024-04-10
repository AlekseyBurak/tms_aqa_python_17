import unittest
class Calc:
    def concatinate(self, a: int, b: int):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Error"

class TestCalc(unittest.TestCase):

    def setUp(self):
        print()
        print("Hi i am setup")
        self.calc = Calc()

    def tearDown(self):
        print()
        print("Hi i am teardown")


    def test_1(self):
        calc = Calc()
        self.assertEquals(calc.concatinate(3, 4), 7)

    def test_2(self):
        calc = Calc()
        self.assertIsInstance(calc.concatinate(3, 4), int)


    # def test_3(self):
        # calc = Calc()
        # self.assertIsInstance(calc.concatinate(3.0, 4), "Error")


