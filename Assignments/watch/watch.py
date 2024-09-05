import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'.*<iframe.*https?://(www\.)?youtube\.com/embed/(\w+).*>.*</iframe>.*', s)

    if not match:
        return None

    return f'https://youtu.be/{match.groups()[1]}'


if __name__ == "__main__":
    main()
