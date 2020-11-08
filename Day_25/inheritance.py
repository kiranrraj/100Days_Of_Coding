# Title  : Inheritance
# Author : Kiran Raj R.
# Date   : 08:11:2020

import math

class Polygon:
    "Create a simply polygon class, which takes number of sites and takes the maginute of each sides"
    def __init__(self, num_sides):
        self.num_sides = int(num_sides)
        self.mag_sides = []
    
    def get_sides(self):
        self.mag_sides = [float(input(f"Enter the value for side {i+1}: ")) for i in range(self.num_sides)]
    
    def print_sides(self):
        if len(self.mag_sides) == 0:
            print("No sides entered")
            return
        print(f"The polygon have {self.num_sides} sides")
        for i in range(self.num_sides):
            print(f"The side {i+1} is {self.mag_sides[i]}")


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    
    def findArea(self):
        a,b,c = self.mag_sides
        # print(self.mag_sides)
        sum_s = (a+b+c) / 2
        # print(sum_s)
        product = sum_s * ((sum_s-a) * (sum_s-b) * (sum_s-c))
        area = math.sqrt(product)
        print(f"The area of the triangle with sides {a}, {b}, {c} is {area}")

# triangle = Polygon(3)
# # triangle.get_sides()
# # triangle.print_sides()
triangle1 = Triangle()
triangle1.get_sides()
triangle1.findArea()
