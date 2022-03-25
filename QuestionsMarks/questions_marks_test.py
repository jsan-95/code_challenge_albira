import unittest

from QuestionsMarks.questions_marks import QuestionsMarks


class TestQuestionsMarks(unittest.TestCase):

    def test_correct_questions_marks(self):
        input_str = 'arrb7????5xxbl6????eee6'
        self.assertTrue(QuestionsMarks(input_str))
        input_str = 'acc?8???sss?4rr1??????5'
        self.assertTrue(QuestionsMarks(input_str))
        input_str = '????asd4???sss?8rr1???5'
        self.assertTrue(QuestionsMarks(input_str))

    def test_error_questions_marks(self):
        input_str = 'arrb7??????5xxbl6??????eee6'
        self.assertFalse(QuestionsMarks(input_str))
        input_str = 'acc?8???sss4rr1??????5'
        self.assertFalse(QuestionsMarks(input_str))
        input_str = '????asd4?????sss?8rr1???5'
        self.assertFalse(QuestionsMarks(input_str))
        input_str = '????asd4???sss?7rr1???5'
        self.assertFalse(QuestionsMarks(input_str))


if __name__ == '__main__':
    unittest.main()
