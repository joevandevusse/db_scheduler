#!/usr/bin/python3

class Scheduler:

    """
    Typical day - 2 workers from 7:30 am - 7:30 pm
    12 hours or 24 intervals
    Intervals -
    0 =  7:30  am - 8:00  am
    1 =  8:00  am - 8:30  am
    2 =  8:30  am - 9:00  am
    3 =  9:00  am - 9:30  am
    4 =  9:30  am - 10:00 am
    5 =  10:00 am - 10:30 am
    6 =  10:30 am - 11:00 am
    7 =  11:00 am - 11:30 am
    8 =  11:30 am - 12:00 pm
    9 =  12:00 pm - 12:30 pm
    10 = 12:30 pm - 1:00  pm
    11 = 1:00  pm - 1:30  pm
    12 = 1:30  pm - 2:00  pm
    13 = 2:00  pm - 2:30  pm
    14 = 2:30  pm - 3:00  pm
    15 = 3:00  pm - 3:30  pm
    16 = 3:30  pm - 4:00  pm
    17 = 4:00  pm - 4:30  pm
    18 = 4:30  pm - 5:00  pm
    19 = 5:00  pm - 5:30  pm
    20 = 5:30  pm - 6:00  pm
    21 = 6:00  pm - 6:30  pm
    22 = 6:30  pm - 7:00  pm
    23 = 7:00  pm - 7:30  pm
    """

    def __init__(self, emp_list):
        self._emp_list = emp_list
