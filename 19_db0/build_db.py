#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

students = []

with open('students.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        students.append(((row['name'], row['age'], row['id'])))
        
        
        
DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

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
c.execute(command)    # run SQL statement

for student in students:
    name, age, id_num = student
    c.execute("INSERT INTO students (name, age, id) VALUES (?, ?, ?)", (name, age, id_num))

#==========================================================

db.commit() #save changes
db.close()  #close database
