# Title  : Print details about today
# Author : Kiran raj R.
# Date   : 29:10:2020

import datetime
import time

print(f"Today is : { datetime.datetime.now().strftime('%y/%m/%d')}")
print(f"Day : {datetime.date.today().strftime('%A')}")
print(f"Name of month : {datetime.date.today().strftime('%B')}")
print(f"Day of the year : {datetime.date.today().strftime('%j')}")
print(f"Week of the year : {datetime.date.today().strftime('%W')}")
