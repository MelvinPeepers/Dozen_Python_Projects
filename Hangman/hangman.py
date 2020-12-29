import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    # keeps iterating until it's not true, to find a word that is valid a word that doesn't have a space or dash in it
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    # keep track of words and keep track of letters we've guessed and what is a valid letter
    word = get_valid_word(words)
    word_letters = set(word) # saves all the letters in a word as a set
    alphabet = set(string.ascii_uppercase) # predetermined list of letters of the alphabet
    used_letters = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # turns into a string ' '.join(['a', 'b', 'cd']) -> 'a b cd'
        print('Welcome to Hangman. In this game, you have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        # if this is a valid letter in the alphabet, going to add it to my user_letter
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # if letter is in word letter then remove
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # takes away a life if wrong
                print(user_letter, 'is not in word.')
        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letter) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word, '.')
    else:
        print('You guessed the word', word, '!!')


hangman()