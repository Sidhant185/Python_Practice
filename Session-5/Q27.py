"""
Q27: Maximum Units on a Truck

Problem: Maximize units loaded on truck using greedy approach.
"""


def maximumUnits(boxTypes, truckSize):
    """
    Find maximum units that can fit on truck.
    
    Greedy approach: Sort by units per box in descending order and fill truck.
    
    Args:
        boxTypes: List of [numberOfBoxes, numberOfUnitsPerBox]
        truckSize: Maximum boxes truck can carry
    
    Returns:
        Maximum total units
    
    Time Complexity: O(n log n)
    Space Complexity: O(1) excluding input
    """
    # Sort by units per box in descending order
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    
    total_units = 0
    boxes_loaded = 0
    
    for num_boxes, units_per_box in boxTypes:
        # How many boxes of this type can we take?
        boxes_to_take = min(num_boxes, truckSize - boxes_loaded)
        
        total_units += boxes_to_take * units_per_box
        boxes_loaded += boxes_to_take
        
        # If truck is full, stop
        if boxes_loaded == truckSize:
            break
    
    return total_units


# Main execution
if __name__ == "__main__":
    # Test case
    n = int(input("Enter number of box types: "))
    boxTypes = []
    for _ in range(n):
        num_boxes, units = map(int, input(f"Enter box type (boxes units): ").split())
        boxTypes.append([num_boxes, units])
    
    truckSize = int(input("Enter truck size: "))
    
    result = maximumUnits(boxTypes, truckSize)
    print(result)
    
    # Additional test cases
    print("\n--- Additional Test Cases ---")
    test_cases = [
        ([[1, 3], [2, 2], [3, 1]], 4),
        ([[5, 10], [2, 5], [4, 7], [3, 9]], 10),
        ([[1, 1]], 1),
        ([[1000000, 1000000]], 1),
    ]
    
    for boxTypes, truckSize in test_cases:
        result = maximumUnits(boxTypes.copy(), truckSize)
        print(f"boxTypes={boxTypes}, truckSize={truckSize} -> {result}")
