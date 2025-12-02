#!/usr/bin/env python3

from __init__ import CONN, CURSOR
# from department import Department
from employee import Employee

import ipdb

# Department.drop_table()
# Department.create_table()

# payroll = Department.create("Payroll", "Building A, 5th Floor")
# print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

# hr = Department.create("Human Resources", "Building C, East Wing")
# print(hr)  # <Department 2: Human Resources, Building C, East Wing>

# hr.name = 'HR'
# hr.location = "Building F, 10th Floor"
# hr.update()
# print(hr)  # <Department 2: HR, Building F, 10th Floor>


Employee.drop_table()
Employee.create_table()

emp1 = Employee.create("Joseph Chai", "Software Engineer", 75000)
print(emp1)

emp2 = Employee.create("Jane Samuel", "HR Manager", 65000)
print(emp2)

emp3 = Employee.create("Fatma", "Data Analyst", 70000)
print(emp3)

emp4 = Employee.create("Fatma Ahmed", "Marketing Manager", 68000)
print(emp4)

emp5 = Employee.create("Fatma Hassan", "Finance Manager", 72000)
print(emp5)

emp6 = Employee.create("Brian Kamotho", "Project Manager", 80000)
print(emp6)


ipdb.set_trace()

