import string

# text = "My name is Bonisam and I love Chelsea fc"
text = input("Enter a text or sentence: ")

def word_counter(text):
    
    text = text.lower()

    
    for char in string.punctuation:
        text = text.replace(char, "")


    words = text.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


print(word_counter(text))