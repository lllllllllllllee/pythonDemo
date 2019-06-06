#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE WHETHER
       (time          VARCHAR(50)    NOT NULL, 
       temp           VARCHAR(50)    NOT NULL,
       humidy         VARCHAR(50)     NOT NULL);''')
print("Table created successfully")
conn.commit()
conn.close()