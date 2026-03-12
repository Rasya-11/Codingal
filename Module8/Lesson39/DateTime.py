# Create a program to display today’s date, time, hour, mins, second, and calendar year in 3 columns.

import datetime
import calendar

currentTime = datetime.datetime.now()
print("Time now at Greenwhich meridian is", currentTime)
print(calendar.calendar(2026))