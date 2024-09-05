from datetime import date
import re
import sys
import inflect

inflector = inflect.engine()

def main():
    print(num_to_words(date_to_minutes(*get_date())))

def get_date():
    s = input('Date of Birth: ')
    match = re.search(r'\s*(\d{4})-(\d{2})-(\d{2})\s*', s)

    if not match:
        sys.exit('Invalid date')

    else:
        return (int(match.groups()[0]), int(match.groups()[1]), int(match.groups()[2]))

def date_to_minutes(year, month, day):
    input_date = date(year, month, day)

    if input_date > date.today():
        sys.exit('Invalid date')

    return round((date.today() - input_date).days * 24 * 60)

def num_to_words(num):
    output = inflector.number_to_words(num) + " minutes"
    output = output.replace(' and', '')
    output = output[0].upper() + output[1:]
    return output

if __name__ == "__main__":
    main()
