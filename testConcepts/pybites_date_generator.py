from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)
special_day = []


def gen_special_pybites_dates():
    calc_date = PYBITES_BORN + timedelta(days=100)
    print(calc_date)
    special_day.append(calc_date)
    print(special_day)
    # WHY DOES IT ADD datetime.datetime TO LIST????
    # for i in range(9):
    #     special_day.append(special_day[i] + timedelta(days=100))
    return special_day

gen_special_pybites_dates()

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