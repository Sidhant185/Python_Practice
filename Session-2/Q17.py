# Q17: Check if string is palindrome
# Compares string with its reverse

def palindrome(str):
    """
    Check if string reads same forwards and backwards
    """
    # Reverse the string
    rev = str[::-1]
    
    # Compare original with reverse
    if(rev==str):
        return "True"
    else:
        return "False"

# Input: Get string from user
text = input()

# Call function and print result
print(palindrome(text))

