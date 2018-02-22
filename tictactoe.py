def print_board(board):
    for row in board:
        print("|".join(row))

def take_turn(player, symbol):
    while True:
        row = int(input("{}, pick row: ".format(player))) - 1
        col = int(input("{}, pick col: ".format(player))) - 1
        if (row in range(3) and
            col in range(3) and
            board[row][col] == "_"):
            break
        print("You cannot choose this field")
    board[row][col] = symbol

def game_won():
    print("Game Over! You've won!")
    print_board(board)

def game_ongoing():
    symbols = ['X', 'O']
    for symbol in symbols:
        # check if rows match
        if [symbol, symbol, symbol] in board:
            game_won()
            return False
        # check if columns match
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == symbol:
                game_won()
                return False
        # indent matches complex logic condition
        if (board[0][0] == board[1][1] == board[2][2] == symbol or
            board[0][2] == board[1][1] == board[2][0] == symbol):
            game_won
            return False
    # if neither matches, game goes on
    return True

turn = 1
board = []

for x in range(0, 3):
    board.append(["_"] * 3)

while game_ongoing():
    print("Turn", turn)
    print_board(board)
    if turn % 2:
        player = "Player 1"
        symbol = "X"
    else:
        player = "Player 2"
        symbol = "O"
    try:
        take_turn(player, symbol)
        turn += 1
        if turn > 9:
            # winning move in 9th turn
            if not game_ongoing():
                break
            print("It's a draw!")
            break
    except (ValueError, SyntaxError, NameError):
        print("You must pick a number")
