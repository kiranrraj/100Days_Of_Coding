# Title  : Triangle or not
# Author : Kiran Raj R.
# Date   : 30/11/2020

angles = []
total = 0

for i in range(3):
    val = float(input(f"Enter the angle of side {i}: "))
    angles.append(val)

total = sum(angles);
# print(total)
if total == 180 and angles[0] != 0 and angles[1] != 0 and angles[2] != 0:
    print("Valid angles for a triangle") 
else:
    print("Provided angles cannot form a triangle") 