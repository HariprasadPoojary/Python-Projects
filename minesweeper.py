from random import randint
import re


class Board:
    def __init__(self, dimension, num_bombs) -> None:
        self.dimension = dimension
        self.num_bombs = num_bombs

        # create the board
        self.board = self.make_new_board()  # plant the bombs too
        self.assign_value_to_board()

        # initialize a set to keep track of which locations is uncovered
        # save (row, col) tuples into this set
        self.dug = set()  # e.g. dig at 0,1, then self.dug = {(0,1)}

    def make_new_board(self):
        # new board based on dimension and no. of bombs
        # board is initialized with None values in a list of list based on dimension
        board = [[None for i in range(self.dimension)] for i in range(self.dimension)]
        # sample board representation ↓
        # [
        #     [None, None,....., None],
        #     [None, None,....., None],
        #     [None, None,....., None],
        #     [None, None,....., None]
        # ]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = randint(0, self.dimension ** 2 - 1)
            # e.g dimension = 4 then there would be 16(4²) blocks in the board
            row = loc // self.dimension
            col = loc % self.dimension

            if board[row][col] == "*":
                # we've already planted a bomb here
                continue
            # Plant the bomb
            board[row][col] = "*"
            bombs_planted += 1

        return board

    def __str__(self) -> str:
        visible_board = [
            [None for i in range(self.dimension)] for i in range(self.dimension)
        ]
        for row in range(self.dimension):
            for col in range(self.dimension):
                if (row, col) in self.dug:  # check if user has dug this block
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "

        # put this together in a string
        string_rep = ""
        # get max column widths for printing
        widths = []
        for idx in range(self.dimension):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))

        # print the csv strings
        indices = [i for i in range(self.dimension)]
        indices_row = "   "
        cells = []
        for idx, col in enumerate(indices):
            format = "%-" + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += "  ".join(cells)
        indices_row += "  \n"

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f"{i} |"
            cells = []
            for idx, col in enumerate(row):
                format = "%-" + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += " |".join(cells)
            string_rep += " |\n"

        str_len = int(len(string_rep) / self.dimension)
        string_rep = indices_row + "-" * str_len + "\n" + string_rep + "-" * str_len

        return string_rep

    def assign_value_to_board(self):
        # Assign a number 0-8 for all blocks which are not a bomb, which represents how many neighboring bombs there are.
        for r in range(self.dimension):
            for c in range(self.dimension):
                if self.board[r][c] == "*":  # We don't want to override the bomb
                    continue
                # get neighboring bomb count if the block is not a bomb
                self.board[r][c] = self.get_num_neighbor_bomb_cnt(r, c)

    def get_num_neighbor_bomb_cnt(self, row, col):

        num_neighbor_bombs = 0
        # min and max is used to make sure that values do not go out of bounds
        for r in range(
            max(0, row - 1), min(self.dimension - 1, row + 1) + 1
        ):  # range(below row, above row)
            for c in range(
                max(0, col - 1), min(self.dimension - 1, col + 1) + 1
            ):  # range(left col, right col)
                if r == row and c == col:
                    # our location, no need to check
                    continue
                if self.board[r][c] == "*":
                    num_neighbor_bombs += 1

        return num_neighbor_bombs

    def dig(self, row, col) -> bool:
        # True if successful dig, False if bomb
        # Scenarios:
        # 1. Bomb -> False, Game Over
        # 2. Neighboring bomb -> True, finish dig
        # 3. No Neighboring bomb -> Recurse this function until it finds Neighboring bomb

        self.dug.add((row, col))  # Keep track of what we dug

        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0 -> No Neighboring bomb, check around the block for Neighboring bomb
        # copy the loop code from get_num_neighbor_bomb_cnt()
        for r in range(
            max(0, row - 1), min(self.dimension - 1, row + 1) + 1
        ):  # range(below row, above row)
            for c in range(
                max(0, col - 1), min(self.dimension - 1, col + 1) + 1
            ):  # range(left col, right col)
                if (r, c) in self.dug:
                    # No need to dig where we've already dug
                    continue
                self.dig(r, c)

        # if our initial dig didn't hit a bomb then we shouldn't hit a bomb here
        return True


def play(dimension=10, num_bombs=10):
    # Steps:
    # 1. Create the board and plant the bombs
    # 2. Show the board and ask user where to dig
    # 3a. If the location is a bomb, end game and show message
    # 3b. If the location is not a bomb, dig recursively until each square is atleast next to a bomb
    # 4. Repeat steps 2 and 3a/3b until there is no place to dig and to victory, game ends

    play_board = Board(dimension, num_bombs)
    safe = True

    while len(play_board.dug) < (play_board.dimension ** 2 - num_bombs):
        print(play_board)
        user_input = re.split(
            ",(\\s)*", input("Where would you like to dig? Input -> row,col: ")
        )  # e.g. 2,5
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= dimension or col < 0 or col >= dimension:
            print("Invalid input, please try again!")
            continue

        safe = play_board.dig(row, col)

        if not safe:
            # dug a bomb
            break

    if safe:
        print("You Won!!!")
    else:
        print("Game OVER :( ")
        # Reveal the whole board
        play_board.dug = [(r, c) for r in range(dimension) for c in range(dimension)]
        print(play_board)


if __name__ == "__main__":
    play()