# Title  : Generate a password with uppercase letters, digit and symbols
# Author : Kiran raj R.
# Date   : 28:10:2020


import random
import string


def create_pass():
    all_letters = string.ascii_letters + string.digits + string.punctuation
    word = random.sample(all_letters, 5)
    word += random.sample(string.ascii_uppercase, 1)
    word += random.choice(string.digits)
    word += random.sample(string.punctuation, 1)

    wordList = list(word)
    random.SystemRandom().shuffle(wordList)
    pswd = "".join(wordList)
    return pswd


print(f"Password generated is : {create_pass()}")
