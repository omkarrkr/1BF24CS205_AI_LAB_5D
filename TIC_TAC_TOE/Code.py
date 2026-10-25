board = [" "] * 9
winning = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()
def check_winner(player):
    for a, b, c in winning:
        if board[a] == board[b] == board[c] == player:
            return True
    return False
def bot_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "
    if board[4] == " ":
        board[4] = "O"
        return
    for i in [0, 2, 6, 8]:
        if board[i] == " ":
            board[i] = "O"
            return
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return
while True:
    print_board()
    move = int(input("Enter position (1-9): "))-1
    if move < 0 or move >= 9 or board[move] != " ":
        print("Invalid move!")
        continue

    board[move] = "X"
    if check_winner("X"):
        print_board()
        print("Human Wins!")
        break
    if " " not in board:
        print_board()
        print("Draw!")
        break
    bot_move()
    print("Bot played.")
    if check_winner("O"):
        print_board()
        print("Bot Wins!")
        break
    if " " not in board:
        print_board()
        print("Draw!")
        break
