import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r'^(\d{1,2}):?(\d{0,2}) (AM|PM) to (\d{1,2}):?(\d{0,2}) (AM|PM)$', s)

    if not match:
        raise ValueError

    sd1, sd2, s, ed1, ed2, e = match.groups()

    if sd2 == "":
        sd2 = 0

    if ed2 == "":
        ed2 = 0

    sd1 = int(sd1)
    sd2 = int(sd2)
    ed1 = int(ed1)
    ed2 = int(ed2)

    if sd1 == 12:
        sd1 = 0

    if ed1 == 12:
        ed1 = 12

    if ed1 > 12 or sd1 > 12 or sd2 > 59 or ed2 > 59:
        raise ValueError

    if s == 'PM' and sd1 != 12:
        sd1 = sd1 + 12

    if e == 'PM' and ed1 != 12:
        ed1 = ed1 + 12

    if sd1 < 10:
        sd1 = f'0{sd1}'

    if sd2 < 10:
        sd2 = f'0{sd2}'

    if ed1 < 10:
        ed1 = f'0{ed1}'

    if ed2 < 10:
        ed2 = f'0{ed2}'

    return f'{sd1}:{sd2} to {ed1}:{ed2}'


if __name__ == "__main__":
    main()
