"""
CIS206 W01 4/01/2024
Alexander Martinez Leyva
Assignment 11
"""

import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

# Create a table with 5 columns including real numbers and text
cur.execute('''CREATE TABLE IF NOT EXISTS my_table (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                salary REAL,
                department TEXT,
                city TEXT
            )''')

# Insert 5 rows
data = [
    ('John', 30, 50000.0, 'HR', 'New York'),
    ('Alice', 25, 60000.0, 'IT', 'San Francisco'),
    ('Bob', 35, 70000.0, 'Finance', 'Chicago'),
    ('Emily', 28, 55000.0, 'Marketing', 'Los Angeles'),
    ('David', 32, 65000.0, 'Operations', 'Boston')
]

cur.executemany('INSERT INTO my_table VALUES (NULL,?,?,?,?,?)', data)

# List
print("All columns and rows:")
cur.execute('SELECT * FROM my_table')
print(cur.fetchall())

# List - but using the where clause
print("\nAll columns with where clause:")
cur.execute('SELECT * FROM my_table WHERE department = "IT"')
print(cur.fetchall())

# List only the text columns but all the rows
print("\nOnly text columns:")
cur.execute('SELECT name, department, city FROM my_table')
print(cur.fetchall())

# Sum one of the real number columns
cur.execute('SELECT SUM(salary) FROM my_table')
total_salary = cur.fetchone()[0]
print("\nTotal salary:", total_salary)

# Provide a count of the rows in the table
cur.execute('SELECT COUNT(*) FROM my_table')
row_count = cur.fetchone()[0]
print("Row count:", row_count)

# Create a cursor
print("\nCursor showing all rows and columns:")
cur.execute('SELECT * FROM my_table')
for row in cur.fetchall():
    print(row)

# Commit changes
conn.commit()
conn.close()
