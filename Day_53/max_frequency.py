# Title  : Find the max frequent element
# Author : Kiran raj R.
# Date   : 22:10:2020

userInput = input("Enter a string to find the highest frequent element: ")

freq_dist = {}

for char in userInput:
    if char in freq_dist:
        freq_dist[char] += 1
    else:
        freq_dist[char] = 1
result = max(freq_dist, key= lambda v: freq_dist[v])

print(f"The most frequent element in '{userInput}' is : {result}")