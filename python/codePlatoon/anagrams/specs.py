import unittest
from anagrams import anagrams_for
list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

class AnagramsTestCase(unittest.TestCase):

    def test_returns_correct(self):
        self.assertEqual(anagrams_for("threads", list_of_words),["threads", "trashed", "hardest", "hatreds"])
    def test_returns_empty(self):
        self.assertEqual(anagrams_for("apple", list_of_words),[])



if __name__ == '__main__':
    unittest.main()
