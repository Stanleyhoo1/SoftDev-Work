# Stanley Hoo, Alex Luo, Tahmim Hassan
# UWSD
# SoftDev
# K19 -- All Your Database Are Belong To Us
# 2024-10-18
# Time spent: 1h

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

students = []

with open('students.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        students.append(((row['name'], row['age'], row['id'])))
        
courses = []

with open('courses.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        courses.append(((row['code'], row['mark'], row['id'])))
        
        
        
DB_FILE="discobandit.db"

conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


command = '''
    CREATE TABLE IF NOT EXISTS students (
        name TEXT NOT NULL UNIQUE,
        age INT,
        id INT NOT NULL UNIQUE
    );
'''

# test SQL stmt in sqlite3 shell, save as string
cur.execute(command)    # run SQL statement

for student in students:
    name, age, id_num = student
    cur.execute("INSERT INTO students (name, age, id) VALUES (?, ?, ?)", (name, age, id_num))

# Create the users table if it doesn't already exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        code TEXT NOT NULL,
        mark INT,
        id INT NOT NULL
    );
''')

for course in courses:
    code, mark, id_num = course
    cur.execute("INSERT INTO courses (code, mark, id) VALUES (?, ?, ?)", (code, mark, id_num))
    
#==========================================================

conn.commit() #save changes
conn.close()  #close database
