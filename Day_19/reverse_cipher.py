# Title  : Reverse Cipher
# Author : Kiran Raj R.
# Date   : 02:11:2020

user_msg = input("Enter the message to encrypt: ")


def encrypt(msg):
    encrypted_msg = ""
    length_msg = len(msg) - 1

    while length_msg >= 0:
        encrypted_msg += msg[length_msg]
        length_msg -= 1
    return encrypted_msg


print(f"The encrypted message is {encrypt(user_msg)}")
