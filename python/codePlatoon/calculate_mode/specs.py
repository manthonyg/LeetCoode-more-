import unittest
from calculate_mode import calculate_mode

class CalculateModeTestCase(unittest.TestCase):
    def test_returns_a_correct_list(self):
        self.assertEqual(calculate_mode([1, 2, 3, 3]),[3])

    def test_returns_a_correct_list2(self):
        self.assertEqual(calculate_mode([1, 1, 2, 2]), [1,2])
    
    def test_returns_a_correct_list3(self):
        self.assertEqual(calculate_mode(["who", "what", "where", "who"]),['who'])

    def test_returns_a_correct_list4(self):
        self.assertEqual(calculate_mode([1, 2, 3]), [1, 2, 3])
    


if __name__ == '__main__':
    unittest.main()
    

