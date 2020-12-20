# set up board
board = [" " for i in range(9)]

# print empty board
for row in [board[i * 3 : (i + 1) * 3] for i in range(3)]:
    # [1*3 : (1+1) * 3] = board[3:6]
    # [2*3 : (2+1) * 3] = board[6:9]
    # [3*3 : (3+1) * 3] = board[6:12]
    print("| " + " | ".join(row) + " |")

# set values
num_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
board_num = []
for j in range(3):
    for i in range(j * 3, (j + 1) * 3):
        board_num.append(str(i))
