from collections import Counter


class ScrabbleWords():
    def __init__(self, l_one, l_two, l_three, l_four, l_five, l_six, l_seven):
        # you can have up to seven letters per user
        self.__l_one = l_one
        self.__l_two = l_two
        self.__l_three = l_three
        self.__l_four = l_four
        self.__l_five = l_five
        self.__l_six = l_six
        self.__l_seven = l_seven
        self.__lines, self.__words = self.create_lines_from_dictionary()

    # Accessors
    def get_l_one(self):
        return self.__l_one

    def get_l_two(self):
        return self.__l_two

    def get_l_three(self):
        return self.__l_three

    def get_l_four(self):
        return self.__l_four

    def get_l_five(self):
        return self.__l_five

    def get_l_six(self):
        return self.__l_six

    def get_l_seven(self):
        return self.__l_seven

    def get_lines(self):
        return self.__lines

    def get_words(self):
        return self.__words

    # Mutators
    def set_l_one(self, l_one):
        self.__l_one = l_one

    def set_l_two(self, l_two):
        self.__l_two = l_two

    def set_l_three(self, l_three):
        self.__l_three = l_three

    def set_l_four(self, l_four):
        self.__l_four = l_four

    def set_l_five(self, l_five):
        self.__l_five = l_five

    def set_l_six(self, l_six):
        self.__l_six = l_six

    def set_l_seven(self, l_seven):
        self.__l_seven = l_seven

    def set_lines(self, lines):
        self.__lines = lines

    def set_words(self, words):
        self.__words = words

    # Description
    # Returns
    def create_lines_from_dictionary(self):
        with open('words_alpha.txt') as dictionary:
            lines = (word.strip().lower() for word in dictionary)
            words = [(word, Counter(word)) for word in lines]
        return lines, words

    # Description: Open word dictionary and find words that use provided letters
    # Returns: list of potential words to be used
    def get_words_list(self):
        print('dude')


def main():
    thing = ScrabbleWords('a', 'b', 'c', 'd', 'e', 'f', 'g')
    print(thing)


main()
