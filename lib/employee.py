from __init__ import CURSOR, CONN


class Employee:

    def __init__(self, name, position, salary, id=None):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"<Employee {self.id}: {self.name}, {self.position}, ksh {self.salary}>"

    @classmethod
    def create_table(cls):
        """Create a table to store employee records."""
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            position TEXT,
            salary INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the employees table."""
        sql = "DROP TABLE IF EXISTS employees;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Save employee to database."""
        sql = """
            INSERT INTO employees (name, position, salary)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.position, self.salary))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, position, salary):
        """Create and save new employee."""
        employee = cls(name, position, salary)
        employee.save()
        return employee

    def update(self):
        """Update this employee's record in the database."""
        sql = """
            UPDATE employees
            SET name = ?, position = ?, salary = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.position, self.salary, self.id))
        CONN.commit()

    def delete(self):
        """Delete this employee's record from the database."""
        sql = "DELETE FROM employees WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()



@classmethod
def instance _from_db(cls, row):
    [1, ]
