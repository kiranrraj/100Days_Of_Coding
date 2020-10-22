# Title  : Remove Duplicate
# Author : Kiran raj R.
# Date   : 21:10:2020


userInput = input("Enter a string to remove dupicate :").strip()

def removeDuplicate(num):
    num =list(num)
    newList = []
    length = len(num)

    for i in range(length):
        for j in range(0, i+1):
            if num[i] == num[j]:
                break
        if i == j:
            newList.append(num[i])

    return " ".join(newList)

print(removeDuplicate(userInput))