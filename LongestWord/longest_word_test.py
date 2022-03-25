import unittest

from LongestWord.longest_word import LongestWord


class TestLongestWord(unittest.TestCase):

    def test_longest_word(self):
        input_str = 'fun&!! time'
        self.assertEqual(LongestWord(input_str), 'time')
        input_str = 'I love dogs'
        self.assertEqual(LongestWord(input_str), 'dogs')
        input_str = 'Programmers use arrays to store data'
        self.assertEqual(LongestWord(input_str),
                         'Programmers')


if __name__ == '__main__':
    unittest.main()
