import re
userInput = input("Enter a password to check the strength: ").strip()

if len(userInput) < 6:
    print("The password must contain 6 characters")
elif not re.search("[a-z]", userInput):
    print("The password must contain characters")
elif not re.search("[0-9]", userInput):
    print("The password must contain digit(s)")
elif not re.search("[A-Z]", userInput):
    print("The password must contain uppercase letter(s)")
elif not re.search("[$#@]", userInput):
    print("The password must contain special character(s)")
else:
    print("Your password is strong")
