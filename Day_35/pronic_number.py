# Title  : Disarium number
# Author : Kiran Raj R.
# Date   : 18/11/2020

def is_pronic(num):
    if num == 0 :
        print("Please enter a value higher than 0")
        return
    else:
        for i in range(1, num+1):
            if i * (i+1) == num:
                print(f"Pronic number: {num}")
                return

for i in range(100):
    if is_pronic(i):
        print(f"Pronic number : {i}")