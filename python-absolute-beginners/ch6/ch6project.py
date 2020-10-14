import random


def main():
    attempt_limit = 5

    show_header(attempt_limit)
    play_game(attempt_limit)


def show_header(tries):
    print('-----------------------------------')
    print('        M&M Guessing Game v2')
    print('-----------------------------------')
    print()
    print(f"Guess the number of M&Ms within {tries} to WIN!")
    print()


def play_game(attempt_limit):
    mm_count = random.randint(1, 100)  # randomly chooses number between 1 and 100

    try_to_guess(mm_count, attempt_limit)


def try_to_guess(count, attempt_limit):
    attempts = 0

    while attempts < attempt_limit:
        guess = int(input("How many M&Ms are in the jar? "))  # asks for user input as string, stores in variable
        attempts += 1

        if count == guess:
            print(f"You guessed CORRECT and WON! You guessed {guess}.")
            break
        elif guess < count:
            print(f"Your guess of {guess} is too LOW.")
        else:
            print(f"Your guess of {guess} is too HIGH.")

    print(f"Goodbye, you're done in {attempts} guesses!")


if __name__ == '__main__':
    main()
