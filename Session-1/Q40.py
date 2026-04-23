# Q40: Function to calculate factorial
# Uses loop to multiply numbers from 1 to num

# Input: Get number from user
num = int(input())

# Define function to calculate factorial
def fact(num):
    # Initialize factorial to 1
    fact = 1
    
    # Multiply all numbers from 1 to num
    for i in range(1,num+1):
        # Accumulate product
        fact = fact*i
    
    # Return calculated factorial
    return fact

# Call function and print result
print(fact(num))