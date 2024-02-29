import string
import random
from words import words


def get_valid_word(words):
    """
    Get a single word from list of words by random.
    :param words: List of all words.
    :return: String which contains single word.
    """
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

    while word_letters and i < 12:
        # printing current word in blankets
        print('Current word: ')
        for item in word:
            if item in word_letters:
                print('_', end=' ')
            else:
                # if letter is removed from word_letters it means user guessed it right
                print(item, end=' ')

        # user's input
        user_letter = input('\nGuess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used this letter!')
        else:
            print('Invalid character. Please, try again')

        print(f'\nUsed letters: ')
        for item in used_letters:
            print(item, end=' ')

        print(f'\nNumber of tries left: {11 - i}')
        i += 1

    if i == 12:
        print('\nYou lost! The word was: \n')
        for item in word:
            print(item, end=' ')
    else:
        print('You won! The word was: \n')
        for item in word:
            print(item, end=' ')


if __name__ == '__main__':
    hangman()
