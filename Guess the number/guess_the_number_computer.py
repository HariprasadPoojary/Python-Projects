from random import randint


def guess(num_limit):
    print(
        f"I will guess the number within range 1 to {num_limit}. \
    Please help me by letting me know if the guessed number is Higher(h) or Lower(l) or Correct(c)"
    )
    high = num_limit
    low = 1
    feedback = ""
    while feedback != "c":
        guess = randint(low, high)
        feedback = input(f"Is {guess} too high(h), too low(l) or correct(c)?? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Hurray! I guessed your number 💪🏽")


guess(10)