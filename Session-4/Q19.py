# Q19: Valid Palindrome
# Check if string is palindrome (alphanumeric only, case-insensitive)

def isPalindrome(s):
    """
    Check if string is valid palindrome
    Only consider alphanumeric characters, ignore case
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Filter to keep only alphanumeric characters, convert to uppercase
    filtered = "".join(c.upper() for c in s if c.isalnum())
    
    # Check if filtered string equals its reverse
    return filtered == filtered[::-1]

# Test
print(isPalindrome("A man, a plan, a canal: Panama"))
