menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    print('Item: ', end = "")

    try:
        s = input()
        s = s.lower()
        s = s.title()

    except EOFError:
        print()
        print(f'Total: ${total:.2f}')
        break

    else:
        if menu.get(s):
            total = total + menu.get(s)
            print(f'Total: ${total:.2f}')







