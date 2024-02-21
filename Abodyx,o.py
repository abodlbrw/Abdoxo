#Welcome, dear users
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != ' ':
            return board[0][col]

    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != ' ':
        return board[0][0]

    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != ' ':
        return board[0][2]

    return None

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        print("Player", player, "turn")

        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print("Player", winner, "wins!")
                break

            player = 'O' if player == 'X' else 'X'
        else:
            print("That spot is already taken. Try again.")

if name == "main":
    main()