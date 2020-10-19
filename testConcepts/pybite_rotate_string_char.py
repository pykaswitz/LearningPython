def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """

    # test if n is pos or neg
    # if pos add first letters to sep list / append to string / return string
    # if neg add first letters up to last referenced by n / append to string / return string

    string = list(string)

    i = n
    parked = []
    popped = string.copy()
    
    if n > 0:
        for char in string:
            if i > 0:
                popped.pop(popped.index(char))
                i -= 1
        parked = string[slice(n)]

        string = popped + parked
        string = "".join(string)
        return string
    elif n < 0:
        popped.reverse()
        string.reverse()        
        for char in string:
            if i < 0:
                parked += popped.pop(popped.index(char))
                i += 1
        popped.reverse()
        parked.reverse()
        string = parked + popped
        string = "".join(string)
        return string  


print(rotate('hello', 2))

'''
Write a function that rotates characters in a string, in both directions:

if n is positive move characters from beginning to end, e.g.: rotate('hello', 2) would return llohe
if n is negative move characters to the start of the string, e.g.: rotate('hello', -2) would return lohel
See tests for more info. Have fun!

'''
