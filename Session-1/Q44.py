# Q44: Function to find all prime numbers up to n
# Returns list of primes using mathematical property

# Input: Get number from user
num = int(input())

# Define function to find primes
def prime(num):
    # Initialize empty list to store primes
    ans = []
    
    # Check all numbers from 1 to num
    for i in range(1, num+1):
        # Numbers less than 3 are considered prime
        if(i<3):
            ans.append(i)
        # Numbers following 6k±1 pattern are prime
        elif(i%6==1 or i%6==5):
            ans.append(i)
    
    # Return list of primes
    return ans

# Call function and print result
print(prime(num))