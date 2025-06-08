import sqlite3

def create_connection():
    conn = sqlite3.connect('employees.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT,
            department TEXT,
            salary REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_employee(name, position, department, salary):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (name, position, department, salary)
        VALUES (?, ?, ?, ?)
    ''', (name, position, department, salary))
    conn.commit()
    conn.close()

def get_all_employees():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_employee(emp_id, name, position, department, salary):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE employees
        SET name = ?, position = ?, department = ? salary = ?
        WHERE id = ?
    ''', (name, position, department, salary, emp_id))
    conn.commit()
    conn.close()

def delete_employee(emp_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    conn.close()

def search_employee(emp_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
    row = cursor.fetchone()
    conn.close()
    return row