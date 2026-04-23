# Q29: Check if number is prime using mathematical property
# All primes > 3 are of form 6k±1

# Input: Get number from user
num = int(input())

# Calculate neighbors
n1 = num-1
n2 = num+1

# Check if either neighbor is divisible by 6
if(n1%6==0 or n2%6==0):
    # Number follows prime pattern
    print("Prime Number")
else:
    # Number doesn't follow prime pattern
    print("Not a prime number")