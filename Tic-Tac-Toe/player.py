import math, random
from time import sleep

class Player:
    def __init__(self, letter) -> None:
        # letter can be x or o
        self.letter = letter

    # Want all palyers to get thier next move given a game
    def get_move(self, game) -> None:
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game) -> None:
        # Get random spot from game(passed board)
        square = random.choice(game.available_moves())
        sleep(0.9)
        return square


class HumanPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game) -> None:
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move(0-9): ")
            # Check if the entered value is correct by doing a type cast
            # Check if entered value is valid - available_moves()
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                else:
                    valid_square = True
            except ValueError as err:
                print("Invalid square. Try again!")

        return val