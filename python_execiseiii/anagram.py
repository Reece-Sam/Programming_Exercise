def are_anagrams(word1, word2):
    
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    
    if sorted_word1 == sorted_word2:
        return True
    else:
        return False
    
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if are_anagrams(word1, word2):
    print("The words are anagrams")
else:
    print("The words are not anagrams, Try again")