import random
from words import words

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # get user input
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
      

user_input = input('Type something')
print(user_input)