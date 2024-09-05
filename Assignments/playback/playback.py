s = input()

output = "";

list = s.split(" ")

for i in range(len(list)):
    if i == len(list) - 1:
        output = output + list[i] 
    else:
        output = output + list[i] + "..."

print(output)
