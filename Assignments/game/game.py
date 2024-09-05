import random

while True:
    try:
        global level
        level = int(input('Level: '))

    except:
        continue

    else:
        if level <= 0:
            continue

        break

random_number = random.randint(1, level)

while True:
    try:
        guess = int(input('Guess: '))

    except:
        continue

    else:
        if guess < 0:
            continue

        if guess < random_number:
            print('Too small!')
            continue

        if guess > random_number:
            print('Too large!')

        else:
            print('Just right!')
            break





