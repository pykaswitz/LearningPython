from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)

gen = gen_special_pybites_dates()
dates = list(islice(gen, 10))
print(dates)

'''
https://codechalleng.es/bites/16/

Write a generator that returns the following "special" dates (datetime objects) for PyBites:

- Our birthday! What is the date every year going forward from the PYBITES_BORN date (datetime.datetime(2017, 12, 19, 
0, 0), datetime.datetime(2018, 12, 19, 0, 0), ...)? 

- Return every 100th day counting forward from the PYBITES_BORN date (datetime(2017, 3, 29, 0, 0), datetime(2017, 7, 
7, 0, 0), ...) 

As this is a beginner challenge we're only calculating/ testing a few years ahead of the PYBITES_BORN date. This will 
omit the next leap year (2020) from the challenge making it a bit easier for you (we will revisit this in an 
intermediate challenge). Have fun! 

'''