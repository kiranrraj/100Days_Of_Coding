# Title  : Symmetrical
# Author : Kiran raj R.
# Date   : 19:10:2020

userInput = input("Enter a string to check whether it is symmetrical or not : ")

def symmetrical(word):
    length = len(word)
    if length%2 != 0:
        return f"'{word}' is not symmetrical"
    else:
        half = int(length / 2)
        output = f"'{word}' is symmetrical" if word[:half] == word[half:] else f"'{word}' is not symmetrical"
    return output
            
print(symmetrical(userInput))
