#print board
board = []

for x in range(0, 3):
    board.append(["| |"] * 3)

def print_board(board):
    for row in board:
        print(" ".join(row))

for turn in range(4):
    print "Turn", turn + 1
    p1_row = int(raw_input("Row: ")) - 1
    p1_col = int(raw_input("Col: ")) - 1
    board[p1_row1][p1_col1] = "X"
    p2_row = int(raw_input("Row: ")) - 1
    p2_col = int(raw_input("Col: ")) - 1
    board[p2_row1][p2_col1] = "O"


    if
        print "Congratulations! You sank my battleship!"
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        elif elif board[][] == "X" or "O" ::
            print( "This field is already taken" )
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if (turn == 3):
            print "Game Over"
        print_board(board)
