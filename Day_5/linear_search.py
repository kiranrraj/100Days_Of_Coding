# Title  : Linear Search
# Author : Kiran raj R.
# Date   : 19:10:2020


user_list = []

try:
    print("Enter a array of numbers to search from (one at each time):")
    user_len = int(input("Enter the lenght of the array : "))
    
except ValueError:
    print(f"Make sure you enter a number")
    exit(1)

def getNum(length):
    for index in range(length):
        userInput = input(">>>")
        user_list.append(userInput)
    return user_list

def linearSearch(item):
    for elem in user_list:
        if elem == item:
            return (f"'{item}' found in {user_list}")
    return(f"'{item}' not found !!!")

getNum(user_len)
user_search = input("Enter the element to search : ")

print(linearSearch(user_search))