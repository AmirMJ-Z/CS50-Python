value = 50

while True:
    print(f'Amount Due: {value}')
    coin = int(input('Insert Coin: '))
    if coin != 5 and coin != 10 and coin != 25:
        continue
    
    if coin >= value:
        print(f'Change Owed: {coin - value}')
        break

    if coin < value:
        value -= coin

