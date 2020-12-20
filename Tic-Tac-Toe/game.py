class TicTacToe:
    def __init__(self) -> None:
        # single list to represent 3x3 board
        self.board = [" " for i in range(9)]
        self.winner = None  # keep track of winner

    def print_board(self):
        # getting rows
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            # [1*3 : (1+1) * 3] = board[3:6]
            # [2*3 : (2+1) * 3] = board[6:9]
            # [3*3 : (3+1) * 3] = board[6:12]
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        num_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in num_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
        # * same logic as above in normal for loop
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == " ":
        #         moves.append(i)

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        # if valid move then make the move(assign letter to the square)
        # and return True else return False
        if self.board[square] == " ":
            self.board[square] = letter
            return True

        return False


# Game On
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()

    letter = "x"  # Starting letter
    square = None
    # Iterate while the game still has empty squares
    while game.empty_squares():
        # Get move based on letter
        if letter == "x":
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        # Make move
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print(" ")

            # After the move completes, alternate the letter
            letter = "o" if letter == "x" else "x"  # switch the letter
