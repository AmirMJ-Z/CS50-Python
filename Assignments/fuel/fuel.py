def main():
    s = input('Fraction: ')
    print(gauge(convert(s)))


def convert(s):
     try:
        nom, denom = s.split('/')
        nom = int(nom)
        denom = int(denom)

     except ValueError:
         raise ValueError

     else:
         if nom > denom:
             raise ValueError

         try:
            percent = round(nom/denom * 100)

         except ZeroDivisionError:
             raise ZeroDivisionError

         else:
             return percent



def gauge(percent):
    if percent >= 90:
        return 'F'

    elif percent <= 1:
        return 'E'

    else:
        return f'{percent}%'


if __name__ == "__main__":
    main()





