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


class SmartComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    # Minimax function
    def minimax(self, state, player):
        max_player = self.letter  # oursleves
        other_min_player = "o" if player == "x" else "x"  # whatever the other letter is

        # Check if the previous move is a winner
        # Base case
        if state.winner == other_min_player:
            # return position and score in order to keep track of the score for minimax to work
            return {
                "position": None,
                "score": 1 * (state.num_empty_squares() + 1)
                if other_min_player == max_player
                else -1 * (state.num_empty_squares() + 1),
            }
        elif not state.num_empty_squares():
            # no empty squares
            return {
                "position": None,
                "score": 0,
            }

        # Initialize dictionary
        if player == max_player:
            # each score should maximize
            best = {
                "position": None,
                "score": -math.inf,
            }
        else:
            # each score should minimize
            best = {
                "position": None,
                "score": math.inf,
            }

        for possible_move in state.available_moves():
            # 1. make a move, try the spot
            state.make_move(possible_move, player)
            # 2. recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_min_player)
            # 3. undo the move
            state.board[possible_move] = " "
            state.winner = None
            sim_score["position"] = possible_move  # to avoid mess on recurion
            # 4. update the dictionaries if necessary
            if player == max_player:
                # trying to maximize the max_player
                if sim_score["score"] > best["score"]:
                    best = sim_score  # replace best to sim_score
            else:
                # minimize the min_player
                if sim_score["score"] < best["score"]:
                    best = sim_score  # replace best to sim_score

        return best

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # Get random spot from game(passed board) if available moves are 9
            square = random.choice(game.available_moves())
        else:
            # Get move by minimax algorithm
            square = self.minimax(game, self.letter)["position"]
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