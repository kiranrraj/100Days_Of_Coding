# Title  : Print second saturdays
# Author : Kiran raj R.
# Date   : 29:10:2020


import calendar

for month in range(1, 13):
    weeks = calendar.monthcalendar(2020, month)
    first_week = weeks[0]
    second_week = weeks[1]
    third_weeks = weeks[2]

    if first_week[calendar.SATURDAY]:
        second_sat = second_week[calendar.SATURDAY]
    else:
        second_sat = third_weeks[calendar.SATURDAY]

    print(f"Second saturday of {calendar.month_name[month]} is {second_sat}")
