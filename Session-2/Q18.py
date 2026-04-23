# Q18: Count vowels and consonants in string
# Checks each character against vowel list

# Input: Get text from user
text = input()

# Define all vowels (lowercase and uppercase)
vowels = "aeiouAEIOU"

# Initialize counters
v = 0
c = 0

# Iterate through each character
for char in text:
    # Check if character is alphabetic
    if char.isalpha():
        # Check if character is vowel
        if char in vowels:
            # Increment vowel counter
            v = v+1
        else:
            # Increment consonant counter
            c = c+1

# Output: Print vowel count
print(v)

# Output: Print consonant count
print(c)