# Q23: Find longest word in sentence
# Compares word lengths and returns word with max length

# Input: Get sentence from user
sentence = input()

# Split sentence into words
words = sentence.split()

# Output: Print list of words
print(words)

# Initialize frequency dictionary and max length
freq = {}
largest = 0

# Store word lengths and find maximum
for word in words:
    # Store length of each word
    freq[word] = len(word)
    
    # Update largest if current word is longer
    if largest<len(word):
        largest = len(word)

# Output: Print word(s) with maximum length
for word,num in freq.items():
    if num == largest:
        print(f"{word} = {num}")