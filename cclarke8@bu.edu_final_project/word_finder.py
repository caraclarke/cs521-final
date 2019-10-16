'''
Main file to run the word finder program
'''
import sys
from ScrabbleWords import ScrabbleWords


def main():
    # switch this to be from user and try/except
    user_input = input('Enter all available letters for your turn: ')
    for value in user_input:
        try:  # Check user didn't enter numbers
            if value.isdigit():
                raise Exception('value is int or float')
        except:  # Exit if another exception occurs
            print("Please enter only letters. Try again")
            sys.exit()
        else:
            user_words = ScrabbleWords(user_input)

    # get potential words from class
    sorted_words = user_words.get_words_list()
    # format nicely and display to user
    for word in sorted_words:
        print("""Suggested word: {}
Potential score: {}
________________________________________
        """.format(*word))


if __name__ == '__main__':
    # Run method to start scrabble word finder
    main()
