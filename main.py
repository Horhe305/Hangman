import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    i = 0

    # user's input
    while word_letters or i < 12:
        user_letter = input('\nGuess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used this letter!')
        else:
            print('Invalid character. Please, try again')

        print('Current word: ')
        for item in word:
            if item in word_letters:
                print('_', end=' ')
            else:
                print(item, end=' ')

        print(f'\nUsed letters: ')
        for item in used_letters:
            print(item, end=' ')

        print(f'\nNumber of tries left: {11 - i}')
        i += 1

    if i == 12:
        print('\nYou lost!')
    else:
        print('You won! The word was: \n')
        for item in word:
            print(item, end=' ')


hangman()
