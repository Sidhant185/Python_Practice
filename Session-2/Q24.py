# Q24: Capitalize first letter of each word in sentence
# Converts word[0] to uppercase and keeps rest as is

# Input: Get sentence from user
sentence = input()

# Split sentence into individual words
words = sentence.split()

# Initialize result list
result = []

# Process each word
for word in words:
    # Capitalize first letter and concatenate with rest
    # word[0].upper() converts first letter to uppercase
    # word[1:] keeps remaining characters unchanged
    result.append(word[0].upper()+word[1:])

# Output: Print modified sentence with space between words
print(" ".join(result))