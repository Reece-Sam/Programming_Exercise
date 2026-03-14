data = {
    "a": 1,
    "b": 2,
    "c": 1
}

inversion = {}

for key, value in data.items():

    if value not in inversion:
        dict[value] = []

    inversion[value].append(key)

print(inversion)