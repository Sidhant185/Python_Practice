# Q21: Check if two strings are anagrams
# Compares strings (note: current implementation has bug, should sort)

# Input: Get first string
text1 = input()

# Input: Get second string
text2 = input()

# Sort both strings to check if they contain same characters
# (Note: the original code doesn't save the sorted results)
sorted(text1)
sorted(text2)

# Compare if strings are equal
# (This will always be False if strings are different due to unsaved sort)
if(text1==text2):
    print("True")
else:
    print("False")