from random import choice


def play():
    # Get inputs
    user = input("'r' for Rock, 'p' for Paper, 's' for Scissor \n")
    computer = choice(["r", "p", "s"])

    # Print Both
    print(f"User chose {user} and Computer chose {computer}")

    # if both choices are same
    if user == computer:
        return "It's a tie!"
    # if user wins
    if is_win(user, computer):
        return "You Won!!"

    return "You Lost"


# Rules --> r > s, p > r, s > p
def is_win(player, opponent) -> bool:
    if (
        (player == "r" and opponent == "s")
        or (player == "p" and opponent == "r")
        or (player == "s" and opponent == "p")
    ):
        return True


print(play())