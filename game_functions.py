import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val > current_val:
        r = "h"
    else:
        r = "l"
    if r == user_input:
        return True
    else:
        return False 

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    split_w = list(word)
    guess = False
    for i, l in enumerate(split_w):
        if l.lower() == letter.lower():
            guess = True
            board[i] = letter
    return guess, board
