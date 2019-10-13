'''
Main file to run the word finder program
'''
import sys
from ScrabbleWords import ScrabbleWords

# Prompt user to enter their scrabble letters
# Match letters to point values
# Obtain potential words from letters and return to user
# Next to words show point raiting
# Order words by highest point rating

# Have user input what word they chose, update their score
# Can have up to 4 users playing (nice to have unlimited)
# Cycle through endlessly until they choose 'game over'
# Can skip users turn if they dont want to use word finder and just update their scores


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
