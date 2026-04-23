# Q13: Largest Odd Number in String
# Remove leading even digits to get largest odd number

def largestOddNumber(num):
    """
    Find largest odd number by removing trailing even digits
    Start from end and find last odd digit
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Iterate from end to start
    for i in range(len(num) - 1, -1, -1):
        # Check if digit is odd
        if int(num[i]) % 2 != 0:
            # Return substring up to this odd digit (inclusive)
            return num[:i+1]
    
    # No odd digit found
    return ""
