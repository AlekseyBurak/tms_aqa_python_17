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
        print("Hi i'm setup")
        self.calc = Calc()

    def tearDown(self):
        print()
        print("Hi i'm tear down")

    @classmethod
    def setUpClass(cls):
        print()
        print("Hi i'm Class setup")

    @classmethod
    def tearDownClass(cls):
        print()
        print("Hi i'm Class tear down")

    def test_1(self):
        self.assertEqual(self.calc.concatinate(3, 4), 7)

    def test_2(self):
        self.assertIsInstance(self.calc.concatinate(3, 4), int)

    # @unittest.expectedFailure
    def test_3(self):
        self.assertEqual(self.calc.concatinate(3.0, 4), "Error")

    def test_4(self):
        with self.assertRaises(TypeError):
            self.calc.concatinate(3, 4, 5)
