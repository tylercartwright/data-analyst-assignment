# First script used.
# Creates a .db file from the .csv, so we can better manipulate the data.

import csv
import sqlite3

db_file = sqlite3.connect("CMS_Data.db")
cursor = db_file.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS population(
                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  city TEXT NOT NULL,
                  state TEXT NOT NULL,
                  population INTEGER NOT NULL
                  );""")
csv_file = open("population.csv", encoding='latin-1')
data = csv.reader(csv_file)
insert_records = "INSERT INTO population (city, state, population) VALUES(?, ?, ?)"
cursor.executemany(insert_records, data)
select_all = "SELECT * FROM population"
rows = cursor.execute(select_all).fetchall()
# For testing the record structure and confirming the process is done:
for r in range(50):
    print(rows[r])
db_file.commit()
db_file.close()
