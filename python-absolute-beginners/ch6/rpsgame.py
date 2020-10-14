print("------------------------------------------------")
print()
print("            Rock, Paper, Scissor v1")
print()
print("------------------------------------------------")

player_1 = input("Enter player one's name: ")
player_2 = input("Enter player two's name: ")

rolls = ['rock', 'paper', 'scissors']

roll1 = input(f"{player_1} what is your roll? [rock, paper, scissors]: ")
roll1 = roll1.lower().strip()  # converts to lower case and removes any trailing spaces
if roll1 not in rolls:
    print(f"Sorry {player_1}, {roll1} not a valid play.")

roll2 = input(f"{player_2} what is your roll? [rock, paper, scissors]: ")
roll2 = roll2.lower().strip()
if roll2 not in rolls:
    print(f"Sorry {player_2}, {roll2} not a valid play.")

print(f"{player_1} rolls {roll1}")
print(f"{player_2} rolls {roll2}")

# Test for a winner
winner = None

if roll1 == roll2:
    print("The play was a tie!")
elif roll1 == 'rock':
    if roll2 == "paper":
        winner = player_2
    elif roll2 == "scissors":
        winner = player_1
elif roll1 == 'paper':
    if roll2 == "rock":
        winner = player_1
    elif roll2 == "scissors":
        winner = player_2
elif roll1 == 'scissor':
    if roll2 == "paper":
        winner = player_1
    elif roll2 == "rock":
        winner = player_2

print("The game is over!")
if winner is None:
    print("It was a tie!")
else:
    print(f"{winner} takes the game!")
