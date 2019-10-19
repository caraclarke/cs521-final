'''
Main file to run the word finder program
'''
import sys
from ScrabbleWords import ScrabbleWords

'''
Description: Prints list of words out for user
Returns: None
'''
def print_words(words):
    for word in words:
        print(
            "Suggested word: {: >10} | Potential score: {: >10}".format(*word))


'''
Description: Gets user input for letters and checks for potential matches
index: current player, default 1
Returns: List of potential words
'''
def play_round(index=1):
    user_input = input(
        'Player {}, Enter all available letters for your turn: '.format(index))
    for value in user_input:
        try:  # Check user didn't enter numbers
            if value.isdigit(): # raise an exception if they did
                raise Exception('value is int or float')
        except:  # Exit if an exception occurs
            print("Please enter only letters. Try again")
            sys.exit()
        else: # Otherwise get the words from ScrabbleWords
            user_words = ScrabbleWords(user_input)
            return user_words


'''
Description: Starts function to allow user to input letters
Returns: Formatted list of suggested words and scores
'''
def main():
    player_input = input("How many players are playing today? ")
    try:
        player_count = int(player_input)
    except ValueError: # if they dont enter a number show error and exit
        print("Please enter only numbers. Try again.")
        sys.exit()
    except: # something else went wrong, show generic error and exit
        print("Something went wrong. Try again.")
        sys.exit()

    # Loop through players if more than one
    if (player_count > 1):
        for player, index in enumerate(range(player_count)):
            # Start at player 1 not player 0
            user_words = play_round(index + 1)
            # get potential words from class
            sorted_words = user_words.get_words_list()
            # format nicely and display to user
            print_words(sorted_words)
    else:
        user_words = play_round()
        # get potential words from class
        sorted_words = user_words.get_words_list()
        # format nicely and display to user
        print_words(sorted_words)


if __name__ == '__main__':
    # Run method to start scrabble word finder
    main()
