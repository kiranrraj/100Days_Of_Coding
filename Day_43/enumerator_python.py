# Title  : Enumerator
# Author : Kiran Raj R.
# Date   : 26/11/2020

list_1 = ['aa', 'bb', 'cc', 'dd']
index = 0

for key in list_1:
    print(f"key:{key}  index:{index}")
    index+=1

print("-" * 100)

for index_1 in range(len(list_1)):
    print(f"key:{list_1[index_1]}  index:{index_1}")

print("-" * 100)

for count, val in enumerate(list_1):
    print(f"key:{val}  index:{count}")

print("-" * 100)

for count_1, val_1 in enumerate(list_1, start=2):
    print(f"key:{val_1}  index:{count_1}")