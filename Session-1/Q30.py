# Q30: Print prime numbers from 0 to 100
# Uses mathematical property: primes > 3 follow 6k±1 pattern

# Loop through numbers 0 to 100
for i in range(101):
    # Check if number is prime (i%6==1 or i%6==5)
    if(i%6==1 or i%6==5):
        # Print prime number
        print(i)
