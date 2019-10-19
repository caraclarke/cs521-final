import unittest
from collections import Counter
from ScrabbleWords import ScrabbleWords

'''
Description: Helper function to get words from dictionary file
Returns: words from dictionary.txt
'''


def get_dictionary_helper():
    with open('dictionary.txt') as dictionary:
        lines = (word.strip().lower() for word in dictionary)
        # list with word and count of each letter in word
        words = [(word, Counter(word)) for word in lines]
    return words

# Test ScrabbleWords Class


class TestScrabbleWords(unittest.TestCase):
    def test_get_user_string(self):
        self.scrabble_word = ScrabbleWords('python')
        word = self.scrabble_word.get_user_string()
        self.assertEqual(word, 'python')

    def test_get_counted_string(self):
        self.scrabble_word = ScrabbleWords('pythooon')
        word = self.scrabble_word.get_counted_string()
        self.assertEqual(
            word, {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 3, 'n': 1})

    def test_get_words(self):
        self.scrabble_word = ScrabbleWords('python')
        words = self.scrabble_word.get_words()
        words_from_file = get_dictionary_helper()
        self.assertEqual(words, words_from_file)

    def test_set_user_string(self):
        self.scrabble_word = ScrabbleWords('python')
        self.scrabble_word.set_user_string('anewstringwow')
        new_word = self.scrabble_word.get_user_string()
        self.assertEqual(new_word, 'anewstringwow')

    def test_set_counted_string(self):
        self.scrabble_word = ScrabbleWords('python')
        self.scrabble_word.set_counted_string({'a': 3, 'e': 3, 'i': 3})
        new_count = self.scrabble_word.get_counted_string()
        self.assertEqual(new_count, {'a': 3, 'e': 3, 'i': 3})

    def test_set_words(self):
        self.scrabble_word = ScrabbleWords('python')
        self.scrabble_word.set_words('old mcdonald had a farm')
        new_words = self.scrabble_word.get_words()
        self.assertEqual(new_words, 'old mcdonald had a farm')

    def test__repr__(self):
        self.scrabble_word = ScrabbleWords('python')
        test_repr = self.scrabble_word.__repr__()
        test_counter = Counter('python')
        self.assertEqual(test_repr, str(test_counter))


if __name__ == '__main__':
    unittest.main()
