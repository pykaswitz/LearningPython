import random  # Load random functions
import json  # Load functions to r/w JSON files
import os  # Load functions to work with different OS types
import datetime  # Load functions for datetime

# It is best to import the library Logbook instead of writing logging from scratch

rolls = {}


def main():
    log("App starting up...")

    load_rolls()
    show_header()
    show_leaderboard()

    player1, player2 = get_players()
    log(f"{player1} has logged in.")

    play_game(player1, player2)
    log("Game over.")


def show_header():
    print("----------------------------")
    print("  Rock, Paper, Scissor v4")
    print(" R/W External Files Edition")
    print("----------------------------")


def show_leaderboard():
    leaders = load_leaders()

    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print()
    print("LEADERS:")
    # f-string on wins format to have commas
    # range expressed as 0:5 meaning Top 5
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins:,} -- {name}")
    print()
    print("----------------------------")
    print()


def get_players():
    p1 = input("Player 1, what is your name? ")
    p2 = "Computer"

    return p1, p2


def play_game(player_1, player_2):
    log(f"New game starting between {player_1} and {player_2}.")

    wins = {player_1: 0, player_2: 0}
    roll_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll1 = get_roll(player_1, roll_names)
        roll2 = random.choice(roll_names)

        if not roll1:
            print("Try again!")
            continue

        log(f"Round: {player_1} rolls {roll1} and {player_2} rolls {roll2}.")
        print(f"{player_1} rolls {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            msg = "Round was a tie!"
            print(msg)
            log(msg)
        else:
            msg = f'{winner} takes the round!'
            print(msg)
            log(msg)
            wins[winner] += 1

        msg = f"Score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}"
        print(msg)
        log(msg)
        print()

    overall_winner = find_winner(wins, wins.keys())
    msg = f"{overall_winner} wins the game!"
    print(msg)
    log(msg)
    record_win(overall_winner)


def find_winner(wins, names):
    best_of = 3

    for name in names:
        if wins.get(name, 0) >= best_of:
            return name

    return None


def check_for_winning_throw(player_1, player_2, roll1, roll2):
    # Test for a winner
    winner = None
    if roll1 == roll2:
        print("The play was a tie!")

    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated_by'):
        return player_2

    return winner


def get_roll(player_name, rolls_names):
    print("Available rolls:")
    for index, r in enumerate(rolls_names, start=1):
        print(f"{index}. {r}")

    text = input(f"{player_name}, what is your roll? ")
    selected_index = int(text) - 1

    # Test if input is valid
    if selected_index < 0 or selected_index >= len(rolls_names):
        print(f"Sorry {player_name}, {text} is out of bounds.")
        return None

    return rolls_names[selected_index]


def load_rolls():
    global rolls

    # Gets current directory path using OS library
    # Then joins file "rolls.json" to the current directory path
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'rolls.json')

    # # This will work, but doesn't close file in cases of exceptions
    # fin = open(filename, 'r', encoding='utf-8')
    # rolls = json.load(fin)
    # fin.close()

    # This closes files safer in cases of exceptions.
    # This is called a Context Manager
    # Much better way to open/close files
    with open(filename, 'r', encoding='utf-8') as fin:
        rolls = json.load(fin)

    log(f"Loading rolls: {list(rolls.keys())} from {os.path.basename(filename)}.")


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
    filename = os.path.join(directory, 'rps.log')
    time_text = datetime.datetime.now().strftime('%c')

    # This format 'a'ppends the output to a file called rps.log
    with open(filename, 'a', encoding="utf-8") as fout:
        fout.write(f"[{time_text}] ")
        fout.write(msg)
        fout.write('\n')


if __name__ == '__main__':
    main()
