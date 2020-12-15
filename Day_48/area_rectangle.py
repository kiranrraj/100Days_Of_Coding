length, width, area = 0.0, 0.0, 0.0
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Perimeter of rectangle with length ({length}) and width ({width}): {perimeter:.2f}")
print(f"Area of rectangle with length ({length}) and width ({width}): {area:.2f}")