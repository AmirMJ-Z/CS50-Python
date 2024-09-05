def main():
    s = input('What time is it? ')
    s = s.strip()
    time = convert(s)

    if time >= 18 and time <= 19:
        print('dinner time')

    elif time >= 12 and time <= 13:
        print('lunch time')

    elif time >= 7 and time <= 8:
        print('breakfast time')


def convert(time):
    hour, minute = time.split(':')
    hour = int(hour)
    minute = int(minute)
    minute = minute / 60

    return hour + minute


if __name__ == "__main__":
    main()
