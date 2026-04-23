"""
Q22: Squares of a Sorted Array

Problem: Return an array of squares of elements from a sorted array, also sorted.
"""


def sortedSquares(nums):
    """
    Return sorted squares of a sorted array.
    
    Key insight: Largest squares are at both ends (negative numbers and large positive numbers).
    Use two pointers approach from ends and fill result array from the end.
    
    Args:
        nums: Sorted array (may contain negative numbers)
    
    Returns:
        Sorted array of squares
    
    Time Complexity: O(n)
    Space Complexity: O(n) for result array
    """
    n = len(nums)
    result = [0] * n
    
    left = 0
    right = n - 1
    
    # Fill result array from right to left (largest to smallest)
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    
    return result


# Main execution
if __name__ == "__main__":
    # Test case
    n = int(input("Enter number of elements: "))
    nums = list(map(int, input("Enter sorted array: ").split()))
    
    result = sortedSquares(nums)
    print(" ".join(map(str, result)))
    
    # Additional test cases
    print("\n--- Additional Test Cases ---")
    test_cases = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [0],
        [-1],
        [1, 2, 3]
    ]
    
    for nums in test_cases:
        print(f"{nums} -> {sortedSquares(nums)}")
