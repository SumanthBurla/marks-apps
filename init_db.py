import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO halfyearly_exam_marks (std_id, std_name, maths, physics, coding, grade) VALUES (?, ?, ?, ?, ?, ?)",
            (1, 'std1', 90, 90, 90, 90)
            )
cur.execute("INSERT INTO halfyearly_exam_marks (std_name, maths, physics, coding, grade) VALUES (?, ?, ?, ?, ?)",
            ('std2', 80, 70, 90, 80)
            )

connection.commit()
connection.close()