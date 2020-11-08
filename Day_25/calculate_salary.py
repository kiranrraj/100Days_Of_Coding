# Title  : Python inheritance # Calculate_salary file #
# Author : Kiran Raj R.
# Date   : 08:11:2020


import hr_payroll

weekly_emp = hr_payroll.WeeklyEmployee(121, 'John Doe', 15000)
hourly_emp = hr_payroll.HourlyEmployee(125, "Manoj", 12, 300)
sales_emp = hr_payroll.SalesEmployee(221, "Salah", 15000, 5000)
pay = hr_payroll.Payroll()
pay.calculate_pay([
    weekly_emp,
    hourly_emp,
    sales_emp
])