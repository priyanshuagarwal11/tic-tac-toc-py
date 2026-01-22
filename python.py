board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_win(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],   # rows
        [0,3,6],[1,4,7],[2,5,8],   # columns
        [0,4,8],[2,4,6]            # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def check_draw():
    return " " not in board

current_player = "X"

while True:
    print_board()
    move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

    if board[move] != " ":
        print("❌ Position already taken!")
        continue

    board[move] = current_player

    if check_win(current_player):
        print_board()
        print(f"🎉 Player {current_player} wins!")
        break

    if check_draw():
        print_board()
        print("😐 It's a Draw!")
        break

    current_player = "O" if current_player == "X" else "X"
