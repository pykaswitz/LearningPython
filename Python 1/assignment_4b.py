# Brian Wolfe                       Created: 09/29/2020


def print_header():
    print("---------------------------------")
    print("      Assignment 4B: Lists")
    print("---------------------------------")
    print()


def collect_customer_data(customers):
    customer_list_count = 10  # Set the number of customers entries to capture
    customer_idx = 0  # Tracks loop count and provide index for list
    error_msg = 0
    name = []
    spend = []

    print(f"Please enter {customer_list_count} customer names and spending amounts.\n")
    while customer_idx < customer_list_count:
        try:
            name.append(input("Enter customer name: ").title())

            if name[-1] == "" or name[-1].isspace():  # Test that name input isn't empty or all spaces
                error_msg = 1  # Upon raising exception, provides specific error message
                raise ValueError
            spend.append(float(input(f"How much did {name[customer_idx]} spend? $")))
            print()

            if spend[-1] < 0:  # Test that spend input isn't negative
                error_msg = 2  # Upon raising exception, provides specific error message
                spend.pop()  # Reset list to clear invalid entry
                raise ValueError
            else:
                customer_idx += 1

        except ValueError as ve:
            if error_msg == 1:
                print("ERROR: Input cannot be empty.  Try again with customer name.\n")
            elif error_msg == 2:
                print(f"ERROR: Invalid input.  Enter {name[-1]}'s name again, and use a positive number.\n")
            else:
                print(f"UNKNOWN ERROR: An exception has occurred: {ve}.\n")

            name.pop()  # Reset list to clear invalid entry
        except Exception as ex:
            print(f"An error has occurred: {ex}")

    # Create a List of Lists for customers[[names], [spend]]
    customers.append(name)
    customers.append(spend)


def total_spend(customers, spend_idx):
    spend_total = 0.0

    # loops through list length to total all spend amounts in list
    for customer_idx in range(len(customers[spend_idx])):
        spend_total += customers[spend_idx][customer_idx]

    return spend_total


def average_spend(customers, spend_idx):
    spend_total = total_spend(customers, spend_idx)
    spend_average = spend_total / len(customers[spend_idx])

    return spend_average


def highest_spend(customers, spend_idx):
    spend_highest = max(customers[spend_idx])
    return spend_highest


def lowest_spend(customers, spend_idx):
    spend_lowest = min(customers[spend_idx])
    return spend_lowest


def print_report(customers):
    customer_idx = 0  # Tracks loop count and provide index for list
    name_idx = 0  # call the Names list and make code more readable when used in lists or functions
    spend_idx = 1  # call the Spend list and make code more readable when used in lists or functions

    print("---------------------------------")
    print("Customer Report")
    print("---------------------------------")
    while customer_idx < len(customers[name_idx]):
        print(customers[name_idx][customer_idx], end="\t\t.......\t\t")
        print(f"${format(customers[spend_idx][customer_idx], ',.2f')}")
        customer_idx += 1
    print("---------------------------------")
    print(f"Total\t\t.......\t\t${format(total_spend(customers, spend_idx), ',.2f')}")
    print("\n---------------------------------")
    print("Spending Report")
    print("---------------------------------")
    print(f"Average\t\t.......\t\t${format(average_spend(customers, spend_idx), ',.2f')}")

    print(f"Highest\t\t.......\t\t${format(highest_spend(customers, spend_idx), ',.2f')}")

    print(f"Lowest\t\t.......\t\t${format(lowest_spend(customers, spend_idx), ',.2f')}")
    print("\n")


def main():
    customers = []

    print_header()

    collect_customer_data(customers)

    print_report(customers)

    print("You have completed the report.  Thank you and goodbye!\n")


if __name__ == '__main__':
    main()
