# Title  : Print capitals of user inputed countries
# Author : Kiran raj R.
# Date   : 20:10:2020

from tkinter import Tk, simpledialog, messagebox
world = {}

print('Capital cities of the world')
main = Tk()
main.withdraw()


def read_from_file():
    with open('capital.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            country = country.strip().lower()
            city = city.strip().lower()
            world[country] = city


def write_to_file(country_name, city_name):
    with open('capital.txt', 'a') as file:
        file.write('\n' + country_name + ' / ' + city_name)


read_from_file()

while True:
    query = simpledialog.askstring('Country', 'Type the name of a country:')
    if query in world:
        result = world[query]
        messagebox.showinfo(
            'Answer', f'The capital city of {query.upper()} is {result.upper()}')
    else:
        new_city = simpledialog.askstring(
            'Teach me', f"What's the capital of {query} ?")
        write_to_file(query, new_city)


main.mainloop()
