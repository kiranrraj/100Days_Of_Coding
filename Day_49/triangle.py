area, perimeter = 0.0, 0.0
sides=[]

for i in range(3):
    val = float(input(f"Enter the length of side {i}: "))
    sides.append(val)

perimeter = sum(sides)
s = perimeter / 2
area =  ( s * ((s - sides[0]) * (s - sides[1]) * (s - sides[2]))) ** 0.5
print(f"Area of triangle with sides, [{sides[0]}, {sides[1]}, {sides[2]}] : {area:.2f}")
print(f"Perimeter of triangle with sides, [{sides[0]}, {sides[1]}, {sides[2]}] : {perimeter:.2f}")