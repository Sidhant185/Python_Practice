# Q16: Maximum Conveyor Shifts
# Count total shifts for all zeros between ones

def maxConveyorShifts(s):
    """
    Count movement of zeros when between ones
    For each 0 between 1s, count how many 1s are to its left
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    res = 0
    ones = 0  # Count of 1s seen so far
    
    # Iterate through string
    for i in range(len(s)):
        if s[i] == '1':
            # Increment count of ones
            ones += 1
        # If current is 0 and there's a 1 before it
        elif i > 0 and s[i-1] == '1':
            # Add count of ones to result
            res += ones
    
    return res