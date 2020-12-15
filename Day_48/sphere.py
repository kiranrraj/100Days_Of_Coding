PI = 3.14

print("Enter 's' to calculate volume of Sphere")
print("Enter 'c' to calculate volume of Cylinder")

choice = input().lower()

if choice == 's' :
    radius = float(input('Enter the Radius of a Sphere: '))
    s_area =  4 * PI * radius * radius
    vol = (4 / 3) * PI * radius * radius * radius

    print(f"The Surface area of a Sphere: {s_area:.2f}")
    print(f"The Volume of a Sphere: {vol:.2f}")

elif choice == 'c':
    radius = float(input('Enter the Radius of a Cylinder: '))
    height = float(input('Enter the Height of a Cylinder: '))

    s_area = 2 * PI * radius * (radius + height)
    vol = PI * radius * radius * height
    l_s_area = 2 * PI * radius * height
    t_area = PI * radius * radius

    print(f"The Surface area of a cylinder: {s_area:.2f}")
    print(f"The Volume of a cylinder: {vol:.2f}")
    print(f"Lateral Surface Area of a cylinder: {l_s_area:.2f} ")
    print(f"Top / Bottom Surface Area of a cylinder: {t_area:.2f}")

else:
    print("Sorry, option not found")
    exit()