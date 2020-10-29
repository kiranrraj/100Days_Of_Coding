# Title  : Create an Enum
# Author : Kiran raj R.
# Date   : 21:10:2020

from enum import Enum


class CountryCaps(Enum):
    ICELAND = 'REYKJAVIK'
    INDIA = 'NEW_DELHI'
    INDONESIA = 'JAKARTA'
    IRAN = 'TEHRAN'
    IRAQ = 'BAGHDAD'
    IRELAND = 'DUBLIN'
    ISRAEL = 'JERUSALEM'
    ITALY = 'ROME'


country_list = []

for item in CountryCaps:
    print(
        f"[-----------------]\nCountry : {item.name}\nCapital : {item.value}")
    country_list.append(item.name)

print(f"Countries : {country_list}")
