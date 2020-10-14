import random
import json
import os
import datetime

from colorama import Fore, init
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter, Completer, Completion


rolls = {}
init()


def main():
    try:
        print(Fore.WHITE)
        log("App starting up...")

        load_rolls()
        show_header()
        show_leaderboard()

        player1, player2 = get_players()
        log(f"{player1} has logged in.")

        play_game(player1, player2)
        log("Game over.")
    except json.decoder.JSONDecodeError as je:
        print()
        print(Fore.RED + "ERROR: The file rolls.json is invalid JSON." + Fore.WHITE)
        print(Fore.RED + f"ERROR: {je}" + Fore.WHITE)
    except FileNotFoundError as fe:
        print()
        print(Fore.RED + "ERROR: Rolls file not found." + Fore.WHITE)
        print(Fore.RED + f"ERROR: {fe}" + Fore.WHITE)
    except KeyboardInterrupt:
        print()
        print(Fore.CYAN + "You gotta run? Ok, cya next!" + Fore.WHITE)
    except Exception as x:
        print()
        print(Fore.RED + f"Unknown Error: {x}" + Fore.WHITE)


def show_header():
    print(Fore.LIGHTMAGENTA_EX, end="")
    print("----------------------------")
    print("  Rock, Paper, Scissor v.6")
    print("   Error Handling Edition")
    print("----------------------------")
    print(Fore.WHITE, end="")


def show_leaderboard():
    leaders = load_leaders()

    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print(Fore.LIGHTGREEN_EX)
    print("----------------------------")
    print("LEADERS:")
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins:,} -- {name}")
    print("----------------------------")
    print(Fore.WHITE)


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
            print(Fore.LIGHTRED_EX + "Try again!")
            print(Fore.WHITE)
            continue

        log(f"Round: {player_1} rolls {roll1} and {player_2} rolls {roll2}.")
        print(Fore.YELLOW + f"{player_1} rolls {roll1}")
        print(Fore.LIGHTBLUE_EX + f"{player_2} rolls {roll2}")
        print(Fore.WHITE, end="")

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            msg = "Round was a tie!"
            print(msg)
            log(msg)
        else:
            msg = f'{winner} takes the round!'
            fore = Fore.GREEN if winner == player_1 else Fore.LIGHTRED_EX
            print(fore + msg + Fore.WHITE)
            log(msg)
            wins[winner] += 1

        msg = f"Score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}"
        print(msg)
        log(msg)
        print()

    overall_winner = find_winner(wins, wins.keys())
    fore = Fore.GREEN if overall_winner == player_1 else Fore.LIGHTRED_EX
    msg = f"{overall_winner} wins the game!"
    print(fore + msg + Fore.WHITE)
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
    try:
        print(f"Available rolls: {', '.join(rolls_names)}")

        word_comp = PlayCompleter()

        roll = prompt(f"{player_name}, what is your roll: ", completer=word_comp)

        # Test if input is valid
        if not roll or roll not in rolls_names:
            print()
            print(Fore.LIGHTRED_EX, end="")
            print(f"Sorry {player_name}, {roll} is out of bounds.")
            print(Fore.WHITE, end="")
            return None

        return roll
    except ValueError as ve:
        print(Fore.RED + f"Could not convert integer: {ve}" + Fore.WHITE)
        return None


def load_rolls():
    global rolls

    # Gets current directory path using OS library
    # Then joins file "rolls.json" to the current directory path
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'rolls.json')

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

    with open(filename, 'a', encoding="utf-8") as fout:
        fout.write(f"[{time_text}] ")
        fout.write(msg)
        fout.write('\n')


class PlayCompleter(Completer):

    def get_completions(self, document, complete_event):
        roll_names = list(rolls.keys())
        word = document.get_word_before_cursor()
        complete_all = not word if not word.strip() else word == '.'
        completions = []

        for roll in roll_names:
            is_substring = word in roll
            if complete_all or is_substring:

                completion = Completion(
                    roll,
                    start_position=-len(word),
                    style="fg:white bg:blue",
                    selected_style="fg:yellow bg:green",
                )

                completions.append(completion)

        return completions


if __name__ == '__main__':
    main()
