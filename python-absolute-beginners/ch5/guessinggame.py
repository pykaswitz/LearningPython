import random

print('-----------------------------------')
print('         M&M Guessing Game')
print('-----------------------------------')

print("Guess the number of M&Ms and you get lunch on the house!")
print()

mm_count = random.randint(1, 100)  # randomly chooses number between 1 and 100
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_txt = input("How many M&Ms are in the jar? ")  # asks for user input as string, stores in variable
    guess = int(guess_txt)  # converts string(guess_text) to integer(guess)
    attempts += 1

    if mm_count == guess:
        print(f"You guessed CORRECT and WON a free lunch! You guessed {guess}.")
        break
    elif guess < mm_count:
        print(f"Your guess of {guess} is too LOW.")
    else:
        print(f"Your guess of {guess} is too HIGH.")


print(f"Goodbye, you're done in {attempts}!")
