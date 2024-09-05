s = input('cameCase: ')
words = []
last_index = 0;

for i in range(len(s)):
    if s[i].isupper():
        words.append(s[last_index:i].lower())
        last_index = i

    if i == len(s) - 1:
        words.append(s[last_index:].lower())


print("snake_case: ", end = "")

print(*words, sep='_')




