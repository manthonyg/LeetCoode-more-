import unittest
from optimal_change import ChangeMaker

class ChangeMakerTestCase(unittest.TestCase):
    def test_returns_correct_change_string(self):
        change_maker1 = ChangeMaker(62.13, 100)
        change_string = change_maker1.optimal_change()
        expected_string = "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
        self.assertEqual(change_string, expected_string)

    def test_returns_correct_change_string2(self):
        change_maker2 = ChangeMaker(31.51, 50)
        change_string = change_maker2.optimal_change()
        expected_string = "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
        self.assertEqual(change_string, expected_string)

if __name__ == '__main__':
    unittest.main()


