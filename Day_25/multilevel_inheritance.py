# Title  : Multilevel Inheritance
# Author : Kiran Raj R.
# Date   : 08:11:2020

class Employee:
    def __init__(self, emp_id, name, basicSalary, position):
        self.emp_id = emp_id
        self.name = name
        self.basicSalary = basicSalary
        self.position = position

    def print_details(self):
        print(f"ID: {self.emp_id}\nName: {self.name}\nSalary: {self.basicSalary}\nPosition: {self.position}")

class SalesTeam(Employee):
    def __init__(self, emp_id, name, basicSalary, position, target):
        Employee.__init__(self, emp_id, name, basicSalary, position)
        self.target = target
        self.position = "Sales"

    def calcSalary(self):
        if self.target == True:
            self.basicSalary = self.basicSalary *1.2

class SalesManager (SalesTeam):
    def __init__(self, emp_id, name, basicSalary, target, bonus):
        SalesTeam.__init__(self, emp_id, name, basicSalary, position="Sales Manager", target=True) 
        self.bonus = bonus
        self.position = "Sales Manager"

    def calcBonus(self):
        self.calcSalary()
        if self.bonus == True:
            self.basicSalary= self.basicSalary * 11.2

emp1 = Employee(121, "Kiran", 45000, "asst_store keeper")
emp1.print_details()
print("-----------------------------------------------------")
st1 = SalesTeam(121, "Kiran", 45000, "asst_store keeper", True)
st1.calcSalary()
st1.print_details()
print("-----------------------------------------------------")
sm = SalesManager(121, "Kiran", 45000, True, False)
sm.calcBonus()
sm.print_details()