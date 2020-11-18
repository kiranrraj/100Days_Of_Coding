# Title  : Generator function
# Author : Kiran Raj R.
# Date   : 14/11/2020

def my_generator():
    n = 1
    print(f"This is a generator's first message: {n}");
    yield n

    n += 1
    print(f"This is a generator message: {n}");
    yield n

    n+=1
    print(f"This is a generator message: {n}");
    yield n

    print(f"This is a generator's last message: {n}");


for i in my_generator():
    print(i)
