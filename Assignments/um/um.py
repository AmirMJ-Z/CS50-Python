import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match1 = re.findall(r'[^\w]+um[^\w]+', s, re.IGNORECASE)
    match2 = re.findall(r'^um[^\w]+', s, re.IGNORECASE)
    match3 = re.findall(r'[^\w]um$', s, re.IGNORECASE)
    match4 = re.findall(r'^um$', s, re.IGNORECASE)
    return len(match1) + len(match2) + len(match3) + len(match4)


if __name__ == "__main__":
    main()
