# Q14: Maximum subarray sum (Kadane's Algorithm)
# Finds contiguous subarray with largest sum

def maxSum(arr):
    """
    Find maximum sum of any contiguous subarray
    Uses Kadane's Algorithm - O(n) time, O(1) space
    """
    # Initialize with first element
    max_Sum = current_Sum = arr[0]
    
    # Iterate through rest of array
    for i in range(1, len(arr)):
        # Either extend current subarray or start new one
        current_Sum = max(arr[i], current_Sum+arr[i])
        
        # Update max if current is larger
        max_Sum = max(current_Sum, max_Sum)
    
    return max_Sum

# Input: Get array from space-separated input
num1 = list(map(int, input().split()))

# Call function and print result
print(maxSum(num1))