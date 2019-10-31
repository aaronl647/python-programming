#Create an program that calculates the number of hours worked

import time
from datetime import datetime, timedelta

#Gets user input of how many shift user worked
days_worked = int(input("How many shifts did you work? "))

#stores dates of when you worked
day_list = []
for i in range(days_worked): 
    dates = input("List the dates you worked. ")
    day_list.append(dates)

#Gets start and end times for each shift and then saves all the hours into a list
sum_time = []
for i in range(days_worked): 
    s1 = input("When did you start? Please enter 'Hour:Minute' in 24H format. ")
    s2 = input("When did you end? Please enter 'Hour:Minute' in 24H format. ")
    FMT = '%H:%M'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)

    if tdelta.days < 0:
        tdelta = timedelta(days=0, seconds=tdelta.seconds, microseconds=tdelta.microseconds)
    t_min=tdelta.seconds/60
    t_hr=t_min/60
    sum_time.append(t_hr)
#adds the 2 lists together to make a dictionary of the 
work_final = dict(zip(day_list, sum_time))

print(work_final)
print("You worked a total of ", sum(sum_time), " hours.")