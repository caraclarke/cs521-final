from collections import Counter
from WordScores import WordScores


# Class for taking user string and returning list of potential words/their scores
# Inherits from WordScores Class
class ScrabbleWords(WordScores):
    def __init__(self, user_string):
        super().__init__()
        # merged string of letters available to user
        self.user_string = user_string
        # count of occurance of each letter in provided string
        self.counted_string = Counter(user_string)
        # words available from dictionary file
        self.__words = self.__get_words_from_dictionary()

    # Accessors
    def get_user_string(self):
        return self.user_string

    def get_counted_string(self):
        return self.counted_string

    def get_words(self):
        return self.__words

    # Mutators
    def set_user_string(self, user_string):
        self.user_string = user_string

    def set_counted_string(self, counted_string):
        self.counted_string = counted_string

    def set_words(self, words):
        self.__words = words

    '''
    Description: override repr to return letter count of user provided string
    Returns: count of letters provided by user
    '''
    def __repr__(self):
        return repr(self.counted_string)

    '''
    Description: read txt file and create word dictionary
    Returns list with tuple containing word and count of each letter in word
    '''
    def __get_words_from_dictionary(self):
        # Depending on the input getting the suggested word can take a while
        # Show message to let user know something is happening
        print("We're thinking...")
        # dictionary.txt contains Collins Scrabble Words (2019)
        with open('dictionary.txt') as dictionary:
            lines = (word.strip().lower() for word in dictionary)
            # list with word and count of each letter in word
            words = [(word, Counter(word)) for word in lines]
        return words

    '''
    Description: Open word dictionary and find words that use provided letters
    Returns: list of potential words to be used
    '''
    def get_words_list(self):
        # Empty list
        potential_words = []
        # new_word is a word in self.__words, word_length is the count of each letter in a word
        for new_word, word_length in self.__words:
            # If the suggested word is at least 2 letters (so it can be played on the board)
            # and if there is nothing left after you subtract word_length from the count of user provided letters
            if len(new_word) >= 2 and not (word_length - self.counted_string):
                word_score = self.get_word_score(new_word)
                # Add tuple with word and score to list to be returned
                potential_words.append((new_word, word_score))
        # sort list by low -> high scores and return
        return sorted(potential_words, key=lambda score: score[1])
