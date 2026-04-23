# Q34: Sum numbers until sum reaches 100
# Uses break statement to exit loop early

# Initialize sum to zero
sum = 0

# Input: Get starting number
num = int(input())

# Add consecutive numbers starting from num
for i in range(1,num+1):
    # Check if sum has reached or exceeded 100
    if(sum>=100):
        # Exit loop
        break
    else:
        # Add current number to sum
        sum = sum+i

# Output: Print final sum
print(sum)