import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        print("SQLite library version:", sqlite3.sqlite_version)  # Preferred approach
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

create_connection()


conn = sqlite3.connect('student.db')
cursor = conn.cursor() #

cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 age INTEGER NOT NULL,
                 grade INTEGER NOT NULL);''');

def add_student(name, age, grade):
    cursor.execute("INSERT INTO Students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    return cursor.lastrowid;

def get_students():
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return rows;

def update_student(id, name, age, grade):
    cursor.execute("UPDATE Students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, id))
    conn.commit()
    return cursor.rowcount;

def delete_student(id):
    cursor.execute("DELETE FROM Students WHERE id=?", (id,))
    conn.commit()
    return cursor.rowcount;


print(add_student('Alice', 25, 90))

students = get_students()
print("All student", students);

print(update_student(1, 'Alice', 26, 91))

students = get_students()

print("Updated student", students);

print(delete_student(1))

students = get_students()

print("After delete student", students);

conn.close()