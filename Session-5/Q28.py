"""
Q28: Repeated DNA Sequences

Problem: Find all 10-letter DNA sequences that appear more than once.
"""


def findRepeatedDnaSequences(s):
    """
    Find all 10-letter sequences that occur more than once.
    
    Using sliding window and hash set approach.
    
    Args:
        s: DNA sequence string
    
    Returns:
        List of repeated 10-letter sequences (sorted)
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(s) < 10:
        return []
    
    seen = set()
    result = set()
    
    # Sliding window of size 10
    for i in range(len(s) - 9):
        sequence = s[i:i+10]
        
        if sequence in seen:
            result.add(sequence)
        else:
            seen.add(sequence)
    
    return sorted(list(result))


def findRepeatedDnaSequencesOptimized(s):
    """
    Optimized version using bit masking for DNA sequences.
    
    Maps: A=0, C=1, G=2, T=3 (2 bits each)
    10 nucleotides = 20 bits, fits in integer.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(s) < 10:
        return []
    
    # Map characters to bits
    char_to_bit = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    seen = set()
    result = set()
    
    # Create hash for first sequence
    hash_val = 0
    for i in range(10):
        hash_val = (hash_val << 2) | char_to_bit[s[i]]
    
    seen.add(hash_val)
    
    # Sliding window
    mask = (1 << 20) - 1  # Mask for 10 characters (20 bits)
    
    for i in range(10, len(s)):
        # Remove leftmost character and add new rightmost character
        hash_val = ((hash_val << 2) | char_to_bit[s[i]]) & mask
        
        if hash_val in seen:
            result.add(s[i-9:i+1])
        else:
            seen.add(hash_val)
    
    return sorted(list(result))


# Main execution
if __name__ == "__main__":
    # Test case
    s = input("Enter DNA sequence: ").strip()
    
    result = findRepeatedDnaSequences(s)
    print(" ".join(result) if result else "")
    
    # Additional test cases
    print("\n--- Additional Test Cases ---")
    test_cases = [
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "AAAAAAAAAAAAA",
        "ACGT",
        "AAAAACCCCCAAAAACCCCACABBBBBCD",
    ]
    
    for s in test_cases:
        result = findRepeatedDnaSequences(s)
        print(f"Input: {s}")
        print(f"Output: {' '.join(result) if result else 'No repeats'}")
        print()
