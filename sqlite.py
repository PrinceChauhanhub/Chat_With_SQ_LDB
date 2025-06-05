import sqlite3

## Connect to sqllite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table

cursor = connection.cursor()

## create the table
table_info = """
CREATE TABLE student(Name VARCHAR(50), class VARCHAR(25), section VARCHAR(25), marks INT)
"""

cursor.execute(table_info)

## Insert some records

cursor.execute('''INSERT INTO student values('Krish','Data Science','A',90)''')
cursor.execute('''INSERT INTO student values('Prince','Data Science','A',99)''')
cursor.execute('''INSERT INTO student values('Disha','Data engineer','B',90)''')
cursor.execute('''INSERT INTO student values('Pragati','doctor','B',95)''')
cursor.execute('''INSERT INTO student values('Vishal','visualizer','C',75)''')


## Display all the record 
print("the inserted records are")
data = cursor.execute('''SELECT * FROM student''')

for row in data:
    print(row)
    
    
## Commit changes in the databases
connection.commit()
connection.close()