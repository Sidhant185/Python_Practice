# Q14: Reverse Prefix
# Reverse string up to first occurrence of character

def reversePrefix(word, ch):
    """
    Reverse string from start up to character ch
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Find first occurrence of character
    idx = word.find(ch)
    
    # If character not found, return original string
    if idx == -1: 
        return word
    
    # Reverse up to character and concatenate rest
    # word[:idx+1] is the part to reverse
    # word[idx+1:] remains as is
    return word[:idx+1][::-1] + word[idx+1:]
