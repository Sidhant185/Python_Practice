"""
Q25: Two Numbers Unlock the Target

Problem: Find two numbers in a sorted array that sum to target (1-indexed).
"""


def twoSum(numbers, target):
    """
    Find two numbers in sorted array that sum to target.
    
    Using two-pointer approach for O(n) time and O(1) space.
    
    Args:
        numbers: Sorted array of integers
        target: Target sum
    
    Returns:
        List [index1, index2] (1-indexed) where numbers[i] + numbers[j] = target
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # Convert to 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]  # Should not reach here as solution is guaranteed


# Main execution
if __name__ == "__main__":
    # Test case
    numbers = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target sum: "))
    
    result = twoSum(numbers, target)
    print(f"[{result[0]}, {result[1]}]")
    
    # Additional test cases
    print("\n--- Additional Test Cases ---")
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1),
        ([1, 2, 3, 4, 5, 6, 7], 13),
    ]
    
    for numbers, target in test_cases:
        result = twoSum(numbers, target)
        print(f"numbers={numbers}, target={target} -> {result}")
