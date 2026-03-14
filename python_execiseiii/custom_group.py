def group_by(words, func):
    result = {}

    for word in words:
        key = func(word)

        if key not in result:
            result[key] = []

        result[key].append(word)

    return result


words = ["one", "two", "three", "four", "five", "six"]

print(group_by(words, len))