# Title  : Caesar Cipher with decode option
# Author : Kiran Raj R.
# Date   : 02:11:2020

import string


def shift_n(char, key):
    char = char.lower()
    if char not in string.ascii_lowercase:
        return char
    cipher = ord(char) + key
    print(cipher)
    if cipher > 123:
        cipher -= 26
    return chr(cipher)


def caesar(message, key):
    encoded_text = [shift_n(char, key) for char in message]
    return "".join(encoded_text)


print(caesar("hello world", 5))


def decode_char(c_char, key):
    c_char = c_char.lower()
    decode_text = []
    if c_char not in string.ascii_lowercase:
        return c_char
    d_char = ord(c_char) - key

    if d_char < 96:
        d_char += 26

    return chr(d_char)


def decode_text(message, key):
    text = [decode_char(char, key) for char in message]
    return "".join(text)


print(decode_text("mjqqt btwqi", 5))
