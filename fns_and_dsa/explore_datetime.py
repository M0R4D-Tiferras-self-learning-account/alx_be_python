#!/usr/bin/env python3

import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date:%Y-%m-%d %H:%M:%S}")

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    current_date = datetime.datetime.now()
    delta_days = datetime.timedelta(days=number_of_days) 
    future_date = current_date + delta_days
    print(f"future date: {future_date.strftime('%Y-%m-%d')}")
calculate_future_date()

