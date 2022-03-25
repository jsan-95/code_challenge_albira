import unittest

from AlphabetSoup.alphabet_soup import AlphabetSoup


class TestAlphabetSoup(unittest.TestCase):

    def test_alphabet_soup(self):
        input_str = 'coderbyte'
        self.assertEqual(AlphabetSoup(input_str), 'bcdeeorty')
        input_str = 'hello'
        self.assertEqual(AlphabetSoup(input_str), 'ehllo')
        input_str = 'hooplah'
        self.assertEqual(AlphabetSoup(input_str), 'ahhloop')
        input_str = 'zyxwvutsrqponmlkjihgfedcba'
        self.assertEqual(AlphabetSoup(input_str), 'abcdefghijklmnopqrstuvwxyz')


if __name__ == '__main__':
    unittest.main()
