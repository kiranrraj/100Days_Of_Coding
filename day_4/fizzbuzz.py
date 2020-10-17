# Title  : FizzBuss
# Author : Kiran raj R.
# Date   : 18:10:2020

try:
    userinput = int(input("Enter a limit to print : "))
except:
    print("Enter a whole number")
    exit(1)


for num in range(1,userinput):

    if num % 3 == 0 and num % 5 == 0:
        print("Fizzbuzz")
        continue
    elif num % 3 == 0 :
        print("Fizz")
        continue
    elif num % 5 == 0 :
        print("Buzz")
        continue
    else:
        print(num)

