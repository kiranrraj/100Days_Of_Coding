userInput = input("Enter a string to remove dupicate :").strip()


def removeDuplicate(num):
    num =list(num)
    newList = []
    length = len(num)
    index = 0

    for i in range(length):
        for j in range(0, i+1):
            if num[i] == num[j]:
                break
        if i == j:
            print(j)
            newList.append(num[i])
            index+=1

    return newList

print(removeDuplicate(userInput))