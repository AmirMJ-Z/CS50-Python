import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments ')

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments ')

path = sys.argv[1]

if path[len(path)-3:] != '.py':
    sys.exit('Not a python file')

try:
    file = open(path)

except:
    sys.exit('File does not exist')

count = 0

for line in file:
    line = line.strip()

    if line == '':
        continue

    if line[0] == '#':
        continue

    count += 1

file.close()
print(count)

