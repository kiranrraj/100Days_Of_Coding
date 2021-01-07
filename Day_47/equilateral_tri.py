# Title  : Equilateral triangle or not
# Author : Kiran Raj R.
# Date   : 30/11/2020

import math
side, area, perimeter, semi_p, altitude = 0.0, 0.0, 0.0, 0.0, 0.0

side = float(input("Enter a side of an triangle: "))

area = ( math.sqrt(3) / 4) * (side **2)
perimeter = 3 * side
altitude = (math.sqrt(3) / 2) * side

print(f"Perimeter of a equilateral triangle with side, {side}: {perimeter:.2f}")
print(f"Semi Perimeter of a equilateral triangle with side, {side}: {(perimeter / 2):.2f}")
print(f"Area of a equilateral triangle with side {side}: {area:.2f}")
print(f"Altitude of a equilateral triangle with side {side}: {altitude:.2f}")