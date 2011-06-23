# -*- coding: utf-8 -*-
# Filename: vacation.py
# Description: 
# Author: Rodrigo Coacci <rodrigo@kuat>
# Copyright (C) 2011, Rodrigo Coacci, all rights reserved.
# Created: 2011-06-22 23:35:46
# Version: 0.1
# Last-Updated: 2011-06-22 23:35:46 By: Rodrigo Coacci

from calendar import calendar
import datetime

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def holidays_in(year):
    """Returns a list of datetime.date object containing all holidays in the year. 
    """
    
def near_weekend(day):
    """Returns True if day is near (immediately before or after) a weekend
    >>> near_weekend(datetime.date(2011,06,22))
    False
    >>> near_weekend(datetime.date(2011,06,24))
    True
    """
    weekday = weekdays[day.weekday()]
    return (weekday =='Friday') or (weekday == 'Monday')

def near_holiday(day,holiday_list):
    """Returns True if day is near (immediately before or after) a day in holiday_list
    >>> near_holiday(datetime.date(2011,06,22),[datetime.date(2011,06,23),datetime.date(2011,12,25)])
    True
    >>> near_holiday(datetime.date(2011,06,20),[datetime.date(2011,06,23),datetime.date(2011,12,25)])
    False
    """
    for d in holiday_list:
        delta = day - d
        if (delta == datetime.timedelta(-1) or delta == datetime.timedelta(1)):
            return True
        
    return False

def best_vacation(start_date,holiday_list):
    """
    """
    day = start_date
    max_days = 0
    best_start1 = None
    best_end1 = None
    while day.year == start_date.year:
        end1 = day + datetime.timedelta(10)
        total_days = day + end1
        if(near_weekend(day)):
            total_days+=2
        if(near_weekend(end1)):
            total_days+=2
        if(near_holiday(day)):
            total_days=+1
        if(near_holiday(end1)):
            total_days+=1
        if max_days < total_days:
            max_days = total_days
            best_start1 = day
            best_end1 = end1
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
