string = input("Enter any string: ")
d = {}

for string in string:
    if string not in d:
        d[string] = 1
    else:
        d[string] += 1

print(d)
print(max(d, key=d.get))
