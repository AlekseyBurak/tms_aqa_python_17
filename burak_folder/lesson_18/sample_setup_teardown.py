import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print("I'm in setUp()")

    @classmethod
    def setUpClass(cls):
        print("I'm in setUpClass()")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def tearDown(self):
        print("I'm in tearDown()")

    @classmethod
    def tearDownClass(cls):
        print("I'm in tearDownClass()")
