import matplotlib.pyplot as plt
import numpy as np
import csv

labels = []
counts = []

#with open("count specialties.csv") as csv_file:
#with open("gender_m.csv") as csv_file:
with open("gender_f.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        labels.append(row["providertype"])
        counts.append(int(row["COUNT(DISTINCT npi)"]))

y = np.array(counts)

def make_autopct(counts):
    def my_autopct(pct):
        total = sum(counts)
        val = int(round(pct*total/100.0)) # Take the percentage share of each slice, multiply it by the total of all counts. This returns the original count.
        return '{v:d}'.format(p=pct,v=val)
    return my_autopct

plt.pie(y, labels = labels, rotatelabels = True, radius = 25, autopct=make_autopct(counts))
plt.show()
