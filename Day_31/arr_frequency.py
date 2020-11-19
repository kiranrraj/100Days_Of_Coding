# Title  : Element frequency in an array
# Author : Kiran Raj R.
# Date   : 14/11/2020

arr1 = [23,1,2,2,3,4,3,1,4,2,3,5,3,4,0]
arr1_freq = [None] * len(arr1)
flag = -1

for i in range(0, len(arr1)):
    count = 1
    for j in range(i+1, len(arr1)):
        if arr1[i] == arr1[j]:
            count+=1
            arr1_freq[j] = flag

    if arr1_freq[i] != flag:
        arr1_freq[i] = count

for i in range(len(arr1)):
    if arr1_freq[i] != -1:
        print(f"{arr1[i]} ---> {arr1_freq[i]}")
    

