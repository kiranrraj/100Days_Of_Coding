area, base, height = 0.0, 0.0, 0.0

base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = (base * height) / 2

print(f"Area of triangle with base ({base}) and height ({height}): {area:.2f}")