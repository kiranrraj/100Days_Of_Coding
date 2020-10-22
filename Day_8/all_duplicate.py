# Title  : Print all duplicate elements
# Author : Kiran raj R.
# Date   : 22:10:2020

userInput = input("Enter a string to find the highest frequent element: ")

freq_dist = {}
result = []

for char in userInput:
    if char in freq_dist:
        freq_dist[char] += 1
    else:
        freq_dist[char] = 1

for key, val in freq_dist.items():
    if val > 1:
        result.append(key)

print(f"The duplicate letters in the '{userInput}' is : {', '.join(result)}")


