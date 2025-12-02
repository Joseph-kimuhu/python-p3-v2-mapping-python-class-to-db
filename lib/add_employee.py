#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from employee import Employee

# Add new employee
new_emp = Employee.create("Fatma Hassan", "Finance Manager", 72000)
print(f"Added: {new_emp}")

# View all employees table
employees = CURSOR.execute('SELECT * FROM employees').fetchall()
print("\nEmployees Table:")
print("ID | Name | Position | Salary")
print("-" * 40)
for emp in employees:
    print(f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]}")