from pathlib import Path
from random import choice
import string

BASE_DIR = Path(__file__).resolve().parent
# Get words from file
def load_words():
    with open(f"{BASE_DIR}\words.txt", "r") as file:
        words = file.readlines()
    return words


def get_valid_word() -> str:
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
    lives = ["✿", "✿", "✿", "✿", "✿", "✿"]

    while len(word_letters) > 0 and len(lives) > 0:
        # Print used letter
        print("You have used these letters: " + " ".join(used_letters))

        # print lives
        print("Lives left: " + " ".join(lives))

        # Show letter which is to be guessed '-' with already guessed letters
        curr_guess_letters = [
            letter if letter in used_letters else "-" for letter in word
        ]
        print("Current Guessed Letters: " + " ".join(curr_guess_letters))

        # letter from user
        user_letter = input("Guess a letter: ").upper()

        # Logic
        if (
            # Check if the letter given by user is used yet
            user_letter
            in alphabet - used_letters
        ):

            # Add the letter to the set
            used_letters.add(user_letter)
            if (
                # Check if letter given by user is there in word letters
                user_letter
                in word_letters
            ):
                # Remove the letter from word letters
                word_letters.remove(user_letter)
            else:
                lives.pop()
        elif user_letter in used_letters:  # Letter already used!
            print("You have already used this letter.")
            lives.pop()
        else:
            print("You typed wrong character.")
            lives.pop()

    # Gets here when lives = 0 or word is guessed correctly
    if len(lives) == 0:
        print(f"Sorry you're of lives, the word was {word}")
    else:
        print(f"Yeah!!!! you guessed {word} correctly")


hangman()
