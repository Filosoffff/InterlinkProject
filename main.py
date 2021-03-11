import csv

with open('acme_worksheet.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        if line[1] == line[1]:
            print(line)