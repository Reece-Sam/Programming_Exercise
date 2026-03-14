numbers = [1, 3, 3, 3, 2, 2, 4, 3]

def frequent(numbers):
    count = {}

#Counts how many times each number appears
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

#find the number with the frequency 
    most_common = max(count, key=count.get)
    return most_common

print(frequent(numbers))