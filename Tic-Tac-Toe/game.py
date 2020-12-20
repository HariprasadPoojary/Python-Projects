from player import HumanPlayer, RandomComputerPlayer


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

    def check_winner(self, square, letter):
        # winner is 3 in a row or column or diagnol

        # * check rows
        row_ind = square // 3  # Get the row index
        # Get the whole row with values
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        # Check if all the values in a row has same value
        if all([spot == letter for spot in row]):
            return True

        # * check columns
        col_ind = square % 3  # Get the column index
        # Get the whole column with values
        col = [self.board[col_ind + i * 3] for i in range(3)]
        # Check if all the values in a column has same value
        if all([spot == letter for spot in col]):
            return True

        # * check diagonal
        # only possible move to win a diagonal is with a
        # square with even number(0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal_1]):
                return True
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_2]):
                return True

        # No winner
        return False

    def make_move(self, square, letter):
        # if valid move then make the move(assign letter to the square)
        # and return True else return False
        if self.board[square] == " ":
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.winner = letter
            return True

        return False


# Game On
def play(game, x_player, o_player, print_game=True):
    # Returns winner of the game('x' or 'o') or None(tie)
    if print_game:
        game.print_board_nums()

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

            if game.winner:  # check if winner is not None(if someone won)
                if print_game:
                    print(f"{letter} wins!")
                    return letter

            # After the move completes, alternate the letter
            letter = "o" if letter == "x" else "x"  # switch the letter

    # if no empty squares and winner is None, It's a tie
    if game.winner is None:
        print("It's a Tie!")
        return None


if __name__ == "__main__":
    x_player = HumanPlayer("x")
    o_player = RandomComputerPlayer("o")
    t = TicTacToe()
    play(t, x_player, o_player, True)
