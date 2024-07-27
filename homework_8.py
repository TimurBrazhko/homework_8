import sqlite3 as sql

with sql.connect('person.db') as conn:
    cursor = conn.cursor()
    # cursor.execute('''DROP TABLE IF EXISTS Employees''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    DepartmentID INTEGER NOT NULL
    )''')

    # cursor.execute('''DROP TABLE IF EXISTS Departments''')


    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
    DepartmentName TEXT,
    DepartmentID INTEGER NOT NULL,
    FOREIGN KEY(DepartmentID) REFERENCES Employees(DepartmentID)
    )''')

    cursor.execute('''INSERT INTO Departments (DepartmentName, DepartmentID) 
    VALUES
    ('HR', 101),
    ('IT', 102),
    ('Sales', 103)
    ''')

    cursor.execute('''INSERT INTO Employees (FirstName, LastName, DepartmentID) 
    VALUES
    ('timur', 'chikeev', 102),
    ('aidar', 'isamatov', 103),
    ('bayastan', 'akmataliev', 103),
    ('adilet', 'nogoibaev', 101),
    ('aldiar', 'ahumbaev', 102),
    ('sultan', 'asheraliev', 101)
    ''')

    cursor.execute('''DELETE FROM Employees WHERE EmployeeID > 6''')

    cursor.execute('''SELECT Employees.FirstName, Employees.LastName,
    Departments.DepartmentID, Departments.DepartmentName
    FROM Employees
    LEFT JOIN Departments ON Departments.DepartmentID = Employees.DepartmentID
    ''')

    for row in cursor.fetchall():
        print(row)

    print('------------')


    cursor.execute('''SELECT Employees.FirstName, Employees.LastName,
    Departments.DepartmentID, Departments.DepartmentName
    FROM Employees
    LEFT JOIN Departments ON Departments.DepartmentID = Employees.DepartmentID
    WHERE Departments.DepartmentName LIKE 'IT'
    ''')

    for row in cursor.fetchall():
        print(row)
