# Title  : Find words with specified length
# Author : Kiran Raj R.
# Date   : 15/11/2020

def words_with_length():
    userValue = int(input("Enter the length of the word: ").strip())
    if userValue == "" or userValue == 0:
        print("Please try again with a number greater than zero")
        return
    with open ('content.txt') as file:
        count = 0
        for line in file:
            for word in line.split():
                if len(word) == userValue:
                    count+=1
                    print(word)
        if count ==0:
            print(f"Could not found words with length {userValue} in the file.")
        else:
            print(f"Number of words with length {userValue} is {count}")

words_with_length()