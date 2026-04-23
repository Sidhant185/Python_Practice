# Q9: Count frequency of each element in array
# Uses dictionary to track occurrences

# Input: Get array from space-separated input
nums = list(map(int, input().split()))

# Initialize frequency dictionary
frequency = {}

# Count frequency of each element
for i in nums:
    # Use get() to handle missing keys, default to 0
    frequency[i] = frequency.get(i,0)+1

# Output: Print frequency of each element
for num, count in frequency.items():
    print(f"{num}: {count} times")
