# Brian Wolfe                       Created: 11/11/2020

FILENAME = "error_log.txt"


def display_header():
    print("{:-<40}".format(""))
    print("{: ^40}".format("Assignment 9B"))
    print("{: ^40}".format("Error Log File"))
    print("{:-<40}".format(""))


def get_file_contents(file_path):
    # RETURN a LIST of the content_of_file using the file_path
    # Each index position in LIST contains a line of text from file
    # Using with/open format to make sure file closes even on error
    try:
        with open(file_path, "r") as fout:
            return fout.readlines()
    except FileNotFoundError:
        print(f"CRITICAL ERROR: The file named \"{FILENAME}\" could not be found. Please resolve before trying to run this file again.")
        exit()


def display_log_lines(log_content, log_type, sub_log_type=None):
    print("{: <40}".format(f"Display details of lines containing: \"{log_type}\""))
    print("{:-<40}".format(""))

    if sub_log_type is None:
        for i in range(len(log_content)):
            if log_type in log_content[i]:
                print(log_content[i], end="")
    else:
        count = 0
        client_addy = []
        for i in range(len(log_content)):
            if log_type in log_content[i]:
                count += 1
                content = log_content[i].replace("[", "").replace("]", "")
                content = content.split()
                if sub_log_type in content:
                    ip_index = content.index(sub_log_type) + 1
                    ip = content[ip_index]
                    if ip not in client_addy:
                        client_addy.append(ip)

        if len(client_addy) > 1:
            print(f"There are {count} file statements listing [info] for client address(es) {client_addy}.")
        else:
            print(f"There are {count} file statements listing [info] for client address {client_addy}.")

    print("{:-<40}".format(""))
    print()


def display_file_content(file_path):
    file_content = get_file_contents(file_path)
    print("{: ^40}".format(f"Displaying contents of {FILENAME}..."))
    print()

    display_log_lines(file_content, "[error]")
    display_log_lines(file_content, "statistics")
    display_log_lines(file_content, "[info]", "client")


def main():
    display_header()
    display_file_content(FILENAME)

    print("Thank you. Good bye!")


if __name__ == '__main__':
    main()
