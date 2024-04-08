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
        print("hi")
        self.calc = Calc()

    def tearDown(self):
        print()
        print("Buy")

     @classmethod
    def setUpClass(cls):
        print()
        print("Oh")

    @classmethod
    def tearDownClass(cls):
        print()
        print("Ho")

    def test_1(self):
        self.assertEqual(self.calc.concatinate(3, 4), 7)

    def test_2(self):
        self.assertIsInstance(self.calc.concatinate(3, 4), int)

    def test_3(self):
        self.assertTrue(self.calc.concatinate(3, 4), 7)

    def test_4(self):
        self.assertGreaterEqual(self.calc.concatinate(3, 4), 7)

    def test_5(self):
        self.assertDictEqual(self.calc.concatinate(3, 4), 7)

    def test_6(self):
        with self.assertRaises(TypeError):
            self.calc.concatinate(3, 4, 5)

    def test_7(self):
        self.assertEqual(5, "5")

    def test_8(self):
        self.assertEqual(2 + "3", "5")
