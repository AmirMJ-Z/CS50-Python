l = {}

while True:
    try:
        s = input()
        s = s.upper()

        if l.get(s):
            l[s] = l[s] + 1

        else:
            l[s] = 1


    except EOFError:
        break

keys = list(l.keys())
keys.sort()

for i in keys:
    print(f'{l[i]} {i}')
