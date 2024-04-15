import unittest

class Calc:
    def concatinate(self, a: int, b: int):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Error"

class TestCalc(unittest.TestCase):

    def setUp(self):
        print("Hi i am setup")
        self.calc = Calc()

    def tearDown(self):
        print()
        print("Hi i am tear down")


    @classmethod
    def setUpClass(cls):
        print()
        print("Hi i am Class down")

    @classmethod
    def tearDownClass(cls):
        print()
        print("Hi i'm Class tear down")



    def test_1(self):
        # calc = Calc()
        self.assertEqual(self.calc.concatinate(3, 4), 7)




    def test_2(self):
        calc = Calc()
        self.assertIsInstance(calc.concatinate(3, 4), int)

    def test_3(self):
        calc = Calc()
        self.assertEqual(calc.concatinate(3.0, 4), "Error")

    # def test_4(self):
    #     calc = Calc()
    #     with self.assertRaises(TypeError):
    #         calc.concatinate(3, 4, 5)



    def test_4(self):
        calc = Calc()
        with self.assertRaises(ValueError):
            calc.concatinate(3, 4, 5)

    def test_5(self):
        self.assertEqual(5, "5")

    def test_6(self):
        self.assertEqual(2 + "3", "5")




