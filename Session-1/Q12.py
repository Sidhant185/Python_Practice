# Q12: Check if character is vowel or consonant
# Compares input character against vowel list

# Define string containing all vowels
vowels = "aeiou"

# Input: Get character from user (take first character only)
char = input("Enter a character: ")[0]

# Convert to lowercase for case-insensitive comparison
char = char.lower()

# Check if character is in vowels list
if char in vowels:
    print("Vowel")
else:
    # Character is a consonant
    print("Consonent")