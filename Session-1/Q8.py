# Q8: Find the largest among three numbers
# Reads three numbers, stores in list, and finds maximum

# Input: Get three numbers from user
n1 = int(input())
n2 = int(input())
n3 = int(input())

# Create empty list to store numbers
nums = []

# Add all three numbers to the list
nums.append(n1)
nums.append(n2)
nums.append(n3)

# Output: Display all numbers
print(nums)

# Initialize largest with first number
largest = n1

# Iterate through list to find maximum
for i in range(3):
    # Update largest if current number is greater
    if(nums[i]>largest):
        largest = nums[i]

# Output: Display largest number
print(largest)