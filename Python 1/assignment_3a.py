# Brian Wolfe                       Created: 09/21/2020

# # This commented out function can be used to test data passed to a function.
# # If data tried is valid then the function is ran normally,
# # Else if the data returns an exception, report the exception
# # This would require the 'lambda:' be used.
# # Example: pass_fail(lambda: append('Hello', 'World!'))
#
# def pass_fail(method_to_run):
#     try:
#         result = method_to_run()
#         return result
#     except Exception as e:
#         print("Exception Raised: ", e)


# Take 2 string variables, concatenate together and print
def append(string1, string2):
    cat_string = string1 + " " + string2
    print(cat_string)


# Take a number and return 0 if less than 0,
# Otherwise return value given
def positiveNumber(num):
    if num < 0:
        return 0
    else:
        return num


# Tests if a number is odd or even.
# Return true if even else return false.
def evenOdd(num):
    even_odd_test = num % 2
    if even_odd_test == 0:
        return True
    else:
        return False


# Test if number is between 0 and 100, inclusive and return True.
def inCenturyRange(num):
    if num in range(0, 101):  # Tests if num is in range of 0 to 100, inclusive
        return True
    else:
        return False


# Take passed string value and append to variable x times then print the results.
def repeater(string='Hello World!', x=5):
    count = 0
    cat_string = ""
    while count < x:
        cat_string += (string + " ")
        count += 1
    print(cat_string)


def main():
    print("-------------------------------------------------------")
    print("     Assignment 3A: Functions w/ Exception Testing")
    print("-------------------------------------------------------")
    print()

    print("Void Function: concatenates 2 strings together.\n")
    append('Hello', 'World!')

    print()
    print("--------------------------")
    print()

    print("Value-Returning Function: returns 0 if number is 0 or less than 0.\n")
    print("Test data: -4, 5, -234, 545\n")
    print(positiveNumber(-4))
    print(positiveNumber(5))
    print(positiveNumber(-234))
    print(positiveNumber(545))

    print()
    print("--------------------------")
    print()

    print("Test if number is even or odd.\n")
    print(f"Value 10 returned for evenOdd() function is: {evenOdd(10)}")
    print()
    print(f"Value 25 returned for evenOdd() function is: {evenOdd(25)}")

    print()
    print("--------------------------")
    print()

    print("Test if value is within 0 to 100 inclusive.\n")
    print("Test data: 50, 1065\n")
    print(f"Value returned for inCenturyRange() function is: {inCenturyRange(50)}")
    print()
    print(f"Value returned for inCenturyRange() function is: {inCenturyRange(1065)}")

    print()
    print("--------------------------")
    print()

    print("Print string value by appending itself x times.")
    print("Default values unless provided alternate values.\n")
    repeater()
    repeater('Provided String Value', 3)

    print()
    print("-----------END------------")
    print()


# Call on the main() function to start program
if __name__ == '__main__':
    main()
