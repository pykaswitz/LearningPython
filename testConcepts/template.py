# Brian Wolfe                       Created: MM/DD/YYYY


def display_instructions():
    pass


def display_header():
    print("{:-<40}".format(""))
    print("{: ^40}".format("Assignment Title"))
    print("{: ^40}".format("Sub-Title"))
    print("{:-<40}".format(""))
    print()
    display_instructions()


def main():
    display_header()


if __name__ == '__main__':
    main()
