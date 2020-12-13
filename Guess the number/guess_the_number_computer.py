from random import randint


def guess(max_num):
    guess_num = randint(1, max_num)
    user_guess = 0
    while user_guess != guess_num:
        user_guess = int(input(f"Guess a number between 1 and {max_num}: "))
        if user_guess > guess_num:
            print("Please guess a lower number 👎🏽")
        elif user_guess < guess_num:
            print("Please guess a higher number 👍🏽")

    print(f"You guessed correct 🎉 - {user_guess}")


guess(10)