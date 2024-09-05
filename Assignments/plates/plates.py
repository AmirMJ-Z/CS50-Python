def is_valid(s):
    digit_found = False

    if len(s) > 6 or len(s) < 2:
        return False

    if (not s[0].isalpha()) or (not s[1].isalpha()):
        return False

    for i in range(len(s)):
        if s[i].isdigit() and s[i] == '0' and (not digit_found):
            return False

        if s[i].isdigit():
            digit_found = True

        if s[i].isdigit() and i+1 < len(s) and s[i+1].isalpha():
            return False

        if s[i] == ' ' or s[i] == '.' or s[i] == ':':
            return False

    return True

def main():
    s = input('Plate: ')

    if isvalid(s):
        print('Valid')

    else:
        print('Invalid')

if __name__ == '__main__':
    main()







