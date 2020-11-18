# Title  : Scramble Words
# Author : Kiran Raj R.
# Date   : 15/11/2020

import random, string
new_word =""

with open ('content.txt') as file:
    count = 0
    for line in file:
        for word in line.split():
            count+=1
            if len(word) >= 4:
                if word[0] == string.ascii_letters and word[-1] == string.ascii_letters:
                    scramble_part = word[1:-1]
                    front = word[0]
                    last = word[-1]
                    scramble = scramble_word(scramble_part)
                    word = front + scramble + last
                elif word[0] == string.ascii_letters and word[-1] != string.ascii_letters:
                    scramble_part = word[1:-2]
                    front = word[0]
                    last = word[-2::]
                    scramble = scramble_word(scramble_part)
                    word = front + scramble + last
                elif word[0] != string.ascii_letters and word[-1] == string.ascii_letters:
                    scramble_part = word[2:-1]
                    front = word[0:2]
                    last = word[-1]
                    scramble = scramble_word(scramble_part)
                    word = front + scramble + last
                elif word[0] != string.ascii_letters and word[-1] != string.ascii_letters:
                    scramble_part = word[2:-2]
                    front = word[0:2]
                    last = word[-2::]
                    scramble = scramble_word(scramble_part)
                    word = front + scramble + last
            print(word)
    print(f"Number of words in the file is: {count}")

def scramble_word(word):
    new_word = "".join(random.choice(word))
    return new_word