# NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
#          'julian sequeira', 'sandra bullock', 'keanu reeves',
#          'julbob pybites', 'bob belderbos', 'julian sequeira',
#          'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
NAMES = ['brian okken', 'michael kennedy', 'trey hunner',
         'matt harrison', 'julian sequeira', 'dan bader',
         'michael kennedy', 'brian okken', 'dan bader']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    n = []
    names = set(names)  # removes dups out of list
    n += [name.title() for name in names]  # list comprehension to title case each value
    return n


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda name: name.split(" ")[-1], reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    n = []
    n += [name.split(" ") for name in names]
    n = sorted(n, key=lambda first: len(first[0]))
    return n[0][0]


print(shortest_first_name(NAMES))

'''
In this bite you will work with a list of names.

First you will write a function to take out duplicates and title case them.

Then you will sort the list in alphabetical descending order by surname and lastly determine what the shortest first 
name is. For this exercise you can assume there is always one name and one surname. 

With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)

'''
