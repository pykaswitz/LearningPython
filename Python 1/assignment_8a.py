# Brian Wolfe                       Created: 11/04/2020
from datetime import datetime

ANCHOR_DATE_STR = "December 7, 1941"


def display_instructions():
    print(f"How many days have passed since {ANCHOR_DATE_STR}?")


def display_header():
    print("{:-<40}".format(""))
    print("{: ^40}".format("Assignment 8A"))
    print("{: ^40}".format("Determine How Many Days Passed"))
    print("{:-<40}".format(""))
    print()
    display_instructions()


def main():
    display_header()

    program_looping = True

    # Looping until a successful date is entered
    while program_looping:
        try:
            # ASK FOR DATE
            user_date_str = input("Enter a date in the format of YYYY-MM-DD: ")
            print()

            # CONVERT TO DATE OBJECTS
            # If conversion fails, raises exception, ValueError
            user_date = datetime.strptime(user_date_str, '%Y-%m-%d')
            anchor_date = datetime.strptime(ANCHOR_DATE_STR, '%B %d, %Y')

            # TEST DATE OBJECTS ARE INLINE WITH REQUIREMENTS
            # Does user date come before or after anchor date?
            if user_date > anchor_date:
                number_of_days = format((user_date - anchor_date).days, ",")
                print(number_of_days, "days have passed since", ANCHOR_DATE_STR)
                print("Thank you.  Good bye!")
                program_looping = False
            else:
                print(f"INVALID DATE: You must enter a date after {ANCHOR_DATE_STR}.  Please try again.")
                continue
        except ValueError:
            print("INVALID ENTRY: You entered an invalid date or a date in an unexpected format.  Please try again.")
            continue
        except Exception as ex:
            print(f"UNKNOWN ERROR: {type(ex)}: {ex}")
            continue


if __name__ == '__main__':
    main()
