# Brian Wolfe                       Created: 10/26/2020
import pickle


def display_instructions():
    print("Enter a pair of product code and numbers.")
    print("Repeat this process until all products have been entered.")
    print("Once complete you can exit to create and save the data to file.")
    print()


def display_header():
    print("{:-<40}".format(""))
    print("{: ^40}".format("Assignment 7A"))
    print("{: ^40}".format("Strings, Dictionaries & Serialization"))
    print("{:-<40}".format(""))
    print()
    display_instructions()


def ask_product_code():
    # Tests the PRODUCT CODE meets requirements: Must be 4 capital letters
    testing_key = True
    while testing_key:
        user_key = input("Enter a product CODE (four capital letters): ").upper()  # Force entry to uppercase

        # Test fails if it contains NUMBERS or WHITESPACE
        for uk in user_key:
            if uk.isdigit() or uk.isspace():
                this_test_passed = False
                break  # If test fails no need to keep testing
            else:
                this_test_passed = True

        # Tests if value is not 4 characters or empty/spaces or if previous test failed
        if len(user_key) != 4 or this_test_passed is False:
            print("\n\tProduct CODE must be four capital letters only.  Please try again.\n")
        else:
            return user_key


def ask_product_number():
    # Tests the PRODUCT NUMBER meets requirements: Must be a number leading with 0
    testing_value = True
    while testing_value:
        user_value = input("Enter a product NUMBER (a number with a leading 0): ")

        # Test fails if it contains LETTERS or WHITESPACES
        for uv in user_value:
            if uv.isalpha() or uv.isspace():
                this_test_passed = False
                break  # If test fails no need to keep testing
            else:
                this_test_passed = True

        # Tests if value is empty/spaces or if value doesn't start with 0 or if previous test failed
        if user_value.isspace() or not user_value.startswith("0") or this_test_passed is False:
            print("\n\tProduct NUMBER must be a number leading with 0.  Please try again.\n")
        else:
            return user_value


def write_products_to_file(products):
    invalid_char = '<>:"/\\|?*'  # \\ is escaped to allow \ in string, using ' to allow " in string
    testing_filename = True

    print("Your data is ready to be saved to file.\n")

    while testing_filename:
        file_name = input("Enter a filename to save product data (no need to apply file extension): ").lower()

        # SCRUB/FORMAT FOR FINAL OUTPUT
        file_name += ".dat"  # Format to add file extension
        file_name = file_name.replace(" ", "_")  # Replace all spaces with underscore
        file_name = file_name.replace(".dat.dat", ".dat")  # Corrects when user applies .dat extension to input
        file_name = file_name.replace("..", ".")  # Corrects when user adds an extra . to end of input value

        # Test to make sure filename doesn't contain characters prohibited by OS for Windows & Linux
        for fn in file_name:
            if fn in invalid_char:
                print(f'\tInvalid Character, {fn}, in {file_name}.  Please try again.\n')
                testing_filename = True
                break
            else:
                testing_filename = False

    # Write user provided data to file
    with open(file_name, "wb") as bfin:
        pickle.dump(products, bfin)


def enter_products():
    products = {}  # Create empty dictionary
    menu_looping = True  # Setting up master-loop

    # START OF MASTER-LOOP  // Only exits if user does not continue
    while menu_looping:
        # ASK FOR PRODUCT DATA
        user_key = ask_product_code()
        user_value = ask_product_number()

        # Tests if user wants to continue or not or if entry is invalid
        user_to_continue = True
        while user_to_continue:
            # All Tests Passed: Store product code & number to dictionary
            products[user_key] = user_value

            user_continue = input("\nDo you wish to continue? Enter y/n: ").upper()
            print()

            if user_continue == 'N' or user_continue == 'NO':
                write_products_to_file(products)
                user_to_continue = False  # Exit sub-loop
                menu_looping = False  # Exit master-loop
            elif user_continue == 'Y' or user_continue == 'YES':
                user_to_continue = False  # Exit sub-loop, but stay in master-loop
            else:
                print("\tInvalid entry. Please enter (Y)es or (N)o to continue.")


def main():
    display_header()
    enter_products()

    print("\nThank you.  Good bye!")


if __name__ == '__main__':
    main()
