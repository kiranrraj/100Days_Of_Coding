# Title  : Create count down app using tkinter
# Author : Kiran raj R.
# Date   : 20:10:2020

import tkinter
from datetime import date, datetime

vertical_space = 100


def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events


def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(" ")
    return number_of_days[0]


root = tkinter.Tk()
root.title("Count down clock")
c = tkinter.Canvas(root, width=600, height=600, bg='black')
c.pack()
c.create_text(100, 50, anchor='w', fill='orange',
              font='Arial 28 bold underline', text='My Countdown Calendar')

events = get_events()
events.sort(key=lambda x: x[1])
today = date.today()

for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = f"It is {days_until} days until {event_name}"
    if int(days_until) <= 100:
        fill_color = "red"
    else:
        fill_color = "yellow"
    c.create_text(100, vertical_space, anchor='w', fill=fill_color,
                  font='Arial 18 bold underline', text=display)
    vertical_space = vertical_space + 30
root.mainloop()
