# Title  : Mean, median Mode of a list of numbers
# Author : Kiran raj R.
# Date   : 16:10:2020

import math

a = [1, 2, 3, 4, 5]
b = [2, 4, 5, 7, 3, 8]


def findMean(num):
    """Find the mean of a list of numbers"""

    length = len(num)
    sumList = sum(num)
    return f"Mean value of {num} is {round((sumList / length) ,2)}"


def findMedian(num):
    """Find the median of a list of numbers"""
    num.sort()
    length = len(num)
    if length % 2 == 0:
        midindex1 = int(length/2)
        midindex2 = int((length/2)-1)
        midElem1 = num[midindex1]
        midElem2 = num[midindex2]
        # print(length/2, (length/2)-1)
        return f"The middle elements are {midElem2} and {midElem1}.Median is {(midElem1+midElem2)/2}"
    else:
        index = int(math.floor(length/2))
        return f"The middle element is {num[index]} "


def countNum(num, elem):
    """Return the occurance of a given number in the specified list of numbers"""
    countNum = 0
    for i in range(len(num)):
        if elem == num[i]:
            countNum += 1
    return countNum


def findMode(num):
    """Find the mode of a list of numbers"""
    newlist = []
    cntlist = []
    newlist.append(num[0])

    # Removing duplicate => set(num)
    for i in num:
        if not (i in newlist):
            newlist.append(i)
    print(newlist)

    # Creating mode list => num.count
    for i in newlist:
        cnt = countNum(num, i)
        cntlist.append(cnt)
    print(cntlist)

    # Finding the most repeated num
    large = cntlist[0]
    pos = 0
    for i in range(len(cntlist)):
        if large < cntlist[i]:
            large = cntlist[i]
            pos = i
    return f"Mode is {newlist[pos]}"


def quick(num):
    return f"Mode is {max(set(num), key=num.count)}"


print("----------------------")
print(findMean(a))
print(findMean(b))
print(findMedian(a))
print(findMedian(b))
print(findMode([2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 1, 2,
                7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]))
print(quick([2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 1, 2,
             7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]))
