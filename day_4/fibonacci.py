# Title  : Fibonacci
# Author : Kiran raj R.
# Date   : 18:10:2020

def fibonacci(num):
    output=[]
    f1 =0
    f2 =1
    output.extend((f1,f2))
    for i in range(num-2):
        sum = f1 + f2
        f1 = f2
        f2 = sum
        output.append(sum)
    return output
    

try:
    userInput = input("Enter the number of elements you need in a fibonacci series : ")
    limit = int(userInput)
    print(f"Fibonacci series with {limit} elements => {fibonacci(limit)}")
except:
    print("Please enter a valid number with no decimal places")