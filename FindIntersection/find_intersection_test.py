import unittest

from FindIntersection.find_intersection import FindIntersection


class TestFindIntersection(unittest.TestCase):

    def test_full_intersection(self):
        input_array = ['-1, 3, 4, 7', '-1, 3, 4, 7']
        self.assertEqual(FindIntersection(input_array), '-1,3,4,7')
        input_array = ['0', '0']
        self.assertEqual(FindIntersection(input_array), '0')
        input_array = ['-100, -50, 0, 50, 100', '-100, -50, 0, 50, 100']
        self.assertEqual(FindIntersection(input_array), '-100,-50,0,50,100')

    def test_intersection(self):
        input_array = ['1, 3, 4, 7, 13', '1, 2, 4, 13, 15']
        self.assertEqual(FindIntersection(input_array), '1,4,13')
        input_array = ['1, 3, 9, 10, 17, 18', '1, 4, 9, 10']
        self.assertEqual(FindIntersection(input_array), '1,9,10')

    def test_no_intersection(self):
        input_array = ['-1, 3, 4, 7', '-10, 2, 5, 8']
        self.assertEqual(FindIntersection(input_array), 'false')
        input_array = ['0', '1']
        self.assertEqual(FindIntersection(input_array), 'false')
        input_array = ['-100, -50, 0, 50, 100', '-10, -5, 5, 10']
        self.assertEqual(FindIntersection(input_array), 'false')


if __name__ == '__main__':
    unittest.main()
