import unittest

from FirstReverse.first_reverse import FirstReverse


class TestFirstReverse(unittest.TestCase):

    def test_first_reverse(self):
        input_str = 'I Love Code'
        self.assertEqual(FirstReverse(input_str), 'edoC evoL I')
        input_str = 'coderbyte'
        self.assertEqual(FirstReverse(input_str), 'etybredoc')
        input_str = 'Hello World and Coders'
        self.assertEqual(FirstReverse(input_str), 'sredoC dna dlroW olleH')
        input_str = 'Fun'
        self.assertEqual(FirstReverse(input_str), 'nuF')


if __name__ == '__main__':
    unittest.main()
