"""
Q24: Relative Ranks

Problem: Rank athletes based on their scores and return their ranks.
"""


def findRelativeRanks(score):
    """
    Return ranks for athletes based on scores.
    
    Ranks:
    - 1st place: "Gold Medal"
    - 2nd place: "Silver Medal"
    - 3rd place: "Bronze Medal"
    - 4th onwards: Position number as string
    
    Args:
        score: List of unique scores
    
    Returns:
        List of rank strings in original order
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    n = len(score)
    
    # Create list of (score, original_index)
    indexed_scores = [(score[i], i) for i in range(n)]
    
    # Sort by score in descending order
    indexed_scores.sort(reverse=True, key=lambda x: x[0])
    
    # Create result array
    result = [""] * n
    
    # Assign ranks
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    for rank, (_, original_idx) in enumerate(indexed_scores):
        if rank < 3:
            result[original_idx] = medals[rank]
        else:
            result[original_idx] = str(rank + 1)
    
    return result


# Main execution
if __name__ == "__main__":
    # Test case
    n = int(input("Enter number of athletes: "))
    scores = list(map(int, input("Enter scores: ").split()))
    
    result = findRelativeRanks(scores)
    print(" ".join(result))
    
    # Additional test cases
    print("\n--- Additional Test Cases ---")
    test_cases = [
        [5, 4, 3, 2, 1],
        [10, 3, 8, 9, 4],
        [1],
        [2, 1],
    ]
    
    for scores in test_cases:
        print(f"{scores} -> {findRelativeRanks(scores)}")
