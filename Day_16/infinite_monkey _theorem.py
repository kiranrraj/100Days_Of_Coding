# Title  : Infinite monkey theorem
# Author : Kiran raj R.
# Date   : 29:10:2020

import random
import string


def generate_string(length):

    characters = string.ascii_lowercase + " "
    out_str = ""
    for i in range(length):
        out_str += random.choice(characters)

    # print(f"{length} -- {out_str}")
    return out_str


def find_score(user_str, str_in):
    score = 0
    length = len(user_str)-1
    for i in range(length):
        if user_str[i] == str_in[i]:
            score += 1

    return score


def infinite_type():
    user_string = "hello world"
    req_length = len(user_string)
    generated_str = generate_string(req_length)
    best_score = 0
    new_score = find_score(user_string, generated_str)

    while new_score < req_length:
        if new_score > best_score:
            best_score = new_score
            print(generated_str, best_score)

        generated_str = generate_string(req_length)
        new_score = find_score(user_string, generated_str)


infinite_type()
