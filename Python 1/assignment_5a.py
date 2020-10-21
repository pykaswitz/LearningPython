# Brian Wolfe                       Created: 10/06/2020

FILENAME = "assignment_5a.txt"  # Setting a constant variable


def display_header():
    print("----------------------------------------")
    print("  Assignment 5A: R/W to External Files  ")
    print("----------------------------------------")
    print()


def display_menu():
    print("Please choose a number option from the menu below:")
    print("1. Write Content to File")
    # print("n. Append Content to File")  # Removed as it isn't part of the assignment
    print("2. Read Content from File as String ")
    print("3. Read Content from File as List")
    print("4. Exit")
    print()


def writeToTextFile(file_path, content_string):
    # WRITE content_string to file_path, return nothing
    # Using with/open format to make sure file closes even on error
    file_content = readListFromTextFile(file_path)
    file_content.append(content_string)

    with open(file_path, "w") as fin:
        for line in file_content:
            fin.write(line)


# def appendToTextFile(file_path, content_string):
#     # APPEND content_string to file_path, return nothing
#     # Commented out as it wasn't asked for in assignment
#     with open(file_path, "a") as fin:
#         fin.write(content_string)


def readFromTextFile(file_path):
    # RETURN the content_of_file using the file_path
    # Using with/open format to make sure file closes even on error
    with open(file_path, "r") as fout:
        return fout.read()


def readListFromTextFile(file_path):
    # RETURN a LIST of the content_of_file using the file_path
    # Each index position in LIST contains a line of text from file
    # Using with/open format to make sure file closes even on error
    with open(file_path, "r") as fout:
        return fout.readlines()


def main():
    menu_looping = True

    display_header()

    print("This program will take text that you enter and save it a file.")
    print("Then gives you an option to display the contents of the file.")
    print("Content is either displayed as a string, or from a list.")
    print()

    while menu_looping:
        try:
            display_menu()
            menu_selection = int(input("Enter your selection: "))

            if menu_selection == 1:
                write_to_file = input("Type content to write to file: ")
                write_to_file = write_to_file + "\n"
                writeToTextFile(FILENAME, write_to_file)
                print()
                print("Your entry has been saved to file.")
                print()
            # elif menu_selection == n:
            #     append_to_file = input("Type content to append to file: ")
            #     append_to_file = append_to_file + "\n"
            #     appendToTextFile(FILENAME, append_to_file)
            elif menu_selection == 2:
                print()
                print("Reading contents of entire file, as string...")
                print("-----------------------------------------")
                print(readFromTextFile(FILENAME))
                print("-------------------EoF-------------------")
                print()
            elif menu_selection == 3:
                listed_content = readListFromTextFile(FILENAME)
                print()
                print("Reading contents of entire file, as list...")
                print("----------------------------------------")
                for i in range(len(listed_content)):
                    print(listed_content[i], end="")
                print("-------------------EoF-------------------")
                print()
            elif menu_selection == 4:
                menu_looping = False
                print("Thank you! Good bye.")
            else:
                print()
                print(f"{menu_selection} is not a valid section. Try again.")
                print()
        except ValueError:
            print()
            print("ERROR: You must choose a number option from the menu.")
            print()
        except FileNotFoundError:
            print()
            print(f"ERROR: The file {FILENAME} could not be found.")
            print("\t   Please choose Option 1 to create the file.")
            print()
        except Exception as ex:
            print()
            print(f"UNKNOWN ERROR: A exception has occurred: {type(ex)}, {ex}")
            print()
            raise


if __name__ == '__main__':
    main()
