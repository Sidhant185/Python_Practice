# Q25: Remove duplicate characters from string
# Maintains order while removing first occurrence duplicates

# Input: Get word from user
word = input()

# Initialize set to track seen characters
seen = set()

# Initialize result string
result = ""

# Iterate through each character
for char in word:
    # Check if character not seen before
    if char not in seen:
        # Add to result
        result += char
        # Add to seen set
        seen.add(char)

# Output: Print string without duplicates
print(result)
