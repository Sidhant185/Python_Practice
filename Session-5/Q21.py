"""
Q21: Sorting the Treasure Chest

Problem: Sort an array of integers in ascending order.
"""


def sortArray(nums):
    """
    Sort array in ascending order using built-in sort.
    
    Args:
        nums: List of integers
    
    Returns:
        Sorted list
    
    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n) depending on sort implementation
    """
    return sorted(nums)


def sortArrayManual(nums):
    """
    Sort array using merge sort algorithm.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(nums) <= 1:
        return nums
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def mergeSort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        return merge(left, right)
    
    return mergeSort(nums)


# Main execution
if __name__ == "__main__":
    # Test case
    n = int(input("Enter number of elements: "))
    nums = list(map(int, input("Enter elements: ").split()))
    
    result = sortArray(nums)
    print(result)
    
    # Additional test cases
    print("\n--- Additional Test Cases ---")
    test_cases = [
        [5, 2, 3, 1],
        [64, 34, 25, 12, 22, 11, 90],
        [-5, -2, 0, 3, 10],
        [1]
    ]
    
    for nums in test_cases:
        print(f"{nums} -> {sortArray(nums)}")
