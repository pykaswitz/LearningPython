# Brian Wolfe                       Created: 10/14/2020

FILENAME = "mid_term_product.txt"  # text file for storing data


def display_header():
    print("----------------------------------------")
    print("      Assignment Mid-Term Exercise")
    print("           Inventory Program")
    print("----------------------------------------")
    print()


def display_menu():
    print("1. Enter a product")
    print("2. Display all products")
    print("3. Exit")
    print()


def append_to_file(file_path, content_list):
    # Convert list to string, APPEND string to file_path
    content_list[2] = str(format(content_list[2], '.2f'))  # Format float 2 decimal then to string
    content_str = ", ".join(content_list)  # Ready list for write to file adding commas
    with open(file_path, "a") as fin:
        fin.write(content_str)
        fin.write("\n")


def read_from_file(file_path):
    # Read the file contents and return
    with open(file_path, "r") as fout:
        return fout.readlines()


def main():
    menu_looping = True

    display_header()

    while menu_looping:
        product = []

        display_menu()
        menu_option = input("Please choose a number option from the menu: ")
        print()

        if menu_option == "1":
            print("---------------")
            print("Enter a Product")
            print("---------------")
            product.append(input("Name: ").title())  # Title case entry
            product.append(input("Code: ").upper())  # Upper case entry
            product.append(float(input("Price: $")))  # Convert to float

            append_to_file(FILENAME, product)

            print(f"\nProduct added to {FILENAME}.\n")

        elif menu_option == "2":
            products = read_from_file(FILENAME)

            print("----------------------------------------")
            print("Products on file...")
            print("----------------------------------------")
            for item in range(len(products)):
                print(products[item], end="")
            print("-------------------EoF-------------------")
            print()

        elif menu_option == "3":
            menu_looping = False

        else:
            print("Invalid menu selection.  Please try again.\n")


if __name__ == '__main__':
    main()

