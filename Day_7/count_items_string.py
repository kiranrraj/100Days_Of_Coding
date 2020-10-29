# Title  : Find the number of upper, lower, numbers in a string
# Author : Kiran raj R.
# Date   : 21:10:2020

import string


def count_items(words):

    word_list = words.split()
    upper_count = lower_count = num_count = special_count = 0
    length_wo_space = 0

    for word in words:
        word = word.rstrip()
        length_wo_space += len(word)

        for index in range(len(word)):
            if word[index].isupper():
                upper_count += 1
            if word[index].islower():
                lower_count += 1
            if word[index] in string.punctuation:
                special_count += 1
            if word[index].isnumeric():
                num_count += 1

    print(f"User entered string is: {words}")
    print(f"Total length is {length_wo_space}\nSmall letters in string: {lower_count}\nCapital letters in string: {upper_count}\nSpecial characters in string: {special_count}\nNumbers count in string: {num_count}")


count_items("kiran raj r 12345 ,!# QWERR")
