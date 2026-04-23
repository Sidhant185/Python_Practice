"""
Q26: Largest Number

Problem: Arrange numbers to form the largest possible number.
"""


def largestNumber(nums):
    """
    Arrange numbers to form the largest possible number.
    
    Use custom comparator: compare concatenations (a+b vs b+a).
    
    Args:
        nums: List of non-negative integers
    
    Returns:
        Largest number as string
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    from functools import cmp_to_key
    
    # Convert to strings
    str_nums = [str(num) for num in nums]
    
    # Custom comparator
    def compare(x, y):
        # If x+y > y+x, then x should come first
        if x + y > y + x:
            return -1  # x should come before y
        elif x + y < y + x:
            return 1   # y should come before x
        else:
            return 0   # Equal
    
    # Sort using custom comparator
    str_nums.sort(key=cmp_to_key(compare))
    
    # Join and handle leading zeros
    result = "".join(str_nums)
    
    # If result is all zeros, return "0"
    if result[0] == "0":
        return "0"
    
    return result


# Main execution
if __name__ == "__main__":
    # Test case
    nums = list(map(int, input("Enter numbers: ").split()))
    
    result = largestNumber(nums)
    print(result)
    
    # Additional test cases
    print("\n--- Additional Test Cases ---")
    test_cases = [
        [10, 2],
        [3, 30, 34, 5, 9],
        [0, 0],
        [1],
        [34323, 3432332],
    ]
    
    for nums in test_cases:
        print(f"{nums} -> {largestNumber(nums)}")
