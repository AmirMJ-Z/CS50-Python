def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    out = d.replace("$", "")
    out = float(out)

    return out


def percent_to_float(p):
    out = p.replace("%", "")
    out = float(out) * 0.01

    return out


main()
