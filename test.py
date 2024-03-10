import csv

csv_file = open("cardsInfo.csv","r")

reader = csv.reader(csv_file)

for row in reader:
    print(row[4])

csv_file.close()