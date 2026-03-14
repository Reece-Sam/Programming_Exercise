def flatten_list(data):
    result = []

    for item in data:
        #This checks whether the item is another list.
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result

numbers = [1, [2, 3], [4, [5, 6]], [7, [8, 9]], 10]

print(flatten_list(numbers))