from collections import Counter


class ScrabbleWords():
    def __init__(self, user_string):
        # merged string of letters available to user
        self.__user_string = user_string
        self.__words = self.get_words_from_dictionary()

    # Accessors
    def get_user_string(self):
        return self.__user_string

    def get_words(self):
        return self.__words

    # Mutators
    def set_user_string(self, user_string):
        self.__user_string = user_string

    def set_words(self, words):
        self.__words = words

    # Description
    # Returns
    def get_words_from_dictionary(self):
        with open('words_alpha.txt') as dictionary:
            lines = (word.strip().lower() for word in dictionary)
            # list with word and count of each letter in word
            words = [(word, Counter(word)) for word in lines]
        return words

    # Description: Open word dictionary and find words that use provided letters
    # Returns: list of potential words to be used
    def get_words_list(self):
        print('dude')


def main():
    # switch this to be from user and try/except
    user_input = 'aeinpto'
    thing = ScrabbleWords(user_input)
    print(thing)


main()
