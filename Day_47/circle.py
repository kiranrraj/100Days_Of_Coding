# Title  : Circle or not
# Author : Kiran Raj R.
# Date   : 30/11/2020

PI = 3.14
radius, area, circum = 0.0, 0.0, 0.0

radius = float(input("Enter the radius of the circle: "))
area = PI * radius ** 2
circum = 2 * PI * radius

print(f"Diameter of circle with radius {radius}: {radius * 2}")
print(f"Area of circle with radius {radius}: {area}")
print(f"Circumference of circle with radius {radius}: {circum:.2f}")