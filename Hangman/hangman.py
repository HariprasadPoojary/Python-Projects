from pathlib import Path
from random import choice
import string

BASE_DIR = Path(__file__).resolve().parent
# Get words from file
def load_words():
    with open(f"{BASE_DIR}\words.txt", "r") as file:
        words = file.readlines()
    return words


def get_valid_word():
    words = load_words()
    word = choice(words)
    while "-" in word or " " in word:
        print(word)
        word = choice(words)
    return word.upper().removesuffix(
        "\n"
    )  # return word by removing new line at the end


def hangman():
    # Get a word
    word = get_valid_word()
    # Data setup
    word_letters = set(word)  # All letters of the word in a set - unordered
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    # letter from user
    user_letter = input("Guess a letter: ").upper()

    # Logic


hangman()
