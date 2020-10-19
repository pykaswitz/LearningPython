def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """

    # test if n is pos or neg
    # if pos add first letters to sep list / append to string / return string
    # if neg add first letters up to last referenced by n / append to string / return string

    string = list(string)
    parked = []
    for char in string:
        if n > 0:
            parked += char
            n -= 1
        else:
            parked = "".join(parked)
            string += str(parked)
            break

    print("what's this:", parked)
    print("merged:", string)

    print("final:", string)

    # string = list(string)
    # string.append(string.pop(0))  # This worked, but may not be what we need
    # string = "".join(string)
    # print("final:", parked)




print(rotate('hello', 2))

'''
Write a function that rotates characters in a string, in both directions:

if n is positive move characters from beginning to end, e.g.: rotate('hello', 2) would return llohe
if n is negative move characters to the start of the string, e.g.: rotate('hello', -2) would return lohel
See tests for more info. Have fun!

'''