vowels = "aeiou"
char = input("Enter a character: ")[0]
char = char.lower()

if char in vowels:
    print("Vowel")
else: 
    print("Consonent")