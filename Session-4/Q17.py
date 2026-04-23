# Q17: Multiply Strings (Large Numbers)
# Multiply two numbers represented as strings

def multiply(num1, num2):
    """
    Multiply two large numbers represented as strings
    Uses grade-school multiplication algorithm
    Time Complexity: O(m*n) where m,n are lengths
    Space Complexity: O(m+n)
    """
    # Handle zero cases
    if num1 == "0" or num2 == "0": 
        return "0"
    
    # Create result array with max possible length
    res = [0] * (len(num1) + len(num2))
    
    # Multiply each digit of num1 with each digit of num2
    # Process from right to left (least significant to most)
    for i in range(len(num1)-1, -1, -1):
        for j in range(len(num2)-1, -1, -1):
            # Multiply digits
            mul = int(num1[i]) * int(num2[j])
            
            # Calculate positions in result
            p1, p2 = i + j, i + j + 1
            
            # Add to existing value
            total = mul + res[p2]
            
            # Store digit and handle carry
            res[p2] = total % 10
            res[p1] += total // 10
    
    # Remove leading zeros
    start = 0
    while start < len(res) and res[start] == 0: 
        start += 1
    
    # Convert to string and return
    return "".join(map(str, res[start:]))