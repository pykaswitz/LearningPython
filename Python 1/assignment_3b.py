# Brian Wolfe                       Created: 09/21/2020


go_again = True


def printer_header():
    print("-------------------------------------------------------")
    print("    Assignment 3B: Simple Calculating Program v2.0")
    print("-------------------------------------------------------")
    print()


def get_user_choice():
    # Ask for operation to perform and 2 values
    operator = int(input("1) to add\n2) to subtract\n3) to multiply\n4) to divide\nEnter an operation to perform: "))
    x_value = float(input("\nEnter your first value:\t\t"))
    y_value = float(input("Enter your second value:\t"))
    choice_results(operator, x_value, y_value)


def choice_results(operator, x_value, y_value):
    # Pass 2 values to the operation function selected by user, print results
    print("\t\t\t\t\t\t----------")
    if operator == 1:
        print("\t\t\t\tResults:   ", addition(x_value, y_value))
    elif operator == 2:
        print("\t\t\t\tResults:   ", subtraction(x_value, y_value))
    elif operator == 3:
        print("\t\t\t\tResults:   ", multiply(x_value, y_value))
    elif operator == 4:
        print("\t\t\t\tResults:   ", divide(x_value, y_value))
    else:
        print("Invalid choice entered.")

    print()
    print("----------------------------------")
    print("----------------------------------")
    print()


def addition(x_add, y_add):
    add_result = x_add + y_add
    return add_result


def subtraction(x_sub, y_sub):
    sub_result = x_sub - y_sub
    return sub_result


def multiply(x_times, y_times):
    times_result = x_times * y_times
    return times_result


def divide(x_div, y_div):
    div_result = x_div / y_div
    return div_result


def main():
    global go_again

    printer_header()

    while go_again:
        get_user_choice()

        choice = input("Do you have more data to enter? ")
        print()
        if choice.lower() == "yes" or choice.lower() == "y":
            continue
        elif choice.lower() == "no" or choice.lower() == "n":
            print("Good bye.")
            go_again = False
        else:
            print("Invalid choice entered. Enter (y)es or (n)o.\n")
            continue


if __name__ == '__main__':
    main()
