# First script used.
# Creates a .db file from the .csv, so we can better manipulate the data.

import csv
import sqlite3

db_file = sqlite3.connect("CMS_Data.db")
cursor = db_file.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS cms_data(
                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  npi TEXT NOT NULL,
                  lastname TEXT,
                  firstname TEXT,
                  mi TEXT,
                  credentials TEXT,
                  gender TEXT,
                  entitytype TEXT,
                  address1 TEXT,
                  address2 TEXT,
                  city TEXT,
                  state TEXT,
                  statefips TEXT,
                  zip TEXT,
                  ruca REAL,
                  rucadesc TEXT,
                  countrycode TEXT,
                  providertype TEXT,
                  medicareindicator TEXT,
                  hcpcscode TEXT,
                  hcpcsdescription TEXT,
                  hcpcsdrugindicator TEXT,
                  placeofservice TEXT,
                  beneficiaries INTEGER,
                  services REAL,
                  distinctperday REAL,
                  averagesubmitted REAL,
                  averagemedicareallowed REAL,
                  averagemedicarepayment REAL,
                  averagestandardizedpayment REAL
                  );""")
csv_file = open("CMS_Data.csv", encoding='latin-1')
data = csv.reader(csv_file)
insert_records = "INSERT INTO cms_data (npi, lastname, firstname, mi, credentials, gender, entitytype, address1, address2, city, state, statefips, zip, ruca, rucadesc, countrycode, providertype, medicareindicator, hcpcscode, hcpcsdescription, hcpcsdrugindicator, placeofservice, beneficiaries, services, distinctperday, averagesubmitted, averagemedicareallowed, averagemedicarepayment, averagestandardizedpayment) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
cursor.executemany(insert_records, data)
select_all = "SELECT * FROM cms_data"
rows = cursor.execute(select_all).fetchall()
# For testing the record structure and confirming the process is done:
for r in range(50):
    print(rows[r])
db_file.commit()
db_file.close()
