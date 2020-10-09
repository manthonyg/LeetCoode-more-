import unittest  # imports the Unit Test library
# import the fizzbuzz method from fizzbuzz.py
from product_sort import product_sort


class ProductSortCase(unittest.TestCase):
    """Tests for `product_sort.py`."""

    def test_returns_a_list(self):
        self.assertEqual(type(product_sort([8,8,5,5,5,5,1,1,1,4,4])), list)


if __name__ == '__main__':
    unittest.main()
