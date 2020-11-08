# Title  : Python inheritance # HR payroll file #
# Author : Kiran Raj R.
# Date   : 08:11:2020

class Payroll:
    def calculate_pay(self, employees):
        print("Calculating Payroll")
        for employee in employees:
            print(f"Salary for: {employee.id} - {employee.name}")
            print(f"--Check Amount: {employee.calculate_pay()}")
            print()


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class WeeklyEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id,name)
        self.weekly_salary = weekly_salary

    def calculate_pay(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours, rate):
        super().__init__(id, name)
        self.hours = hours
        self.rate = rate

    def calculate_pay(self):
        return self.hours * self.rate


class SalesEmployee(WeeklyEmployee):
    def __init__(self, id, name, weekly_salary, bonus):
        super().__init__(id, name, weekly_salary)
        self.bonus = bonus

    def calculate_pay(self):
        fixed = super().calculate_pay() + self.bonus
        return fixed 