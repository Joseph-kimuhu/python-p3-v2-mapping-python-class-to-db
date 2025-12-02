#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from employee import Employee

# Find Brian and update his data
employees = CURSOR.execute('SELECT * FROM employees WHERE name = "Brian Kamotho"').fetchall()
if employees:
    brian_data = employees[0]
    brian = Employee(brian_data[1], brian_data[2], brian_data[3], brian_data[0])
    
    # Update Brian's details
    brian.position = "Senior Project Manager"
    brian.salary = 90000
    brian.update()
    
    print(f"Updated: {brian}")
else:
    print("Brian Kamotho not found")