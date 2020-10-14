import json
import os
import datetime
from colorama import Fore, init


def main():

    init()

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

    log("App is starting up...")
    show_header()
    show_leaderboard()

    print(Fore.WHITE, end="")

    # CHOSE INITIAL PLAYER
    active_player_index = 0
    player_1 = input(f"Player 1, enter your name: ")
    print()
    player_2 = input(f"Player 2, enter your name: ")

    players = [player_1, player_2]
    symbols = ["R", "Y"]
    player = players[active_player_index]

    log(f"{player_1} has logged in as Player 1 using (R)ed token.")
    log(f"{player_2} has logged in as Player 2 using (Y)ellow token.")

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player, active_player_index)
        show_board(board)
        if not choose_location(board, symbol):
            print(Fore.LIGHTRED_EX, end="")
            print("That isn't an option, try again.")
            print(Fore.WHITE, end="")
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(Fore.LIGHTBLUE_EX, end="")
    print(f"GAME OVER! {player} has won with the board: ")
    print(Fore.WHITE, end="")
    log(f"GAME OVER! {player} has won.")

    show_board(board)
    print()

    record_win(player)


def show_header():
    print(Fore.LIGHTGREEN_EX, end="")
    print("----------------------------")
    print(" Welcome to Connect Four v2")
    print("    Read/Write to Files")
    print("----------------------------")
    print(Fore.WHITE, end="")


def show_leaderboard():
    leaders = load_leaders()

    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print(Fore.LIGHTBLUE_EX, end="")
    print()
    print("LEADERS:")
    # f-string on wins format to have commas
    # range expressed as 0:5 meaning Top 5
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins:,} -- {name}")
    print()
    print("----------------------------")
    print()
    print(Fore.WHITE, end="")


def show_board(board):
    i = 0
    while i < len(board[0]):
        print("| ", end='')
        for cell in board:
            if cell[i] is None:
                cell[i] = "_"
                print(cell[i], end=' | ')
            elif cell[i] == "R":
                print(Fore.LIGHTRED_EX, end="")
                print(cell[i], end='')
                print(Fore.WHITE, end=" | ")
            elif cell[i] == "Y":
                print(Fore.YELLOW, end="")
                print(cell[i], end='')
                print(Fore.WHITE, end=" | ")
            else:
                print(cell[i], end=' | ')
        i += 1
        print()
    print()


def announce_turn(player, turn):
    if turn == 0:
        player_color = Fore.LIGHTRED_EX + player + "'s" + Fore.WHITE
    else:
        player_color = Fore.YELLOW + player + "'s" + Fore.WHITE

    print()
    print("It's", player_color, "turn.")
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


def load_leaders():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    # If file does NOT exist it will load an empty dict
    if not os.path.exists(filename):
        return {}

    # Load existing data from file
    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def record_win(winner_name):
    leaders = load_leaders()

    if winner_name in leaders:
        leaders[winner_name] += 1
    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    # Write data to file
    with open(filename, 'w', encoding='utf-8') as fout:
        json.dump(leaders, fout)


def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'connect4.log')
    time_text = datetime.datetime.now().strftime('%c')

    # This format 'a'ppends the output to a file called rps.log
    with open(filename, 'a', encoding="utf-8") as fout:
        fout.write(f"[{time_text}] ")
        fout.write(msg)
        fout.write('\n')


if __name__ == '__main__':
    main()
