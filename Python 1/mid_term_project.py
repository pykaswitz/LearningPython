# Brian Wolfe                       Created: 10/14/2020

FILENAME = "mid_term_product.txt"  # text file for storing data


def display_header():
    print("----------------------------------------")
    print("      Assignment Mid-Term Exercise")
    print("           Inventory Program")
    print("----------------------------------------")
    print()


def display_menu():
    print("Please select an option from the menu.")
    print()
    print("------------------MENU------------------")
    print("1. Enter a product")
    print("2. Display all products")
    print("3. Exit")
    print("----------------------------------------")
    print()


def append_to_file(file_path, content_list):
    # Convert list to string, APPEND string to file_path
    content_list[2] = str(format(content_list[2], '.2f'))  # Format float 2 decimal then to string
    content_str = ",".join(content_list)  # Ready list for write to file adding commas
    with open(file_path, "a") as fin:
        fin.write(content_str)
        fin.write("\n")


# Chose to reconstitute string into list of lists so that if needed price can easily be converted back to float.
def convert_to_listoflists(tangled_strings):
    lol = []  # ready a list of list variable
    for line in tangled_strings:
        line = line.strip("\n")
        li = list(line.split(","))
        lol.append(li)
    return lol


def read_from_file(file_path):
    # Read the file contents and return
    with open(file_path, "r") as fout:
        file_dump = fout.readlines()
        return convert_to_listoflists(file_dump)


def main():
    menu_looping = True

    display_header()

    while menu_looping:
        try:
            product = []

            display_menu()
            menu_option = input("Please choose a number option from the menu: ")
            print()

            if menu_option == "1":
                print("---------------")
                print("Enter a Product")
                print("---------------")

                testing = True
                while testing:
                    product.append(input("Name: ").title())  # Title case entry
                    if len(product[0]) <= 0:
                        print("\nERROR: This is not a valid name.\n")
                        product.pop()  # Resets the list to remove the invalid entry
                    else:
                        testing = False

                testing = True  # Resets for testing the next entry.
                while testing:
                    product.append(input("Code: ").upper())  # Upper case entry
                    if len(product[1]) != 3:
                        print("\nERROR: This is not a valid code of 3 characters.\n")
                        product.pop()  # Resets the list to remove the invalid entry
                    else:
                        testing = False

                testing = True  # Resets for testing the next entry.
                while testing:
                    try:
                        product.append(float(input("Price: $")))  # Convert to float
                        if product[2] <= 0.0:
                            print("\nERROR: This is not a valid price.\n")
                            product.pop()  # Resets the list to remove the invalid entry
                        else:
                            testing = False
                    except ValueError:
                        # Catches exception if you try to enter nothing
                        print("\nERROR: You must enter a positive amount.\n")
                    except Exception as ex:
                        print(f"\nUNKNOWN ERROR: A exception has occurred: {ex}\n")
                        raise

                append_to_file(FILENAME, product)

                print(f"\nProduct added to {FILENAME}.\n")

            elif menu_option == "2":
                products = read_from_file(FILENAME)

                # https://docs.python.org/2.7/library/string.html#format-specification-mini-language
                # Using string formats to create nicer output of printed file data
                # Detect character length and fills that in within the allotted spacing per cell
                # < ^ > for alignment, number for cell spacing and * for 'unpacking' values
                print("Products on file...")
                print("----------------------------------------")
                print("{: ^20}{: <9}{: <10}".format('Name', 'Code', 'Price'))
                print("----------------------------------------")
                for product in products:
                    print("{: <20}{: <9}${: <10}".format(*product))
                print("-------------------EoF-------------------")
                print()

            elif menu_option == "3":
                print("Thank you. Good bye!")
                menu_looping = False

            else:
                print("ERROR: Invalid menu selection.  Please try again.\n")
        except FileNotFoundError:
            print()
            print(f"ERROR: The file {FILENAME} could not be found.")
            print("\t   Please choose Option 1 to create the file.")
            print()
        except Exception as ex:
            print(f"\nUNKNOWN ERROR: A exception has occurred: {ex}\n")
            raise


if __name__ == '__main__':
    main()
