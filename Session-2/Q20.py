# Q20: Count frequency of each character in string
# Uses dictionary to track character occurrences

# Input: Get text from user
text = input()

# Initialize frequency dictionary
freq = {}

# Count frequency of each alphabetic character
for char in text:
    # Only process alphabetic characters
    if char.isalpha():
        # Get current count or 0 if not present
        freq[char] = freq.get(char, 0) + 1

# Output: Print character frequencies
for ch,num in freq.items():
    print(ch,num)