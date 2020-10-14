# Brian Wolfe                       Created: 09/29/2020

def print_header():
    print("---------------------------------")
    print("      Assignment 4A: Lists")
    print("---------------------------------")
    print()


# Asks user to define list length and provide each value in that list
def create_list(user_list):
    try:
        list_len = int(input("Hello, please enter an integer value the size of your list: "))
        # Logic exception handling: Tests that list length is greater than 0
        if list_len > 0:
            while list_len != 0:
                # Using .append() allows for a loop count using less.
                # Once list_len reaches 0 the loop ends at the users defined list length.
                user_list.append(int(input("Please enter an integer value between 1 and 10 (inclusive): ")))
                list_len -= 1
        else:
            print("\nList size cannot be less than 1.")
            print("Retry again.\n")
    except ValueError as ve:
        print("\nERROR: Enter an integer value only.")
        print(f"ERROR: {ve}")
        print("Retry again.\n")
    except Exception as ex:
        print(f"An error has occurred: {ex}")


def convert_to_symbol(user_list):
    # Takes list values and converts to stars within limit.
    # Limit Range: 0 or < to 1 star; 10 or > to 10 stars

    star = "*"

    for number in user_list:
        if number >= 10:
            print(star * 10)
        elif number <= 0:
            print(star)
        else:
            print(star * number)


def main():
    user_list = []

    print_header()

    # Tests that user_list isn't empty.
    # List will remain empty if function ends due to exception, forces redo for valid input.
    while not user_list:
        create_list(user_list)

    print("\nPrinting your entries as a chart:")
    convert_to_symbol(user_list)


if __name__ == '__main__':
    main()
