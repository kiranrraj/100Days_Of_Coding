# Title  : Find the least frequent
# Author : Kiran raj R.
# Date   : 22:10:2020

userInput = input("Enter a string to find the least frequent element: ")

freq_dist = {}

for char in userInput:
    if char in freq_dist:
        freq_dist[char] += 1
    else:
        freq_dist[char] = 1
result = min(freq_dist, key= lambda v: freq_dist[v])

print(f"The least frequent element in '{userInput}' is : {result}")
