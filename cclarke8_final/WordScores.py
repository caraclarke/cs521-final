class WordScores():
    def __init__(self, word):
        self.__word = word
        self.__LETTER_SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                                "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                                "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                                "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                                "x": 8, "z": 10}

    # Accessors
    def get_word(self):
        return self.__word

    def get_letter_scores(self):
        return self.__LETTER_SCORES

    # Mutators
    def set_word(self, word):
        self.__word = word

    def set_letter_scores(self, letter_scores):
        self.__LETTER_SCORES = letter_scores

    # Description: Pass in word and get potential score
    # Returns: numeric score for word
    def get_word_score(self, word):
        # word score starts at 0
        total = 0
        for letter in word:
            total += self.__LETTER_SCORES[letter]
        # Return total word score
        return total
