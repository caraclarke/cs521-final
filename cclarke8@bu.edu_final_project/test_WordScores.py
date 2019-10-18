# import class to test
from WordScores import WordScores, WORD_SCORES_DICT

# mock dictionary of scores to test mutators
MOCK_SCORES = {'a': 22, 'z': 47}

# Test WordScores Class


class TestWordScores():
    def setup(self):
        self.word_scores = WordScores()

    def test_returns_letter_scores(self):
        assert self.word_scores.get_letter_scores() == WORD_SCORES_DICT

    def test_can_update_letter_scores(self):
        self.word_scores.set_letter_scores(MOCK_SCORES)
        assert self.word_scores.get_letter_scores() == MOCK_SCORES

    def test_get_word_score(self):
        assert self.word_scores.get_word_score(
            'python') == 14  # score for word 'python'
