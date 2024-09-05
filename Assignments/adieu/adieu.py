names = []

while True:
    print('Name: ', end = "")

    try:
        s = input()

    except EOFError:
        print()

        if len(names) == 1:
            print('Adieu, adieu, to', names[0])
            break

        if len(names) == 2:
            print(f'Adieu, adieu, to {names[0]} and {names[1]}')

        else:
            sliced_names = names[:len(names)-1]
            print('Adieu, adieu, to ', end = "")
            print(*sliced_names, sep = ', ', end = "")
            print(', ', end = "")
            print('and', names[-1])

        break

    else:
        names.append(s)
        continue



