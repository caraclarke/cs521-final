import unittest
from collections import Counter
from ScrabbleWords import ScrabbleWords

# list of words suggested from test string 'python'
WORDS_FROM_PYTHON = [('to', 2),
                     ('on', 2),
                     ('no', 2),
                     ('nt', 2),
                     ('tn', 2),
                     ('ot', 2),
                     ('not', 3),
                     ('ton', 3),
                     ('po', 4),
                     ('op', 4),
                     ('pt', 4),
                     ('np', 4),
                     ('tp', 4),
                     ('pn', 4),
                     ('top', 5),
                     ('oh', 5),
                     ('ny', 5),
                     ('th', 5),
                     ('nh', 5),
                     ('pot', 5),
                     ('ho', 5),
                     ('opt', 5),
                     ('yo', 5),
                     ('yn', 5),
                     ('ht', 5),
                     ('ty', 5),
                     ('hot', 6),
                     ('toy', 6),
                     ('hon', 6),
                     ('hp', 7),
                     ('tony', 7),
                     ('ph', 7),
                     ('hop', 8),
                     ('pty', 8),
                     ('thy', 9),
                     ('python', 14)]

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

    def test_get_words_list(self):
        self.scrabble_word = ScrabbleWords('python')
        suggested_words = self.scrabble_word.get_words_list()
        self.assertEqual(suggested_words, WORDS_FROM_PYTHON)


if __name__ == '__main__':
    unittest.main()
