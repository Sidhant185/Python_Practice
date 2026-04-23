# Q1: Isomorphic Strings
# Determine if string s can be transformed into string t by replacing characters
# One-to-one mapping required (no two different chars map to same char)

def isIsomorphic(s: str, t: str) -> bool:
    """
    Check if s and t are isomorphic strings.
    Uses two dictionaries to maintain bijection (one-to-one mapping).
    
    Time Complexity: O(n) where n is length of strings
    Space Complexity: O(1) - at most 26 unique characters
    
    Args:
        s: Original string
        t: Target string
    
    Returns:
        True if s can be transformed to t with one-to-one mapping
    """
    if len(s) != len(t):
        return False
    
    # Dictionary to map characters from s to t
    s_to_t = {}
    # Dictionary to ensure no two characters from s map to same character in t
    t_to_s = {}
    
    # Process each character pair
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        # Check if s[i] already has a mapping
        if char_s in s_to_t:
            # Verify it maps to same character in t
            if s_to_t[char_s] != char_t:
                return False
        else:
            # Create new mapping
            s_to_t[char_s] = char_t
        
        # Check if t[i] is already mapped from another character
        if char_t in t_to_s:
            # Verify it maps from same character in s
            if t_to_s[char_t] != char_s:
                return False
        else:
            # Create new reverse mapping
            t_to_s[char_t] = char_s
    
    return True


# Main execution
if __name__ == "__main__":
    # Test case 1
    s1 = input("Enter first string: ").strip()
    t1 = input("Enter second string: ").strip()
    
    result = isIsomorphic(s1, t1)
    print("true" if result else "false")
    
    # Additional test cases
    print("\n--- Additional Test Cases ---")
    test_cases = [
        ("egg", "add"),
        ("badc", "baba"),
        ("ab", "aa"),
        ("paper", "title")
    ]
    
    for s, t in test_cases:
        print(f"s='{s}', t='{t}' -> {isIsomorphic(s, t)}")
