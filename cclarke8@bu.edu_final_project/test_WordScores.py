import unittest
from WordScores import WordScores, WORD_SCORES_DICT

# mock dictionary of scores to test mutators
MOCK_SCORES = {'a': 22, 'z': 47}

# Test WordScores Class
class TestWordScores(unittest.TestCase):
    def test_get_letter_scores(self):
        self.word_scores = WordScores()
        scores = self.word_scores.get_letter_scores()
        self.assertEqual(scores, WORD_SCORES_DICT)

    def test_set_letter_scores(self):
        self.word_scores = WordScores()
        self.word_scores.set_letter_scores(MOCK_SCORES)
        new_scores = self.word_scores.get_letter_scores()
        self.assertEqual(new_scores, MOCK_SCORES)

    def test__repr__(self):
        self.word_scores = WordScores()
        test_repr = self.word_scores.__repr__()
        self.assertEqual(test_repr, str(WORD_SCORES_DICT))

    def test_get_word_score(self):
        self.word_scores = WordScores()
        test_word_score = self.word_scores.get_word_score('python')
        self.assertEqual(test_word_score, 14)  # score for word 'python'


if __name__ == '__main__':
    unittest.main()
