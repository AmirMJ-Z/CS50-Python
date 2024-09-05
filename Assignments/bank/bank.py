def main():
    s = input('Greeting: ')
    s = s.strip()
    s = s.lower()

    print('$' + value(s))


def value(s):
    first_word = s.split(" ")[0]
    first_word = s.split(",")[0]

    if first_word == 'hello':
        return 0

    elif first_word[0] == 'h':
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
