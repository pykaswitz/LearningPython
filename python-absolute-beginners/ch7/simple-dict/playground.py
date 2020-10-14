# Data Sturctures
# 1. Dictionaries
# 2. List / Arrays [1,1,7,11]
# 3. Sets

# Lists: creates a list of data
lst = [1, 1, 7, 11]

print(f"Default list output: {lst}")
lst.append(2)
print(f"List now added 2: {lst}")
lst.remove(11)
print(f"List now removed 11: {lst}")
lst.sort()
print(f"List is now sorted: {lst}")

# Sets: Creates a list of distinct data, no duplicates
st = {1, 1, 7, 11}
print(f"\nDefault set output: {st}")
st.add(1)
st.add(1)
st.add(11)
print(f"Set had 1 and 11 added to variable: {st}\nNotice how it lists only unique data.  Duplicates are ignored.\n")

# Dictionary:   Sets values to names, or what are called keys.
#               It can also have different data types for each key.
# d1 = dict(bob=0, sarah=0) :: this is another way of defining a dictionary

d = {
    'bob': 0,
    'sarah': 0,
    'defeats_by': {'paper', 'wolf'},
    'defeats': {'scissors', 'sponge'}
}

print(f"Here is the default print of a dictionary: {d}")
print(f"This pulls the assigned data to the key called 'bob' which is: {d['bob']}")
d['bob'] += 1
print(f"Now you'll see that bob is updated plus one: {d['bob']}")
print(f"And showing all the assigned data to the dictionary shows it has been updated: {d}")
d['mike'] = 7
print(f"Now the dictionary has 'mike' added to the set: {d}")
print(f"You can show the lists in a dictionary like so: {d['defeats_by']}")
# d['other'] which is not in the dictionary when called will crash program
# To test for data in a dictionary you do the following:
print(f"This will return a nul value, meaning the data doesnt exist: {d.get('other')}")
print(f"This will return a specific defined error code, 42, meaning the data doesnt exist: {d.get('other', 42)}")
