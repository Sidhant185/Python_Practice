# Q22: Find first non-repeating character in string
# Counts frequencies and returns first with count 1

# Input: Get text from user
text1 = input()

# Initialize frequency dictionary
freq = {}

# Count frequency of each character
for char in text1:
    freq[char] = freq.get(char, 0)+1

# Find first character with frequency 1
for char in text1:
    # Check if current character appears only once
    if freq[char] == 1:
        # Output: Print first non-repeating character
        print(char)
        break