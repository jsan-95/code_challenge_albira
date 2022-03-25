import unittest

from FirstFactorial.first_factorial import FirstFactorial


class TestFirstFactorial(unittest.TestCase):

    def test_first_factorial(self):
        self.assertEqual(FirstFactorial(1), 1)
        self.assertEqual(FirstFactorial(4), 24)
        self.assertEqual(FirstFactorial(8), 40320)
        self.assertEqual(FirstFactorial(10), 3628800)
        self.assertEqual(FirstFactorial(18), 6402373705728000)


if __name__ == '__main__':
    unittest.main()
