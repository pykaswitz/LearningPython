# Space to play around with concepts and type notes
# ------------------------------------------------------------------------

first_name = "Brian"
last_name = 'Wolfe'
age = 43

# How to combine strings
name = last_name + ", " + first_name
print(name)

# You can't mix data types using this concatenation method
# e.g. name = last_name + ", " + first_name + "is current " + age + "years old."
# This would produce an error unless all variables are of the same data type

# Another way to combine variables but allows for multiple data types.
name1 = f"{last_name}, {first_name} is currently {age} years old."

print(name1)

# A cleaner way to write that is formatted for readability.
# This would require a return before or after + sign.  This is called IMPLICIT CONTINUATION.
# An EXPLICT CONTINUATION would require the \ after each linebreak, but allow a linebreak anywhere.
# Using an explict continuation is considered bad code formatting.
name2 = (last_name + ", "
         + first_name + " is currently "
         + str(age) + " years old.")

print(name2)
print()

# ------------------------------------------------------------------------
# ----------------Math Operators------------------
# Symbol    Operation           Description
# ------------------------------------------------
# +         Addition            Adds two numbers
# -         Subtraction         Subtracts one number from another
# *         Multiplication      Multiplies one number by another
# /         Division            Divides one number by another and gives the results as a float
# //        Integer Division    Divides one number by another and gives the result as a whole number
# %         Remainder           Divides one number by another and gives the result as a whole number
# **        Exponent            Raises a number to a power.
#
# ------------------------------------------------------------------------
#
# Below is a list of codes to add to strings for formatting.
# \n        New Line
# \t        Tab
# \r        Return
# \"        Print quotation mark
# \'        Print quotation mark
# \\        Print back slash.

print("Last Name\t\tFirst Name\t\tAge\n"
      + last_name + "\t\t\t" + first_name + "\t\t\t" + str(age))
print()

# Another way of doing this format is to use "f"
print(f"Last Name       First Name      Age\n"
      f"{last_name}\t\t\t{first_name}\t\t\t{age}")
print()

# ------------------------------------------------------------------------
var = format(123456, '.2f')
print(f"This will add 2 decimal places after the number, formatting the output: ${var}")

var1 = format(123456.789, ',.2f')
print(f"This will truncate the number format to 2 places and add a comma, rounding: ${var1}")

var2 = format(43, '10')
print(f"\n"
      f"This will align the output to have spaces minus the output.\n"
      f"This will produce 8 spaces followed by the number:{var2}")

# ------------------------------------------------------------------------
# print function has two arguments: end= & sep=
# end= replaces the default \n to whatever is placed between ""
# sep= replaces the default single-space separation between variables with whatever is between ""
print("\n" + last_name, first_name, str(age))
print("This is typical print of variables with default separation and new line.\n\n")
print(last_name, first_name, str(age), sep=" | ", end="\t\t\t")
print("Now the next print function, like this one, will be tab separated after previous print function")
print("But following print functions, like this one, revert back to defaults.")

# ------------------------------------------------------------------------
# The round() function will round floating numbers to the nearest decimal
# This you specify the nearest decimal place with an argument in the function
price = 123456.7890123
price = round(price, 2)
print(f"${price} is non-formatted.")
price = format(price, ",")
print(f"${price} is now formatted with a comma.  Notice how you can layer variables into itself.")
print("\n")  # Double space rather than two empty print functions
print("It's better to chain functions. If needed you can format for readability.")
price1 = format(round(123456.7890123, 2), ",")
print(f"${price1} is now formatted and rounded in one")

# ------------------------------------------------------------------------
