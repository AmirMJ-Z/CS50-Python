def convert(s):
    out = s.replace(":(", "🙁")
    out = out.replace(":)", "🙂")

    return out

def main():
    s = input()
    print(convert(s))

main()
