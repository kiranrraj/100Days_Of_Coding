# Title  : Count all upper and lower letter in a sentence.  
# Author : Kiran raj R.
# Date   : 23:10:2020

userInput = input("Enter a sentence : ").strip()

word_list = userInput.split()
words = "".join(word_list)
length = len(words)
upper = 0
lower = 0

for char in userInput:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1

print(f"Length of sentence {length}")
print(f"Number of upper case letters is {upper}")
print(f"Number of lower case letters is {lower}")