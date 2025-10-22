import csv
with open('python/hi.csv',newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ',quotechar='|')
    for row in spamreader:
        print(", ".join(row))
    