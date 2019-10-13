from collections import Counter


class ScrabbleWords():
    def __init__(self, user_string):
        # merged string of letters available to user
        self.__user_string = user_string
        self.__counted_string = Counter(user_string)
        self.__words = self.get_words_from_dictionary()

    # Accessors
    def get_user_string(self):
        return self.__user_string

    def get_counted_string(self):
        return self.__counted_string

    def get_words(self):
        return self.__words

    # Mutators
    def set_user_string(self, user_string):
        self.__user_string = user_string

    def set_counted_string(self, counted_string):  # should we be setting this?
        self.__counted_string = counted_string

    def set_words(self, words):
        self.__words = words

    # Description
    # Returns
    def get_words_from_dictionary(self):
        with open('dictionary.txt') as dictionary:
            lines = (word.strip().lower() for word in dictionary)
            # list with word and count of each letter in word
            words = [(word, Counter(word)) for word in lines]
        return words

    # Description: Open word dictionary and find words that use provided letters
    # Returns: list of potential words to be used
    def get_words_list(self):
        # Empty list to return to user
        potential_words = []
        # new_word is a word in self.__words, word_length is the count of each letter in a word
        for new_word, word_length in self.__words:
            # if there is nothing lef after you subtract word_length from the count of user provided letters
            # That is a word our user could use
            # Only return words that use at least two letters so they can be played onto the board
            if len(new_word) >= 2 and not (word_length - self.__counted_string):
                # Add to potential words list to be returned to user
                potential_words.append(new_word)
        # Return list
        return potential_words


def main():
    # switch this to be from user and try/except
    user_input = 'aeinpto'
    # 10/14 goal
    # get input from user -> 7 letters
    # try/except to make sure its a string
    # merge into one string and pass to words
    thing = ScrabbleWords(user_input)
    print(thing.get_words_list())


if __name__ == '__main__':
    # Run method to start scrabble word finder
    main()
