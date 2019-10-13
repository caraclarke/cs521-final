'''
Main file to run the word finder program
'''
import sys
from ScrabbleWords import ScrabbleWords


def main():
    # switch this to be from user and try/except
    user_input = 'aeinpto'
    # 10/14 goal
    # get input from user -> 7 letters
    # try/except to make sure its a string
    # merge into one string and pass to words
    thing = ScrabbleWords(user_input)
    # Display nicely with point values
    print(thing.get_words_list())


if __name__ == '__main__':
    # Run method to start scrabble word finder
    main()
