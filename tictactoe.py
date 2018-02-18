board = []

for x in range(0, 3):
    board.append(["|_|"] * 3)

def print_board(board):
    for row in board:
        print("".join(row))

def take_turn(player, symbol):
    while True:
        row = int(input("{}, pick row: ".format(player))) - 1
        col = int(input("{}, pick col: ".format(player))) - 1
        if (row in range(3) and
            col in range(3) and
            board[row][col] == "|_|"):
            break
        print("You cannot choose this field")
    board[row][col] = symbol

def game_ongoing():
    if (["|X|", "|X|", "|X|"] not in board and
        ["|O|", "|O|", "|O|"] not in board):
        return True
    print("Game Over! You've won!")
    print_board(board)

turn = 1
while game_ongoing():
    print("Turn", turn)
    print_board(board)
    if turn % 2:
        player = "Player 1"
        symbol = "|X|"
    else:
        player = "Player 2"
        symbol = "|O|"
    try:
        take_turn(player, symbol)
        turn += 1
    except ValueError:
        print("You must pick a number")
