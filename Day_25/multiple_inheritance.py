# Title  : Multiple Inheritance
# Author : Kiran Raj R.
# Date   : 08:11:2020


class EmployeeDetail:
    def __init__(self, emp_id, name, age, email_id, position):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email_id = email_id
        self.position = position
    
    def print_details(self):
        print(f"ID: {self.emp_id}\nName: {self.name}\nAge: {self.age}\nEmail: {self.email_id}\nPosition: {self.position}")

class EmployeeSalary:

    salary = 0

    def __init__(self, basic, da, target=False, bonus=False):
        self.basic = basic
        self.da = da
        self.target = target
        self.bonus = bonus
        
    def calcSalary(self):
        self.salary = self.basic + (self.basic * self.da)
        if self.target == True:
            self.salary = self.basic+ self.basic *10
            return self.salary
        else:
            return self.salary

class Employee(EmployeeDetail, EmployeeSalary):
    def __init__(self, emp_id, name, age, email_id, positon, basic, da, target=False, bonus=False ):
        EmployeeDetail.__init__(self, emp_id, name, age, email_id, positon)
        EmployeeSalary.__init__(self, basic, da, target, bonus)

emp1 = Employee(121, "kiran", 32, "kiran@g.com", "sales_manager", 22000, 5000, True, True)
