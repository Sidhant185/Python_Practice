nums = []
for i in range(3):
    num = int(input("Enter Your Number: "))
    nums.append(num)

nums.sort()
print(nums)

if(nums[0]+nums[1]>nums[2]):
    print("Valid")
elif(nums[2]+nums[0]>nums[1]):
    print("Valid")
elif(nums[2]+nums[1]>nums[0]):
    print("Valid")
else:
    print("Not Valid")