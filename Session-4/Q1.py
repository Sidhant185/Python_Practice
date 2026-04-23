# Q1: Pair Sum Checker
# Check if any two numbers in array sum to target value

def pairSumChecker(arr, x):
    """
    Find if any two numbers in array sum to x
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Set to track numbers we've seen
    seen = set()
    
    # Check each number in array
    for num in arr:
        # Calculate what complement we need
        complement = x - num
        
        # If complement was seen, we found a pair
        if complement in seen:
            return "Yes"
        
        # Add current number to seen set
        seen.add(num)
    
    return "No"