import math

width = float(input("Enter the width length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

third_side = math.sqrt((width**2) + (height**2))
perimeter = third_side + height+ width

area = 0.5 * width * height

print(f"Area of triangle with width ({width}) and height ({height}): {area:.2f}")
print(f"Perimeter of triangle with sides [ {height}, {width}, {third_side:.2f}]: {perimeter:.2f}")