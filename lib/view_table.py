#!/usr/bin/env python3

from __init__ import CONN, CURSOR

# Query the departments table
departments = CURSOR.execute('SELECT * FROM departments').fetchall()

print("Departments Table:")
print("ID | Name | Location")
print("-" * 40)

for dept in departments:
    print(f"{dept[0]} | {dept[1]} | {dept[2]}")