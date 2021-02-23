'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import sqlite3
connection = sqlite3.connect("college.db")
cursor = connection.cursor()

sql_command="""
CREATE TABLE attedance(
roll_no INTEGER,
fname VARCHAR(20),
lname VARCHAR(30),
day DATE,
status CHAR(1))"""

cursor.execute(sql_command)
