import csv

with open('table_in.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('newcsv.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            mydict = {row[0]: row[1], row[1]: row[2]}
            writer.writerow(mydict)