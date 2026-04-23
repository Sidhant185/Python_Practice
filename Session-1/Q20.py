# Q20: Reverse a number
# Extracts digits one by one and rebuilds number in reverse order

# Input: Get number to reverse
num = int(input())

# Initialize reverse number
rev = 0

# Process each digit from right to left
while(num>0):
    # Extract last digit using modulo
    temp = num%10
    
    # Add digit to reversed number at correct position
    rev = (rev*10)+temp
    
    # Remove last digit from original number
    num = num//10

# Output: Print reversed number
print(rev)