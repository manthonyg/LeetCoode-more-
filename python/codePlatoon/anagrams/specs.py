import unittest
from anagrams import anagrams_for
list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]
class AnagramsTest(unittest.TestCase):
    def return_correct_anagramsList(self):
        self.assertEqual(anagrams_for("threads", list_of_words), [
                         "threads", "trashed", "hardest", "hatreds"])
    def return_empty(self):
        self.assertEqual(anagrams_for("apple", list_of_words), [])
