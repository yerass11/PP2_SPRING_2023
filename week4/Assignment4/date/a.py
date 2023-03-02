"""Python date


2.
3.

4.
"""

import datetime

#1
#Write a Python program to subtract five days from current date.

print("1. ")
dt = datetime.date.today() - datetime.timedelta(5)

print('Current Date :',datetime.date.today())
print('5 days before Current Date :',dt)

print()

#2
#Write a Python program to print yesterday, today, tomorrow.

print("2. ")
yestr = datetime.date.today() - datetime.timedelta(1)
tmmrw = datetime.date.today() + datetime.timedelta(1)
print('Yesterday : ', yestr)
print('Today :', datetime.date.today())
print('Tomorrow :', tmmrw)

print()

#3
#Write a Python program to drop microseconds from datetime.

print("3. ")
x = datetime.datetime.today().replace(microsecond = 0)
print(x)

print()

#4
#Write a Python program to calculate two date difference in seconds.

print("4. ")

def date_diff_in_Seconds(date2, date1):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
y = input()#2015-01-01 01:00:00
date1 = datetime.datetime.strptime(y, '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()

print(date1)
print(date2)