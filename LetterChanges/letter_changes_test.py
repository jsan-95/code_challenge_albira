import unittest

from LetterChanges.letter_changes import LetterChanges


class TestLetterChanges(unittest.TestCase):

    def test_letter_changes(self):
        input_str = 'hello*3'
        self.assertEqual(LetterChanges(input_str), 'Ifmmp*3')
        input_str = 'fun times!'
        self.assertEqual(LetterChanges(input_str), 'gvO Ujnft!')
        input_str = 'abc45defghijklmnopqrstuvw?? xyz'
        self.assertEqual(LetterChanges(input_str),
                         'bcd45EfghIjklmnOpqrstUvwx?? yzA')
        input_str = 'abcdefghijklmnopqrstuvwxyz'
        self.assertEqual(LetterChanges(input_str),
                         'bcdEfghIjklmnOpqrstUvwxyzA')

    def test_error_letter_changes(self):
        input_str = 'hello*3'
        self.assertIsNot(LetterChanges(input_str), 'ifmmp*3')
        input_str = 'fun times!'
        self.assertIsNot(LetterChanges(input_str), 'gvo Ujnft!')
        input_str = 'abc45defghijklmnopqrstuvw?? xyz'
        self.assertIsNot(LetterChanges(input_str),
                         'bcdEfghIjklmnOpqrstUvwxyzA')
        input_str = 'abcdefghijklmnopqrstuvwxyz'
        self.assertIsNot(LetterChanges(input_str),
                         'bcdefghIjklmnOpqrstUvwxyzA')


if __name__ == '__main__':
    unittest.main()
