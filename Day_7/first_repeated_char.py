# Title  : First repeated character
# Author : Kiran raj R.
# Date   : 21:10:2020

def first_repeat_char(word):
    flag = False
    for index, char in enumerate(word):
        # print(index, char)
        if word[:index+1].count(char) > 1:
            print(f"First repeated character in '{word}' is '{char}'")
            flag = True
            break
    if not flag:
        print(f"Sorry, no repeating character in '{word}'.")


first_repeat_char("kiranrajr")
first_repeat_char("kiran")
