# Title  : Calculate age in years
# Author : Kiran raj R.
# Date   : 29:10:2020

from datetime import date


def calculate_myAge(dob):
    today = date.today()
    # print((today.month, today.day) < (dob.month, dob.day))
    my_age = today.year - dob.year - \
        ((today.month, today.day) < (dob.month, dob.day))
    print(my_age)


calculate_myAge(date(1988, 4, 19))
