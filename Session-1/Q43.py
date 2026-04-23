# Q43: Function to sum all digits of a number
# Extracts each digit and accumulates the sum

# Input: Get number from user
num = int(input())

# Define function to count digit sum
def count(num):
    # Initialize sum to zero
    sum = 0
    
    # Process each digit
    while(num>0):
        # Extract last digit
        temp = num%10
        # Add digit to sum
        sum = sum+temp
        # Remove last digit
        num = num//10
    
    # Return total sum of digits
    return sum

# Call function and print result
print(count(num))
