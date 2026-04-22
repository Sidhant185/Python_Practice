def isPalindrome(s):
    filtered = "".join(c.upper() for c in s if c.isalnum())
    return filtered == filtered[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
