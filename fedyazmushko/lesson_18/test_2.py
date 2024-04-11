import unittest


class Calc:

    def concatinate(self, a: int , b: int):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "Error"



class TestCalc(unittest.TestCase):

    def setUp(self):
        print()
        print("i'm setup")
        self.calc = Calc()


    # def tearDown(self):
    #     print()
    #     print("i'm tear")
    #
    # @classmethod
    # def setUpClass(cls):
    #     print()
    #     print("i'm class setup")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print()
    #     print("i'm class teardown")



    def test_1(self):
        self.assertEqual(self.calc.concatinate(3, 4), 7)



    def test_2(self):

        self.assertIsInstance(self.calc.concatinate(3, 4), int)


   @unittest.skip
   def test_3(self):
        self.assertEqual(self.calc.concatinate(3.0, 4), "Error")

    def tast_4(self):

        with self.assertRaises(ValueError):
            self.calc.concatinate(3, 4, 5)


    def test_5(self):
        self.assertEqual(5, "5")


    def test_6(self):
        self.assertEqual(2 + "3", "5")

