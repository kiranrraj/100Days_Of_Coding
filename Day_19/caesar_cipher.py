# Title  : Caesar Cipher on text input
# Author : Kiran Raj R.
# Date   : 02:11:2020

import string

user_msg = input("Enter your message: ")


def caesar_cipher(text, shift):
    letters = string.ascii_lowercase
    mask = letters[shift:] + letters[:shift]
    coverText = str.maketrans(letters, mask)
    return text.translate(coverText)


print(caesar_cipher(user_msg, 2))
