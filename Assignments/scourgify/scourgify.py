import sys
import csv

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments ')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments ')

path = sys.argv[1]

if path[len(path)-4:] != '.csv':
    sys.exit('Not a CSV file')

try:
    file = open(path)
    file_read = csv.DictReader(file)

except:
    sys.exit('Could not read', path)

all = []

for row in file_read:
    last, first = row['name'].rstrip().split(',')
    first = first.strip()
    last = last.strip()
    house = row['house'].rstrip()
    all.append({'first' : first, 'last' : last, 'house' : house,})

file = open(sys.argv[2], 'w')

file_write = csv.DictWriter(file, fieldnames = ['first', 'last', 'house'])
file_write.writeheader()

for row in all:
    file_write.writerow(row)

file.close()

