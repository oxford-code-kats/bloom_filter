import unittest

from bloom import BloomFilter

class TestBloom(unittest.TestCase):
    
    def test_empty_filter(self):
        filter = BloomFilter(10)
        self.assertNotIn('word', filter)

    def test_item_in_filter(self):
        word = "dog"
        filter = BloomFilter(10)
        filter.add(word)
        self.assertIn(word, filter)