s = input('Expression: ')
s = s.strip()
x, op, y = s.split(" ")
x = float(x)
y = float(y)

if op == '+':
    result = x + y
elif op == '-':
    result = x - y
elif op == '/':
    result = x / y
elif op == '*':
    result = x * y

print(f'{result:.1f}')
