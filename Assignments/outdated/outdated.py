months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    print('Date: ', end = "")
    s = input()

    if len(s) <= 10:
        m, d, y = s.split('/')

    else:
        try:
            a, y = s.split(',')
            m, d = a.split(' ')

        except:
            continue

        if m not in months:
            continue
    try:
        if len(s) <= 10:
            m = int(m)

        d = int(d)
        y = int(y)

    except ValueError:
        continue

    else:
        if len(s) <= 10 and (m < 1 or m > 12):
            continue

        if d < 1 or d > 31:
            continue

        if len(s) <= 10 and m < 10:
            m = '0' + str(m)

        if d < 10:
            d = '0' + str(d)

        if len(s) <= 10:
            print(f'{y}-{m}-{d}')

        else:
            m = months.index(m) + 1
            if m < 10:
                m = '0' + str(m)

            print(f'{y}-{m}-{d}')

        break
