# Q4: Minimize Height Difference I
# Minimize max-min by adding/subtracting k from elements

def getmin(arr, k):
    """
    Minimize height difference by modifying elements
    Can add or subtract k from each element
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    # Sort array for easier processing
    arr.sort()
    n = len(arr)
    
    # Initialize answer with original difference
    ans = arr[-1] - arr[0]
    
    # Try all partition points
    for i in range(1, n-1):
        # For elements 0..i: add k to maximize
        # For elements i+1..n-1: subtract k to minimize
        # Find min of max and max of min
        mini = min(arr[0]+k, arr[i+1]-k)
        maxi = max(arr[-1]-k, arr[i]+k)
        
        # Update answer if this partition is better
        ans = min(ans, maxi - mini)
    
    return ans

# Input and output
nums = list(map(int, input().split()))
target = int(input())
print(getmin(nums, target))