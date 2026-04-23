# Q3: Count even and odd numbers in array
# Uses modulo operator to classify numbers

# Initialize empty list
nums = []

# Input: Get size of array
size = int(input())

# Input: Read all array elements
for i in range(size):
    nums.append(int(input()))

# Initialize counters
even = 0
odd = 0

# Iterate through all elements
for j in range(size):
    # Check if number is even (divisible by 2)
    if(nums[j]%2==0):
        # Increment even counter
        even = even+1
    else:
        # Increment odd counter
        odd = odd+1

# Output: Print count of even numbers
print(even)

# Output: Print count of odd numbers
print(odd)