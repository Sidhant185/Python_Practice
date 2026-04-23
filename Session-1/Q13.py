# Q13: Check if three numbers can form a valid triangle
# Uses triangle inequality theorem: sum of any two sides > third side

# Create empty list to store numbers
nums = []

# Input: Get three numbers from user
for i in range(3):
    num = int(input("Enter Your Number: "))
    nums.append(num)

# Sort numbers in ascending order for easier comparison
nums.sort()

# Output: Display sorted numbers
print(nums)

# Check triangle inequality: sum of two smaller sides > largest side
if(nums[0]+nums[1]>nums[2]):
    print("Valid")
elif(nums[2]+nums[0]>nums[1]):
    print("Valid")
elif(nums[2]+nums[1]>nums[0]):
    print("Valid")
else:
    # All conditions failed
    print("Not Valid")