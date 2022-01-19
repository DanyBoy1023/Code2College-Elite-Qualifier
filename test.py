import unittest
from main import suggest
from main import load_words

class TestSuggestMethod(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(suggest('soemthin', load_words()), 'something')

if __name__ == '__main__':
  unittest.main()