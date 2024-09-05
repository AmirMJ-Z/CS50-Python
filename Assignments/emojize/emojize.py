import emoji

emojies = {
    ':earth_asia:' : '🌏',
    ':thumbsup:' : '👍',
}

s = input('Input: ')

for key in emojies.keys():
    s = s.replace(key, emojies[key])

print("Output:", emoji.emojize(s))
