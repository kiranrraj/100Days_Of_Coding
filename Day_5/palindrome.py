# Title  : Palindrome
# Author : Kiran raj R.
# Date   : 19:10:2020

userInput = input("Enter a number or word to check whether it is palinfrome or note :").strip()
reverse_ui = userInput[-1::-1]

# if userInput == reverse_ui:
#     print(f"'{userInput}' is a palindrome")
# else:
#     print(f"'{userInput}' is not a palindrome")

print(f"'{userInput}' is a palindrome") if userInput == reverse_ui else print(f"'{userInput}' is not a palindrome")