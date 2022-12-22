# In case I need to run queries on the data; converted to db using '1_Convert to db.py' for convenience

import sqlite3
import csv # for output

output = 1

db_file = sqlite3.connect("CMS_Data.db")
cursor = db_file.cursor()

# For testing: Gets a list of tables
# tables = [a for a in cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# print(tables)

query = "SELECT fips, SUM(beneficiaries) FROM fips GROUP BY fips"
data = cursor.execute(query).fetchall()

# Output query results to a csv:
if output == 1:
    with open('results.csv','w') as out_csv_file:
        csv_out = csv.writer(out_csv_file)
        # Header row:                    
        csv_out.writerow([d[0] for d in cursor.description])
        # Rest of the data:
        for i in range(len(data)):
          csv_out.writerow(data[i])
else:
    print("No output")

db_file.close()
