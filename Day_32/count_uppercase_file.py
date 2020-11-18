# Title  : Count uppercase, lowercase letters in file
# Author : Kiran Raj R.
# Date   : 15/11/2020

import string

with open ('content.txt') as file:
    chars = 0
    countUpper = 0
    countLower = 0
    countDigit = 0
    countPunctuation = 0
    for line in file:
        line = line.strip();
        for word in line.split():
            for ch in word:
                chars+=1
                if ch in string.ascii_uppercase:
                    countUpper+=1
                elif ch in string.ascii_lowercase:
                    countLower+=1
                elif ch in string.digits:
                    countDigit+=1
                elif ch in string.punctuation:
                    countPunctuation+=1

    print(f"Number of characters in the file is: {chars}")
    print(f"Number of upper case letters in the file is: {countUpper}")
    print(f"Number of lower case letters in the file is: {countLower}")     
    print(f"Number of digits in the file is: {countDigit}")
    print(f"Number of punctuations in the file is: {countPunctuation}")

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(string.digits)
# print(string.whitespace)