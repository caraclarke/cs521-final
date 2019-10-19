# Dictionary of available letters: their scrabble score
WORD_SCORES_DICT = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2,
                    "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3,
                    "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1,
                    "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}

# Class for storing score/letter and calculating score/word
class WordScores():
    def __init__(self):
        self.__LETTER_SCORES = WORD_SCORES_DICT

    # Accessors
    def get_letter_scores(self):
        return self.__LETTER_SCORES

    # Mutators
    def set_letter_scores(self, letter_scores):
        self.__LETTER_SCORES = letter_scores

    '''
    Description: override repr to return letter scores
    Returns: dictionary of with key value letter/score
    '''
    def __repr__(self):
        return repr(self.__LETTER_SCORES)

    '''
    Description: Pass in word and get potential score
    word: string to iterate through
    Returns: numeric score for word
    '''
    def get_word_score(self, word):
        # word score starts at 0
        total = 0
        for letter in word:
            total += self.__LETTER_SCORES[letter]
        # Return total word score
        return total
