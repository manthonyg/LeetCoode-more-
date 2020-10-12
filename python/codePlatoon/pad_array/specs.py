import unittest
from pad_array import pad

class PadArrayTest(unittest.TestCase):

    def test_no_padding_input(self):
        self.assertEqual(pad([1, 2, 3], 5), [1, 2, 3, None, None])

    def test_correct_padding1(self):
        self.assertEqual(pad([1, 2, 3], 5, 'apple'),
                         [1, 2, 3, 'apple', 'apple'])

    def test_size_smaller_than_list(self):
        self.assertEqual(pad([1, 2, 3], 0), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()

