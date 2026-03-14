
def word_length_mapping(words):
    result = {}

    for word in words:
        result[word] = len(word)

    return result

words = ["apple", "tiger", "cat", "dog", "lion"]

# words = input("Enter words: ")

print(word_length_mapping(words))
