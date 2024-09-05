def shorten(s):
    all_alphas = ""

    for i in s:
        if i.lower() == 'i' or i.lower() == 'a' or i.lower() == 'o' or i.lower() == 'u' or i.lower() == 'e':
            continue

        else:
            all_alphas += i

    return all_alphas

def main():
    s = input('Input: ')
    print('Output:', shorten(s))


if __name__ == '__main__':
    main()



