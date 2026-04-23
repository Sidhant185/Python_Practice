"""
Q20: Koko Eating Bananas

Problem: Find the minimum eating speed k such that Koko can eat all bananas within h hours.
"""


def minEatingSpeed(piles, h):
    """
    Find minimum eating speed for Koko.
    
    Args:
        piles: List of pile sizes
        h: Hours available
    
    Returns:
        Minimum bananas per hour needed
    
    Time Complexity: O(n * log(max_pile))
    Space Complexity: O(1)
    """
    def canFinish(speed):
        """Check if Koko can finish all bananas at given speed within h hours"""
        hours = 0
        for pile in piles:
            # Ceiling division: (pile + speed - 1) // speed
            hours += (pile + speed - 1) // speed
        return hours <= h
    
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        if canFinish(mid):
            right = mid  # Try slower speed
        else:
            left = mid + 1  # Need faster speed
    
    return left


# Main execution
if __name__ == "__main__":
    # Test case
    n = int(input("Enter number of piles: "))
    piles = list(map(int, input("Enter pile sizes: ").split()))
    h = int(input("Enter hours available: "))
    
    result = minEatingSpeed(piles, h)
    print(result)
    
    # Additional test cases
    print("\n--- Additional Test Cases ---")
    test_cases = [
        ([3, 6, 7, 11], 8),
        ([312884132], 968709470),
        ([1, 1, 1, 1], 4)
    ]
    
    for piles, h in test_cases:
        print(f"piles={piles}, h={h} -> {minEatingSpeed(piles, h)}")
