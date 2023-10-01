# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:27:18 2023

@author: lr
"""

import sqlite3

conn = sqlite3.connect('BBQ.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS meat(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER
    )''')

cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('chicken', 30, 5)")
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('beaf', 55, 10)")
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('pork', 40, 15)")

conn.commit()

cursor.execute("SELECT * FROM meat")
meats = cursor.fetchall()

print("肉類列表:")
for item in meats:
    print(item)

cursor.execute("UPDATE meat SET price = 35 WHERE name = 'pork'")
cursor.execute("UPDATE meat SET quantity = 30 WHERE name = 'chicken'")
conn.commit()

cursor.execute("SELECT * FROM meat")
meats = cursor.fetchall()

print("\n更新後的肉類列表:")
for item in meats:
    print(item)

cursor.execute("DELETE FROM meat WHERE price = 40")
conn.commit()

cursor.execute("SELECT * FROM meat")
meats = cursor.fetchall()

print("\n删除後的肉類列表:")
for item in meats:
    print(item)

cursor.close()
conn.close()
