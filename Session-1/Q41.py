# Q41: Function to check if number is prime
# Uses mathematical property: primes > 3 follow 6k±1 pattern

# Input: Get number from user
num = int(input())

# Define function to check primality
def check(num):
    # Numbers less than 3 are considered prime (for this logic)
    if(num<3):
        return "prime"
    
    # Check if number follows prime pattern (6k±1)
    if(num%6==1 or num%6==5):
        return "prime"
    else:
        return "Not Prime"

# Call function and print result
print(check(num))