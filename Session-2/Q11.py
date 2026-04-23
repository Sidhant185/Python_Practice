# Q11: Find missing number in array of 1 to n+1
# Uses sum formula: n(n+1)/2 and calculates difference

def missing(Arr):
    """
    Find missing number using mathematical formula
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Calculate expected array size (n+1)
    n = len(Arr)+1
    
    # Calculate expected sum: sum of 1 to (n+1)
    ExSum = ((n+1)*n)//2
    
    # Calculate actual sum of array
    actualSum = sum(Arr)
    
    # Missing number is difference
    ans = ExSum-actualSum
    return ans

# Input: Get array from space-separated input
nums = list(map(int, input().split()))

# Call function and print result
print(missing(nums))
