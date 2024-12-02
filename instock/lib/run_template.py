#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import datetime
import pandas as pd

def get_run_date_list():
    """
    Common function to get date parameters, supports batch processing.
    Returns a list of dates to process.
    """
    run_date_list = []
    
    # If no arguments provided, use current date
    if len(sys.argv) == 1:
        run_date_list.append(datetime.datetime.now().strftime("%Y-%m-%d"))
        return run_date_list
    
    # Interval job: python xxx.py 2023-03-01 2023-03-21
    if len(sys.argv) == 3:
        start_date = datetime.datetime.strptime(sys.argv[1], "%Y-%m-%d")
        end_date = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d")
        date_range = pd.date_range(start=start_date, end=end_date)
        for date in date_range:
            run_date_list.append(date.strftime("%Y-%m-%d"))
        return run_date_list
    
    # Multiple dates job: python xxx.py 2023-03-01,2023-03-02
    if "," in sys.argv[1]:
        dates = sys.argv[1].split(",")
        for date in dates:
            run_date_list.append(date)
        return run_date_list
    
    # Current date job: python xxx.py
    run_date_list.append(sys.argv[1])
    return run_date_list
