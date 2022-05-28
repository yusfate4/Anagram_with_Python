# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    word = sorted(word)
    anagram = sorted(anagram)

    return word == anagram


print(find_anagram ("hello", "check"))
print(find_anagram ("below", "elbow"))
