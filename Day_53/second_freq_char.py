# Title  : Second most repeated character
# Author : Kiran raj R.
# Date   : 21:10:2020

def second_frequent_char(word):
    char_dict = {}

    for i in range(len(word)):
        if word[i] in char_dict:
            char_dict[word[i]] += 1
        else:
            char_dict[word[i]] = 1

    sort_dict = sorted(char_dict.items(), key=lambda val: val[1])

    if sort_dict[-2][1] > 1:
        print(
            f"THe second most repeated character in {word} is {sort_dict[-2][0]}, {sort_dict[-2][1]} time(s)")
    else:
        print(f"There is not second repeated character in {word}")


second_frequent_char("kiranrajr")
