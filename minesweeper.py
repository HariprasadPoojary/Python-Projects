from random import randint


class Board:
    def __init__(self, dimension, num_bombs) -> None:
        self.dimension = dimension
        self.num_bombs = num_bombs

        # create the board
        self.board = self.make_new_board()  # plant the bombs too

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


def play(dimension=10, num_bombs=10):
    # Steps:
    # 1. Create the board and plant the bombs
    # 2. Show the board and ask user where to dig
    # 3a. If the location is a bomb, end game and show message
    # 3b. If the location is not a bomb, dig recursively until each square is atleast next to a bomb
    # 4. Repeat steps 2 and 3a/3b until there is no place to dig and to victory, game ends
    b = Board(4, 5)
    print(b.board)

play()