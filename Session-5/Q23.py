"""
Q23: The Archivist's Cleanup

Problem: Count how many columns need to be deleted so all remaining columns are
sorted in non-decreasing order.
"""


def deletedColumnsCount(records):
    """
    Count columns that need to be deleted.
    
    Args:
        records: List of strings (same length)
    
    Returns:
        Number of columns to delete
    
    Time Complexity: O(m * n) where m is number of rows, n is string length
    Space Complexity: O(1)
    """
    if not records:
        return 0
    
    n_rows = len(records)
    n_cols = len(records[0])
    
    count = 0
    
    # Check each column
    for col in range(n_cols):
        # Check if this column is sorted
        is_sorted = True
        for row in range(n_rows - 1):
            if records[row][col] > records[row + 1][col]:
                is_sorted = False
                break
        
        # If not sorted, increment count
        if not is_sorted:
            count += 1
    
    return count


# Main execution
if __name__ == "__main__":
    # Test case
    n = int(input("Enter number of records: "))
    records = []
    for _ in range(n):
        records.append(input("Enter record: "))
    
    result = deletedColumnsCount(records)
    print(result)
    
    # Additional test cases
    print("\n--- Additional Test Cases ---")
    test_cases = [
        ["cba", "daf", "ghi"],  # Column 1 is not sorted (b > a)
        ["a", "b"],  # All sorted
        ["zyx", "wvu", "tsr"],  # No columns sorted
        ["dcba"],  # Single row
        ["abcd", "efgh"],
    ]
    
    for records in test_cases:
        print(f"{records} -> {deletedColumnsCount(records)}")
