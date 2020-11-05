# Brian Wolfe                       Created: 11/04/2020
from datetime import datetime, timedelta


def display_instructions():
    print("Enter a date then provide a number of days you want to increase the date by.")


def display_header():
    print("{:-<40}".format(""))
    print("{: ^40}".format("Assignment 8B"))
    print("{: ^40}".format("Increase Date by Number of Days"))
    print("{:-<40}".format(""))
    print()
    display_instructions()


def main():
    display_header()

    testing = True

    # ASK FOR DATE
    while testing:
        try:
            user_date_str = input("Enter a date in the format of MM/DD/YYYY: ")
            user_date = datetime.strptime(user_date_str, '%m/%d/%Y')
            break
        except ValueError:
            print("INVALID ENTRY: You entered an invalid date or a date in an unexpected format.  Please try again.")
            continue
        except Exception as ex:
            print(f"UNKNOWN ERROR: {type(ex)}: {ex}")
            continue

    # ASK FOR DAYS TO INCREASE DATE
    while testing:
        try:
            adjusted_days = int(input(f"How many days do you want to increase past {user_date.strftime('%B %d, %Y')}: "))
            if adjusted_days > 0:
                adjusted_date = user_date + timedelta(days=adjusted_days)
                break
            elif adjusted_days < 0 or adjusted_days == 0:
                print("INVALID ENTRY: Enter a positive number greater than 0.  Please try again.")
                continue
        except ValueError:
            print("INVALID ENTRY: You must enter a positive number.  Please try again.")
            continue
        except Exception as ex:
            print(f"UNKNOWN ERROR: {type(ex)}: {ex}")
            continue

    # SUCCESS! DISPLAY RESULTS
    print(f"{datetime.strftime(adjusted_date, '%B %d, %Y')} is {adjusted_days} days after {user_date.strftime('%B %d, %Y')}.")



if __name__ == '__main__':
    main()

'''
Code a program that that does the following:

The user should be prompted to enter a date (year, month, day). 

Then the user should be prompted to enter a number of days.

Increase the date by the number of days and display the results.

So if you enter a date of April 1, 2020 and then enter a value of 15 days, the program should display 
a date of April 16, 2020. 

'''