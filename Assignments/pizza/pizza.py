from tabulate import tabulate
import sys
import csv

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments ')

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments ')

path = sys.argv[1]

if path[len(path)-4:] != '.csv':
    sys.exit('Not a CSV file')

try:
    file = open(path)

except:
    sys.exit('File does not exist')

all = []

for line in file:
    line = line.rstrip()
    all.append(line.split(','))

file.close()
print(tabulate(all, tablefmt = 'grid', headers = 'firstrow'))

