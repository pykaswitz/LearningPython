def main():
    print()
    print("Welcome to Connect Four")
    print()

    # CREATE THE BOARD
    # Board is a list of columns
    # Columns are a list of cells
    board = [
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
    ]

    # CHOSE INITIAL PLAYER
    active_player_index = 0
    players = ["\033[1;30;41mBrian\033[0m", "\033[1;30;43mComputer\033[0m"]
    symbols = ["R", "Y"]
    player = players[active_player_index]

    # ADD COLOR TO PLAYER PIECES
    # print("\033[1;30;41m O \033[0m")  # Bold, White on Red Background
    # print("\033[1;30;43m O \033[0m")  # Bold, White on Yellow Background

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} has won with the board: ")
    show_board(board)
    print()


def show_board(board):
    red_begin = '\033[1;30;41m'
    yellow_begin = '\033[1;30;43m'
    color_end = '\033[0m'

    i = 0
    while i < len(board[0]):
        print("| ", end='')
        for cell in board:
            if cell[i] is None:
                cell[i] = "_"
                print(cell[i], end=' | ')
            elif cell[i] == "R":
                print(red_begin + cell[i] + color_end, end=' | ')
            elif cell[i] == "Y":
                print(yellow_begin + cell[i] + color_end, end=' | ')
            else:
                print(cell[i], end=' | ')
        i += 1
        print()
    print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn.")
    print()


# Select column and updates next available space, returns error if column is full
def choose_location(board, symbol):
    col = int(input("Choose which column: "))
    col -= 1
    row = -1
    for col_cell in board[col]:
        if col_cell == "_":
            row += 1

    if row > -1:
        board[col][row] = symbol
        return True
    else:
        return False


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 == "_":
            continue
        elif symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(board):
    sequences = []

    # WIN BY ROWS
    row_counter = 0  # Create 3 step loop to create blocks of 4 rows in all variations
    while row_counter < 4:
        for row_idx in range(0, 6):
            row = [
                board[(0 + row_counter)][row_idx],
                board[(1 + row_counter)][row_idx],
                board[(2 + row_counter)][row_idx],
                board[(3 + row_counter)][row_idx],
            ]

            sequences.append(row)
        row_counter += 1

    # WIN BY COLUMNS
    col_counter = 0  # Create 3 step loop to create blocks of 4 columns in all variations
    while col_counter < 3:
        for row_idx in range(0, 7):
            row = [
                board[row_idx][(0 + col_counter)],
                board[row_idx][(1 + col_counter)],
                board[row_idx][(2 + col_counter)],
                board[row_idx][(3 + col_counter)],
            ]

            sequences.append(row)
        col_counter += 1

    # WIN BY DIAGONALS
    diagonals = [
        [board[0][0], board[1][1], board[2][2], board[3][3]],
        [board[0][1], board[1][2], board[2][3], board[3][4]],
        [board[0][2], board[1][3], board[2][4], board[3][5]],
        [board[0][3], board[1][2], board[2][1], board[3][0]],
        [board[0][4], board[1][3], board[2][2], board[3][1]],
        [board[0][5], board[1][4], board[2][3], board[3][2]],
        [board[1][5], board[2][4], board[3][3], board[4][2]],
        [board[2][5], board[3][4], board[4][3], board[5][2]],
        [board[3][5], board[4][4], board[5][3], board[6][2]],
        [board[1][0], board[2][1], board[3][2], board[4][3]],
        [board[2][0], board[3][1], board[4][2], board[5][3]],
        [board[3][0], board[4][1], board[5][2], board[6][3]],
        [board[1][1], board[2][2], board[3][3], board[4][4]],
        [board[1][2], board[2][3], board[3][4], board[4][5]],
        [board[2][1], board[3][2], board[4][3], board[5][4]],
        [board[3][1], board[4][2], board[5][3], board[6][4]],
        [board[2][2], board[3][3], board[4][4], board[5][5]],
        [board[3][2], board[4][3], board[5][4], board[6][5]],
        [board[4][0], board[3][1], board[2][2], board[1][3]],
        [board[5][0], board[4][1], board[3][2], board[2][3]],
        [board[1][4], board[2][3], board[3][2], board[4][1]],
        [board[2][4], board[3][3], board[4][2], board[5][1]],
        [board[3][3], board[4][2], board[5][1], board[6][0]],
    ]
    sequences.extend(diagonals)
    return sequences


if __name__ == '__main__':
    main()
