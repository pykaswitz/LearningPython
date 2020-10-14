num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6]
text = "I watched the brown fox jumped over the blue dog under the big full moon!"


def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    return [i for i in numbers if i > 0 and (i % 2) == 0]


def replace_with_vowels(word):
    vowels = 'aeiou'
    cat_string = []

    for letter in word:
        if letter.lower() in vowels:
            cat_string.append("*")
        else:
            cat_string.append(letter)

    return cat_string


print(filter_positive_even_numbers(num))
print("".join(replace_with_vowels(text)))

# create empty list to hold counts of each item
# name in test
# letter in name += 1 then store result in count list
# finish name in test then find max # in count list
test = ["Brian", "Juliet", "Biscuit", "Finnley", "Noodle"]
count_list = []

for name in test:
    num = 0
    for letter in name:
        num += 1
    count_list.append(num)

print(max(count_list))


# def name_length(name):
#     letter_count = 0
#     for letter in name:
#         letter_count += 1
#
#     return letter_count


# Round spacing/num to the nearest 4 or whatever number set to base
def myround(x, base=4):
    return base * round(x / base)


spacing = 5
tab_len = 4
if num > myround(spacing):
    num = myround(spacing) + tab_len
print(myround(spacing))

some_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
some_numbers2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def sum_numbers(numbers=None):
    if numbers is None:
        seed = 0
        nums = []
        while seed < 100:
            seed += 1
            nums.append(seed)
        i = 0
        for n in nums:
            i += n
        return i

    else:
        i = 0
        for n in numbers:
            i += n
        return i


def sum_numbers_mini(numbers=None):
    if numbers is None:
        numbers = range(1, 101)
    return sum(numbers)


print("You can use list or tuples in the following.  Just note that tuples are smaller and faster @ machine level.")
print(sum_numbers())
print(sum_numbers(some_numbers))
print()
print("Here is the better, smaller way to write this code:")
print(sum_numbers_mini())
print(sum_numbers_mini(some_numbers2))

print("\nAll about them tuples\n")

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print("Using range:", my_tuple[2:7])
print("Using range with step; even/odd, etc.:", my_tuple[2:8:2])
print("Using start range, starts at index:", my_tuple[2:])
print("Using end range, ends before index:", my_tuple[:6])
print("Using step 1 to list every item:", my_tuple[::1])
print("Using step 2 to list every other item:", my_tuple[::2])
print("Using step -1 to reverse every item:", my_tuple[::-1])

example = my_tuple[2:7]
print("Using a variable:", example)

print()
my_tuple2 = (0, 1, 2, 3, 4, 5)

i1, i2, i3, i4, i5, i6 = my_tuple2
print("Requires equal number of variables to assign value inline.")
print(i1)
print(i2)
print(i3)
print(i4)
print(i5, i6, sep=", ")

print()
n1, *n2, n3 = my_tuple2

print("Using * assigns remain values to variable as list.")
print(n1)
print(n3)
print()
print(
    "A 0 index assigned to n1, -1 (last) index assigned to n3.\nAll remaining values assigned to n2 as marked with *:",
    n2)
