import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        tries = 0
        num1, num2 = generate_integer(level)

        while tries < 3:
            try:
                ans = int(input(f'{num1} + {num2} = '))

            except:
                tries += 1
                print('EEE')
                continue

            else:
                if ans != num1 + num2:
                    tries += 1
                    print('EEE')
                    continue

                else:
                    score = score + 1
                    break

        if tries >= 3:
            print(f'{num1} + {num2} = {num1 + num2}')
            continue

        else:
            continue

    print(f'Score: {score}')


def get_level():
    while True:
        try:
            level = int(input('Level: '))

        except:
            continue

        else:
            if level != 1 and level != 2 and level != 3:
                continue

            return level



def generate_integer(level):
    if level != 1 and level != 2 and level != 3:
        raise ValueError

    if level == 1:
        num1 = random.randint(0, 10 ** level - 1)
        num2 = random.randint(0, 10 ** level - 1)

    else:
        num1 = random.randint(10 ** (level-1), 10 ** level - 1)
        num2 = random.randint(10 ** (level-1), 10 ** level - 1)

    return [num1, num2]



if __name__ == "__main__":
    main()




