# Q42: Function to reverse a number
# Extracts digits and rebuilds in reverse order

# Input: Get number from user
num = int(input())

# Define function to reverse number
def reverse(num):
    # Save original number
    temp = num
    # Initialize reverse to zero
    rev = 0
    
    # Extract and reverse digits
    while(temp>0):
        # Get last digit
        tem = temp%10
        # Add digit to reversed number
        rev = (rev*10)+tem
        # Remove last digit
        temp = temp//10
    
    # Return reversed number
    return rev

# Call function and print result
print(reverse(num))