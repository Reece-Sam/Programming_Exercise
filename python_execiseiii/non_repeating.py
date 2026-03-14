def first_non_repeating(text):
    count = {}

    # count each character
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # find the first non repeating character
    for char in text:
        if count[char] == 1:
            return char

    return None

word = "Ekitike"

print(first_non_repeating(word))

# word = input("Enter a word: ")

# result = first_non_repeating(word)

# if word:
#     print("First non-repeating character")
# else:
#     print("No non-repeating character found")

# print(word)