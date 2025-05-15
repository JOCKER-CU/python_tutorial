# SQLite database
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('employees.db')
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            department TEXT NOT NULL
        )
        '''
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("Table created successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

create_connection()
def insert_connection( record):
    conn = None
    try:
        conn = sqlite3.connect('employees.db')
        insert_query = '''
        INSERT INTO Employees (name, age, department)
        VALUES (?, ?, ?)
        ''';
        cursor = conn.cursor()
        cursor.executemany(insert_query, record );
        conn.commit()
        print("Record inserted successfully");
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close();



data = [
    ('John Doe', 22, 'IT'),
    ('Dame Doe', 23, 'Sale'),
    ('Will Doe', 24, 'HR'),
    ('James Doe', 25, 'ERP')
]

insert_connection(data)
def select_connection():
    conn = None
    try:
        conn = sqlite3.connect('employees.db')
        select_query = '''
        SELECT * FROM Employees
        '''
        cursor = conn.cursor()
        cursor.execute(select_query);
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

select_connection();

def update_connection():
    conn = None
    try:
        conn = sqlite3.connect('employees.db')
        update_query = '''
        UPDATE Employees
        SET age = 30, name = 'Mella James'
        WHERE id = 1
        ''';
        cursor = conn.cursor()
        cursor.execute(update_query);
        conn.commit()
        print("Record updated successfully");
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

update_connection()

def delete_connection():
    conn = None
    try:
        conn = sqlite3.connect('employees.db')
        delete_query = '''
        DELETE FROM Employees
        WHERE id = 4
        ''';
        cursor = conn.cursor()
        cursor.execute(delete_query);
        conn.commit()
        print("Record deleted successfully");
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

delete_connection();

select_connection();
