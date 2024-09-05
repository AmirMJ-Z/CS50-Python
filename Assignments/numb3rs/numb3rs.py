import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r'^\s*([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\s*$', ip)

    if not match:
        return False

    for seg in match.groups():
        if int(seg) > 255:
            return False

    return True


if __name__ == "__main__":
    main()
