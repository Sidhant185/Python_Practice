# 🔥 SESSION 3: Advanced Problem Solving - Python Practice Guide

## Overview
Session 3 covers advanced algorithmic concepts including hashing, sliding windows, greedy algorithms, matrix problems, strings, and combinatorics. This guide provides detailed explanations, examples, and solutions for 130+ problems organized into 13 focused sets.

---

## 🔥 SET 1 — Two Sum / Pair Logic / Hashing (10 Problems)

### Problem 1: Pair Sum = Target
**Problem Statement:**
Given an unsorted array of integers and a target sum, check if any two different numbers in the array add up to the target.

**Examples:**
```python
# Example 1
arr = [1, 5, 7, -1, 5]
target = 6
Output: True  # (1, 5) or (7, -1) both sum to 6

# Example 2
arr = [2, 7, 11, 15]
target = 9
Output: True  # (2, 7)

# Example 3
arr = [1, 2, 3]
target = 10
Output: False  # No pair sums to 10
```

**What to Use / NOT Use:**
- ✅ Use: Hash Set for O(n) time solution
- ✅ Use: Two pointers if array is sorted
- ❌ Avoid: Nested loop (O(n²) time)
- ❌ Avoid: Modifying input array unnecessarily

**Key Concepts:**
- Hash Set allows O(1) lookup
- For each element, check if (target - element) exists in set
- Avoid counting same element twice

**Solution Approaches:**
```python
# Approach 1: Hash Set (Optimal)
def pairSum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
    return False

# Approach 2: Two Pointers (Requires Sorted Array)
def pairSum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False
```

**Complexity Analysis:**
- Time: O(n) hash set, O(n log n) two pointers
- Space: O(n) for hash set

**Key Points:**
- Hash set approach works for unsorted arrays
- Two pointers require sorting but have less space overhead
- Early exit when pair is found

---

### Problem 2: Two Sum - Return Indices
**Problem Statement:**
Given an array of integers and a target, return the indices of the two numbers that add up to the target. Assume each input has exactly one solution and cannot use the same element twice.

**Examples:**
```python
# Example 1
nums = [2, 7, 11, 15]
target = 9
Output: [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9

# Example 2
nums = [3, 2, 4]
target = 6
Output: [1, 2]  # nums[1] + nums[2] = 2 + 4 = 6
```

**What to Use / NOT Use:**
- ✅ Use: Dictionary mapping value to index
- ✅ Use: Single pass through array
- ❌ Avoid: Sorting (loses original indices)

**Key Concepts:**
- Map values to their original indices
- Store indices in dictionary while iterating
- Complement-based lookup

**Solution:**
```python
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
```

**Complexity Analysis:**
- Time: O(n) - single pass
- Space: O(n) - dictionary storage

---

### Problem 3: Count Pairs with Given Sum
**Problem Statement:**
Count the total number of pairs in an array that sum to a target value.

**Examples:**
```python
# Example 1
arr = [1, 5, 7, -1, 5]
target = 6
Output: 2  # (1,5) at indices (0,1) and (1,4)

# Example 2
arr = [1, 1, 1, 1]
target = 2
Output: 6  # All pairs of 1's sum to 2
```

**Key Concepts:**
- Use frequency map for duplicates
- For each element, count occurrences of complement
- Handle edge case when element = target/2

**Solution:**
```python
def countPairs(arr, target):
    count = 0
    freq = {}
    
    for num in arr:
        complement = target - num
        if complement in freq:
            count += freq[complement]
        freq[num] = freq.get(num, 0) + 1
    
    return count
```

**Complexity Analysis:**
- Time: O(n)
- Space: O(n)

---

### Problem 4: Pair with Difference K
**Problem Statement:**
Find if any pair of elements has an absolute difference of K.

**Examples:**
```python
arr = [1, 5, 7, 2, 9]
k = 4
Output: True  # |5-1| = 4

arr = [1, 3, 5]
k = 2
Output: True  # |3-1| = 2 and |5-3| = 2
```

**Solution:**
```python
def pairWithDifference(arr, k):
    num_set = set()
    for num in arr:
        if num - k in num_set or num + k in num_set:
            return True
        num_set.add(num)
    return False
```

---

### Problem 5: Find All Unique Pairs Summing to Target
**Problem Statement:**
Find all unique pairs of numbers that sum to target, returning each pair once.

**Examples:**
```python
arr = [1, 5, 7, -1, 5]
target = 6
Output: [(1, 5), (-1, 7)]

arr = [1, 2, 3, 4, 5]
target = 5
Output: [(1, 4), (2, 3)]
```

**Key Concepts:**
- Sort array to avoid duplicates
- Use two pointers from both ends
- Skip duplicate values

**Solution:**
```python
def uniquePairs(arr, target):
    arr.sort()
    pairs = []
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            # Skip duplicates
            while left < right and arr[left] == arr[left + 1]:
                left += 1
            while left < right and arr[right] == arr[right - 1]:
                right -= 1
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return pairs
```

---

### Problem 6: Subarray with Given Sum
**Problem Statement:**
Find if there exists a contiguous subarray whose sum equals the target.

**Examples:**
```python
arr = [1, 4, 20, 3, 10, 5]
target = 33
Output: True  # Subarray [20, 3, 10] sums to 33

arr = [1, 2, 3, 7, 5]
target = 12
Output: True  # Subarray [2, 3, 7] sums to 12
```

**Key Concepts:**
- Prefix sum approach
- Use hash map to store cumulative sums
- For each position, check if (current_sum - target) was seen before

**Solution:**
```python
def subarraySum(arr, target):
    sum_map = {0: 1}  # Initialize with 0 sum seen once
    current_sum = 0
    
    for num in arr:
        current_sum += num
        if current_sum - target in sum_map:
            return True
        sum_map[current_sum] = sum_map.get(current_sum, 0) + 1
    
    return False
```

---

### Problem 7: Longest Subarray with Sum = K
**Problem Statement:**
Find the maximum length of a contiguous subarray that sums to exactly K.

**Examples:**
```python
arr = [15, 2, 4, 8, 9, 5, 10, 23]
k = 23
Output: 5  # Subarray [4, 8, 9, 5, -3] or [2, 4, 8, 9]

arr = [1, 2, 3, 1, 1, 1, 1, 3, 3, 4, 2]
k = 6
Output: 4  # Subarray [1, 2, 3] or [2, 1, 1, 2]
```

**Solution:**
```python
def longestSubarraySum(arr, k):
    sum_map = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        if current_sum - k in sum_map:
            max_length = max(max_length, i - sum_map[current_sum - k])
        if current_sum not in sum_map:
            sum_map[current_sum] = i
    
    return max_length
```

---

### Problem 8: Sorted Array Pair Check
**Problem Statement:**
For a sorted array, efficiently find if a pair exists with given sum.

**Examples:**
```python
arr = [-1, 1, 3, 5, 7, 9]
target = 8
Output: True  # 1 + 7 = 8
```

**Solution (Two Pointers - Optimal for Sorted):**
```python
def pairInSorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

### Problem 9: Triplet Sum = Target
**Problem Statement:**
Find all unique triplets in array that sum to target.

**Examples:**
```python
arr = [-1, 0, 1, 2, -1, -4]
target = 0
Output: [[-1, -1, 2], [-1, 0, 1]]
```

**Solution:**
```python
def tripletSum(arr, target):
    arr.sort()
    triplets = []
    
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                triplets.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return triplets
```

**Complexity:**
- Time: O(n²)
- Space: O(1) excluding output

---

### Problem 10: 4Sum Problem
**Problem Statement:**
Find all unique quadruplets that sum to target.

**Examples:**
```python
arr = [1000000000, 1000000000, 1000000000, 1000000000]
target = -294967296
Output: [] (No quadruplet sums to target)
```

**Key Concepts:**
- Extend triplet approach with another nested loop
- Careful duplicate handling at each level
- Use early termination when minimum possible sum exceeds target

**Solution:**
```python
def fourSum(arr, target):
    arr.sort()
    n = len(arr)
    result = []
    
    for i in range(n - 3):
        # Skip duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        # Early termination
        if arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3] > target:
            break
        if arr[i] + arr[n - 1] + arr[n - 2] + arr[n - 3] < target:
            continue
        
        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            
            left, right = j + 1, n - 1
            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if current_sum == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    
    return result
```

**Complexity:**
- Time: O(n³)
- Space: O(1) excluding output
## 🔥 SET 2 — Nearby Duplicate / Sliding Window (10 Problems)

### Problem 11: Nearby Duplicate (Distance K)
**Problem Statement:**
Given an array of integers and an integer `k`, return `True` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

**Examples:**
```python
# Example 1
nums = [1, 2, 3, 1], k = 3
Output: True

# Example 2
nums = [1, 0, 1, 1], k = 1
Output: True

# Example 3
nums = [1, 2, 3, 1, 2, 3], k = 2
Output: False
```

**Key Concepts:**
- Use a **Sliding Window** with a Hash Set.
- Maintain a set of elements currently in the window of size `k`.
- If the current element is already in the set, a duplicate within distance `k` exists.

**Solution:**
```python
def containsNearbyDuplicate(nums, k):
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False
```

**Complexity Analysis:**
- Time: O(n) - single pass.
- Space: O(min(n, k)) - set stores at most k elements.

---

### Problem 12: Contains Duplicate (Any)
**Problem Statement:**
Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.

**Examples:**
```python
nums = [1, 2, 3, 1]
Output: True

nums = [1, 2, 3, 4]
Output: False
```

**Solution Approaches:**
```python
# Approach 1: Hash Set (Optimal)
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# Approach 2: Sorting
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False
```

**Complexity Analysis:**
- Approach 1: Time O(n), Space O(n)
- Approach 2: Time O(n log n), Space O(1) (depending on sort)

---

### Problem 13: Contains Duplicate II (Index Constraint)
**Problem Statement:**
Find if two elements at indices `i` and `j` are equal and `abs(i-j) <= k`. (Variation of Problem 11 focusing on Dictionary approach).

**Solution (Dictionary Approach):**
```python
def containsDuplicateII(nums, k):
    num_map = {} # val -> index
    for i, num in enumerate(nums):
        if num in num_map and i - num_map[num] <= k:
            return True
        num_map[num] = i
    return False
```

---

### Problem 14: Longest Substring Without Repeating Characters
**Problem Statement:**
Given a string `s`, find the length of the longest substring without repeating characters.

**Examples:**
```python
s = "abcabcbb"
Output: 3 # "abc"

s = "bbbbb"
Output: 1 # "b"
```

**Key Concepts:**
- Sliding Window with two pointers (`left`, `right`).
- Use a dictionary to store the last seen index of each character.

**Solution:**
```python
def lengthOfLongestSubstring(s):
    char_map = {}
    max_len = left = 0
    
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len
```

**Complexity Analysis:**
- Time: O(n)
- Space: O(min(m, n)) where m is charset size.

---

### Problem 15: Sliding Window Maximum
**Problem Statement:**
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. Return the max sliding window.

**Examples:**
```python
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
```

**Key Concepts:**
- Use a **Deque** (Double-ended queue) to store indices.
- Maintain the deque such that elements are in decreasing order.

**Solution:**
```python
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    res = []
    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
```

---

### Problem 16: Minimum Window Substring
**Problem Statement:**
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window.

**Examples:**
```python
s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Solution:**
```python
from collections import Counter

def minWindow(s, t):
    if not t or not s: return ""
    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None

    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        while l <= r and formed == required:
            char = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            l += 1    
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
```

---

### Problem 17: Distinct Elements in Every Window
**Problem Statement:**
Given an array and an integer `k`, count distinct elements in every window of size `k`.

**Examples:**
```python
arr = [1, 2, 1, 3, 4, 2, 3], k = 4
Output: [3, 4, 4, 3]
```

**Solution:**
```python
def countDistinct(arr, k):
    res = []
    freq = {}
    for i in range(k):
        freq[arr[i]] = freq.get(arr[i], 0) + 1
    res.append(len(freq))
    
    for i in range(k, len(arr)):
        # Remove first element of prev window
        out = arr[i-k]
        freq[out] -= 1
        if freq[out] == 0: del freq[out]
        # Add new element
        freq[arr[i]] = freq.get(arr[i], 0) + 1
        res.append(len(freq))
    return res
```

---

### Problem 18: At most K Distinct Subarray
**Problem Statement:**
Find the length of the longest subarray with at most `k` distinct elements.

**Solution:**
```python
def longestSubarrayAtMostK(arr, k):
    freq = {}
    l = 0
    max_len = 0
    for r in range(len(arr)):
        freq[arr[r]] = freq.get(arr[r], 0) + 1
        while len(freq) > k:
            freq[arr[l]] -= 1
            if freq[arr[l]] == 0: del freq[freq[arr[l]]]
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len
```

---

### Problem 19: Longest Repeating Character Replacement
**Problem Statement:**
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

**Solution:**
```python
def characterReplacement(s, k):
    count = {}
    max_f = 0
    l = 0
    res = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_f = max(max_f, count[s[r]])
        if (r - l + 1) - max_f > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
```

---

### Problem 20: Fruits into Baskets
**Problem Statement:**
You are visiting a farm that has a single row of fruit trees listed from left to right. You have two baskets, and each basket can only hold a single type of fruit. What is the maximum number of fruits you can collect? (Essentially: Longest subarray with at most 2 distinct elements).

**Solution:**
```python
def totalFruit(fruits):
    count = {}
    l = 0
    max_fruits = 0
    for r in range(len(fruits)):
        count[fruits[r]] = count.get(fruits[r], 0) + 1
        while len(count) > 2:
            count[fruits[l]] -= 1
            if count[fruits[l]] == 0: del count[fruits[l]]
            l += 1
        max_fruits = max(max_fruits, r - l + 1)
    return max_fruits
```

## 🔥 SET 3 — Greedy / Placement Problems (10 Problems)

### Problem 21: Garden Plot Allocation
**Problem Statement:**
You have a row of garden plots. Some are planted, some are not. You cannot plant in adjacent plots. Given an array `plots` (0 for empty, 1 for planted) and a number `n`, return `True` if `n` new flowers can be planted.

**Examples:**
```python
plots = [1, 0, 0, 0, 1], n = 1
Output: True # Can plant at index 2

plots = [1, 0, 0, 0, 1], n = 2
Output: False
```

**Solution:**
```python
def canPlaceFlowers(flowerbed, n):
    count = 0
    f = [0] + flowerbed + [0] # Add padding to handle boundaries
    for i in range(1, len(f) - 1):
        if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            count += 1
    return count >= n
```

---

### Problem 22: Can Place Flowers
**Problem Statement:**
Similar to Problem 21, but focus on the greedy logic of checking `i-1`, `i`, and `i+1`. (This is essentially the same problem, provided as a variation).

**Key Concepts:**
- Greedy: Plant a flower whenever you find three consecutive 0s.
- Optimization: Stop early if `count >= n`.

---

### Problem 23: Jump Game
**Problem Statement:**
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return `True` if you can reach the last index.

**Examples:**
```python
nums = [2, 3, 1, 1, 4]
Output: True

nums = [3, 2, 1, 0, 4]
Output: False
```

**Solution (Greedy):**
```python
def canJump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True
```

---

### Problem 24: Jump Game II
**Problem Statement:**
Find the minimum number of jumps to reach the last index.

**Solution:**
```python
def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
```

---

### Problem 25: Gas Station
**Problem Statement:**
There are `n` gas stations along a circular route. You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from station `i` to `i+1`. Given `gas` and `cost` arrays, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

**Solution:**
```python
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost): return -1
    
    total_gas = 0
    start_index = 0
    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        if total_gas < 0:
            total_gas = 0
            start_index = i + 1
            
    return start_index
```

---

### Problem 26: Assign Cookies
**Problem Statement:**
Assume you are an awesome parent and want to give your children some cookies. Each child `i` has a greed factor `g[i]`, and each cookie `j` has a size `s[j]`. You can assign cookie `j` to child `i` only if `s[j] >= g[i]`. Maximize the number of content children.

**Solution:**
```python
def findContentChildren(g, s):
    g.sort()
    s.sort()
    child_i = 0
    cookie_j = 0
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1
        cookie_j += 1
    return child_i
```

---

### Problem 27: Activity Selection
**Problem Statement:**
You are given `n` activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

**Solution:**
```python
def activitySelection(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])
    count = 0
    last_end_time = -1
    for s, e in activities:
        if s >= last_end_time:
            count += 1
            last_end_time = e
    return count
```

---

### Problem 28: Minimum Platforms
**Problem Statement:**
Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits.

**Solution:**
```python
def findPlatform(arr, dep):
    arr.sort()
    dep.sort()
    
    plat_needed = 0
    max_plat = 0
    i = 0
    j = 0
    
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            plat_needed += 1
            i += 1
        else:
            plat_needed -= 1
            j += 1
        max_plat = max(max_plat, plat_needed)
    return max_plat
```

---

### Problem 29: Candy Distribution
**Problem Statement:**
There are `n` children standing in a line. Each child is assigned a rating value. You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

**Solution:**
```python
def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    
    # Left to Right pass
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
            
    # Right to Left pass
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
            
    return sum(candies)
```

---

### Problem 30: Partition Labels
**Problem Statement:**
You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. Return a list of integers representing the size of these parts.

**Solution:**
```python
def partitionLabels(s):
    last = {c: i for i, c in enumerate(s)}
    j = anchor = 0
    ans = []
    for i, c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
    return ans
```

- [x] Batch 1: Set 2 (Sliding Window/Duplicates) & Set 3 (Greedy)
- [x] Batch 2: Set 4 (Minimize Difference) & Set 5 (Matrix Traversal)
- [x] Batch 3: Set 6 (Matrix Logic) & Set 7 (Matrix Patterns)
- [x] Batch 4: Set 8 (Pascal/Combinatorics) & Set 9 (String Basics)
- [x] Batch 5: Set 10 (String Frequency) & Set 11 (Binary Strings)
- [/] Batch 6: Set 12 (String Hard) & Set 13 (Special String Logic)

### Problem 31: Towers I
**Problem Statement:**
Given heights of `n` towers and a positive integer `k`, you have to either increase or decrease the height of every tower by `k` (only once). Find out the minimum possible difference between the height of the shortest and tallest towers after modification.

**Solution:**
```python
def getMinDiff(arr, k):
    arr.sort()
    n = len(arr)
    res = arr[n-1] - arr[0]
    
    for i in range(n-1):
        # Potential min and max after adding/subtracting k
        mini = min(arr[0] + k, arr[i+1] - k)
        maxi = max(arr[n-1] - k, arr[i] + k)
        res = min(res, maxi - mini)
    return res
```

---

### Problem 32: Towers II
**Problem Statement:**
Same as Towers I, but the resulting heights must be non-negative.

**Solution:**
```python
def getMinDiffII(arr, k):
    arr.sort()
    n = len(arr)
    res = arr[n-1] - arr[0]
    
    for i in range(n-1):
        if arr[i+1] < k: continue # Skip if subtraction results in negative
        mini = min(arr[0] + k, arr[i+1] - k)
        maxi = max(arr[n-1] - k, arr[i] + k)
        res = min(res, maxi - mini)
    return res
```

---

### Problem 33: Min Difference After Modification
**Problem Statement:**
Given an array, you can modify at most 3 elements. Minimize the difference between the maximum and minimum elements.

**Solution:**
```python
def minDifference(nums):
    if len(nums) <= 4: return 0
    nums.sort()
    # Options: 
    # 1. Kill 3 largest
    # 2. Kill 2 largest, 1 smallest
    # 3. Kill 1 largest, 2 smallest
    # 4. Kill 3 smallest
    return min(nums[-1] - nums[3], 
               nums[-2] - nums[2], 
               nums[-3] - nums[1], 
               nums[-4] - nums[0])
```

---

### Problem 34: Smallest Range Problem
**Problem Statement:**
You have `k` lists of sorted integers. Find the smallest range that includes at least one number from each of the `k` lists.

**Solution:**
```python
import heapq

def smallestRange(nums):
    pq = [(list[0], i, 0) for i, list in enumerate(nums)]
    heapq.heapify(pq)
    
    max_val = max(list[0] for list in nums)
    ans = -float('inf'), float('inf')
    
    while pq:
        min_val, row, col = heapq.heappop(pq)
        if max_val - min_val < ans[1] - ans[0]:
            ans = min_val, max_val
        
        if col + 1 == len(nums[row]):
            return ans
        
        next_val = nums[row][col+1]
        heapq.heappush(pq, (next_val, row, col+1))
        max_val = max(max_val, next_val)
```

---

### Problem 35: Minimize Max Difference Pairs
**Problem Statement:**
Given an array, pair up elements such that the maximum absolute difference among all pairs is minimized.

**Solution:**
```python
def minimizeMaxDiff(arr):
    arr.sort()
    max_diff = 0
    # Greedily pair adjacent elements
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):
            max_diff = max(max_diff, arr[i+1] - arr[i])
    return max_diff
```

---

### Problem 36: K Closest Elements
**Problem Statement:**
Given a sorted array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array.

**Solution:**
```python
def findClosestElements(arr, k, x):
    # Two pointers approach on sorted array
    l, r = 0, len(arr) - k
    while l < r:
        m = (l + r) // 2
        if x - arr[m] > arr[m + k] - x:
            l = m + 1
        else:
            r = m
    return arr[l : l + k]
```

---

### Problem 37: Chocolate Distribution
**Problem Statement:**
Given an array of `n` integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are `m` students, the task is to distribute chocolate packets such that:
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

**Solution:**
```python
def chocolateDistribution(arr, m):
    if m == 0 or len(arr) == 0: return 0
    arr.sort()
    n = len(arr)
    if n < m: return -1
    
    min_diff = float('inf')
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)
    return min_diff
```

---

### Problem 38: Minimize Sum Difference
**Problem Statement:**
Partition an array into two subsets such that the absolute difference between their sums is minimized.

**Solution (DP approach):**
```python
def minSubsetSumDiff(arr):
    total_sum = sum(arr)
    n = len(arr)
    dp = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]
    for i in range(n + 1): dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
                
    diff = float('inf')
    for j in range(total_sum // 2, -1, -1):
        if dp[n][j]:
            diff = total_sum - 2 * j
            break
    return diff
```

---

### Problem 39: Aggressive Cows
**Problem Statement:**
Given `n` stalls and `k` cows, place cows in stalls such that the minimum distance between any two of them is as large as possible.

**Solution (Binary Search on Answer):**
```python
def canPlace(stalls, k, dist):
    count = 1
    last_pos = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last_pos >= dist:
            count += 1
            last_pos = stalls[i]
    return count >= k

def aggressiveCows(stalls, k):
    stalls.sort()
    low, high = 1, stalls[-1] - stalls[0]
    res = 0
    while low <= high:
        mid = (low + high) // 2
        if canPlace(stalls, k, mid):
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res
```

---

### Problem 40: Painter Partition
**Problem Statement:**
Given `n` boards of length and `k` painters. Find the minimum time to paint all boards, where one painter takes 1 unit time to paint 1 unit of board. A painter can only paint contiguous boards.

**Solution (Binary Search on Answer):**
```python
def isPossible(boards, k, time):
    painters = 1
    current_time = 0
    for board in boards:
        if current_time + board <= time:
            current_time += board
        else:
            painters += 1
            current_time = board
            if painters > k: return False
    return True

def painterPartition(boards, k):
    low, high = max(boards), sum(boards)
    res = high
    while low <= high:
        mid = (low + high) // 2
        if isPossible(boards, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
```

## 🔥 SET 5 — Matrix Traversal / Patterns (10 Problems)

### Problem 41: Snake Pattern
**Problem Statement:**
Traverse a matrix in a snake-like pattern (left-to-right for row 0, right-to-left for row 1, etc.).

**Solution:**
```python
def printSnakePattern(mat):
    res = []
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                res.append(mat[i][j])
        else:
            for j in range(cols - 1, -1, -1):
                res.append(mat[i][j])
    return res
```

---

### Problem 42: Spiral Matrix
**Problem Statement:**
Given an `m x n` matrix, return all elements of the matrix in spiral order.

**Solution:**
```python
def spiralOrder(matrix):
    res = []
    if not matrix: return res
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Move Right
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        
        # Move Down
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Move Left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            
        if left <= right:
            # Move Up
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res
```

---

### Problem 43: Zigzag Traversal
**Problem Statement:**
Traverse a matrix in a zigzag (diagonal) manner.

**Solution:**
```python
def findDiagonalOrder(mat):
    if not mat or not mat[0]: return []
    rows, cols = len(mat), len(mat[0])
    res = []
    for d in range(rows + cols - 1):
        if d % 2 == 0:
            # Go Up-Right
            r = min(d, rows - 1)
            c = d - r
            while r >= 0 and c < cols:
                res.append(mat[r][c])
                r -= 1
                c += 1
        else:
            # Go Down-Left
            c = min(d, cols - 1)
            r = d - c
            while c >= 0 and r < rows:
                res.append(mat[r][c])
                r += 1
                c -= 1
    return res
```

---

### Problem 44: Diagonal Traversal
**Problem Statement:**
Return elements of a matrix as seen in diagonal traversal (variation focusing on simple sum of indices).

**Solution:**
```python
def diagonalTraversal(mat):
    rows, cols = len(mat), len(mat[0])
    res = []
    # Total number of diagonals = rows + cols - 1
    for d in range(rows + cols - 1):
        # r + c = d
        for r in range(max(0, d - cols + 1), min(d + 1, rows)):
            res.append(mat[r][d - r])
    return res
```

---

### Problem 45: Boundary Traversal
**Problem Statement:**
Print the boundary elements of a matrix in clockwise order.

**Solution:**
```python
def boundaryTraversal(mat):
    rows = len(mat)
    cols = len(mat[0])
    res = []
    if rows == 1: return mat[0]
    if cols == 1: return [mat[i][0] for i in range(rows)]
    
    # Top row
    for j in range(cols): res.append(mat[0][j])
    # Right col
    for i in range(1, rows): res.append(mat[i][cols-1])
    # Bottom row
    for j in range(cols-2, -1, -1): res.append(mat[rows-1][j])
    # Left col
    for i in range(rows-2, 0, -1): res.append(mat[i][0])
    return res
```

---

### Problem 46: Wave Traversal
**Problem Statement:**
Traverse matrix column-wise in a wave pattern (down for col 0, up for col 1, etc.).

**Solution:**
```python
def waveTraversal(mat):
    rows, cols = len(mat), len(mat[0])
    res = []
    for j in range(cols):
        if j % 2 == 0:
            for i in range(rows):
                res.append(mat[i][j])
        else:
            for i in range(rows - 1, -1, -1):
                res.append(mat[i][j])
    return res
```

---

### Problem 47: Row/Column Traversal
**Problem Statement:**
Basic iteration over rows and columns.

**Solution:**
```python
# Simple Row-major
def rowMajor(mat):
    return [val for row in mat for val in row]

# Simple Column-major
def colMajor(mat):
    return [mat[i][j] for j in range(len(mat[0])) for i in range(len(mat))]
```

---

### Problem 48: Rotate Matrix
**Problem Statement:**
Rotate an `n x n` matrix 90 degrees clockwise in-place.

**Solution:**
```python
def rotate(matrix):
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

---

### Problem 49: Transpose
**Problem Statement:**
Given a matrix, return its transpose.

**Solution:**
```python
def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    res = [[0]*rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            res[c][r] = matrix[r][c]
    return res
```

---

### Problem 50: Spiral II
**Problem Statement:**
Given a positive integer `n`, generate an `n x n` matrix filled with elements from 1 to `n^2` in spiral order.

**Solution:**
```python
def generateMatrix(n):
    res = [[0]*n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    while num <= n*n:
        for i in range(left, right + 1):
            res[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            res[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            res[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            res[i][left] = num
            num += 1
        left += 1
    return res
```

## 🔥 SET 6 — Matrix Logic / Advanced (10 Problems)

### Problem 51: Toeplitz Matrix
**Problem Statement:**
Given an `m x n` matrix, return `True` if the matrix is Toeplitz. A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

**Solution:**
```python
def isToeplitzMatrix(matrix):
    for r in range(len(matrix) - 1):
        for c in range(len(matrix[0]) - 1):
            if matrix[r][c] != matrix[r+1][c+1]:
                return False
    return True
```

---

### Problem 52: Exit Point
**Problem Statement:**
Given a binary matrix, you start at (0,0) moving Right. When you hit a 1, you turn 90 degrees clockwise and change that 1 to 0. Find the exit point from the matrix.

**Solution:**
```python
def findExitPoint(mat):
    rows, cols = len(mat), len(mat[0])
    r, c = 0, 0
    dir = 0 # 0:R, 1:D, 2:L, 3:U
    
    while True:
        if mat[r][c] == 1:
            dir = (dir + 1) % 4
            mat[r][c] = 0
        
        # Save last valid position
        prev_r, prev_c = r, c
        
        if dir == 0: c += 1
        elif dir == 1: r += 1
        elif dir == 2: c -= 1
        elif dir == 3: r -= 1
        
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return (prev_r, prev_c)
```

---

### Problem 53: Search Sorted Matrix
**Problem Statement:**
Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:
1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the previous row.

**Solution:**
```python
def searchMatrix(matrix, target):
    if not matrix: return False
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    
    while low <= high:
        mid = (low + high) // 2
        # Map mid to matrix coordinates
        val = matrix[mid // cols][mid % cols]
        if val == target: return True
        elif val < target: low = mid + 1
        else: high = mid - 1
    return False
```

---

### Problem 54: Set Matrix Zeroes
**Problem Statement:**
Given an `m x n` integer matrix `matrix`, if an element is 0, set its entire row and column to 0's. Do it in-place.

**Solution:**
```python
def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                if i == 0: first_row_zero = True
                if j == 0: first_col_zero = True
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    if first_row_zero:
        for j in range(cols): matrix[0][j] = 0
    if first_col_zero:
        for i in range(rows): matrix[i][0] = 0
```

---

### Problem 55: Game of Life
**Problem Statement:**
Implement Conway's Game of Life rules in-place on a grid.
- Live with < 2 neighbors dies.
- Live with 2 or 3 neighbors lives.
- Live with > 3 neighbors dies.
- Dead with 3 neighbors becomes live.

**Solution:**
```python
def gameOfLife(board):
    rows, cols = len(board), len(board[0])
    # Codes: 0->0: 0, 1->1: 1, 1->0: 2, 0->1: 3
    for r in range(rows):
        for c in range(cols):
            neighbors = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if (i == r and j == c) or i < 0 or i >= rows or j < 0 or j >= cols:
                        continue
                    if board[i][j] in [1, 2]: neighbors += 1
            
            if board[r][c] == 1:
                if neighbors < 2 or neighbors > 3: board[r][c] = 2
            else:
                if neighbors == 3: board[r][c] = 3
                
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 2: board[r][c] = 0
            elif board[r][c] == 3: board[r][c] = 1
```

---

### Problem 56: Flood Fill
**Problem Statement:**
An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. You should perform a flood fill on the image starting from the pixel `image[sr][sc]`.

**Solution:**
```python
def floodFill(image, sr, sc, color):
    start_color = image[sr][sc]
    if start_color == color: return image
    
    rows, cols = len(image), len(image[0])
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
            return
        image[r][c] = color
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
        
    dfs(sr, sc)
    return image
```

---

### Problem 57: Number of Islands
**Problem Statement:**
Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

**Solution:**
```python
def numIslands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0' # Mark visited
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count
```

---

### Problem 58: Rotting Oranges
**Problem Statement:**
You are given an `m x n` grid where each cell can have one of three values:
- 0: empty
- 1: fresh orange
- 2: rotten orange
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return min time for all oranges to rot.

**Solution:**
```python
from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2: queue.append((r, c))
            elif grid[r][c] == 1: fresh += 1
            
    minutes = 0
    while queue and fresh > 0:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
    return minutes if fresh == 0 else -1
```

---

### Problem 59: Matrix Distance
**Problem Statement:**
Given an `m x n` binary matrix `mat`, return the distance of the nearest 0 for each cell.

**Solution:**
```python
def updateMatrix(mat):
    rows, cols = len(mat), len(mat[0])
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0: queue.append((r, c))
            else: mat[r][c] = float('inf')
            
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                mat[nr][nc] = mat[r][c] + 1
                queue.append((nr, nc))
    return mat
```

---

### Problem 60: Shortest Path in Grid
**Problem Statement:**
Given an `m x n` grid where each cell is either 0 (path) or 1 (obstacle), and an integer `k` (max obstacles you can remove), find the shortest path from (0,0) to (m-1, n-1).

**Solution:**
```python
def shortestPath(grid, k):
    rows, cols = len(grid), len(grid[0])
    target = (rows - 1, cols - 1)
    if k >= rows + cols - 2: return rows + cols - 2
    
    queue = deque([(0, 0, k, 0)]) # r, c, k, dist
    visited = set([(0, 0, k)])
    
    while queue:
        r, c, k_rem, d = queue.popleft()
        if (r, c) == target: return d
        
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_k = k_rem - grid[nr][nc]
                if new_k >= 0 and (nr, nc, new_k) not in visited:
                    visited.add((nr, nc, new_k))
                    queue.append((nr, nc, new_k, d + 1))
    return -1
```

## 🔥 SET 7 — Matrix Patterns / Special Shapes (10 Problems)

### Problem 61: Hourglass Sum
**Problem Statement:**
Given a 6x6 2D array, an hourglass is a subset of values with indices falling in this pattern:
```
a b c
  d
e f g
```
Find the maximum hourglass sum.

**Solution:**
```python
def maxHourglassSum(grid):
    max_sum = -float('inf')
    for i in range(4):
        for j in range(4):
            current_sum = (grid[i][j] + grid[i][j+1] + grid[i][j+2] +
                           grid[i+1][j+1] +
                           grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2])
            max_sum = max(max_sum, current_sum)
    return max_sum
```

---

### Problem 62: Max Rectangle
**Problem Statement:**
Given a binary matrix, find the maximum area of a rectangle containing only 1s.

**Solution (Using Largest Rectangle in Histogram):**
```python
def largestRectangleArea(heights):
    stack = [-1]
    max_area = 0
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)
    while stack[-1] != -1:
        max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
    return max_area

def maximalRectangle(matrix):
    if not matrix: return 0
    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0
    for row in matrix:
        for i in range(cols):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        max_area = max(max_area, largestRectangleArea(heights))
    return max_area
```

---

### Problem 63: Largest Square of 1s
**Problem Statement:**
Given an `m x n` binary matrix filled with 0s and 1s, find the largest square containing only 1s and return its area.

**Solution (DP):**
```python
def maximalSquare(matrix):
    if not matrix: return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0]*(cols + 1) for _ in range(rows + 1)]
    max_side = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side * max_side
```

---

### Problem 64: Count Submatrices Sum
**Problem Statement:**
Given a matrix and a target, count the number of non-empty submatrices that sum to target.

**Solution:**
```python
def numSubmatrixSumTarget(matrix, target):
    r, c = len(matrix), len(matrix[0])
    # Prefix sums for rows
    for row in matrix:
        for i in range(1, c):
            row[i] += row[i-1]
            
    count = 0
    for i in range(c):
        for j in range(i, c):
            # Sums of subarrays between col i and j
            sums = {0: 1}
            cur = 0
            for k in range(r):
                cur += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                if cur - target in sums:
                    count += sums[cur - target]
                sums[cur] = sums.get(cur, 0) + 1
    return count
```

---

### Problem 65: Max Sum Submatrix
**Problem Statement:**
Given a 2D array, find the maximum sum submatrix (Kadane's 2D).

**Solution:**
```python
def maxSumSubmatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_sum = -float('inf')
    
    for i in range(cols):
        temp = [0] * rows
        for j in range(i, cols):
            for r in range(rows):
                temp[r] += matrix[r][j]
            
            # Apply Kadane's on temp
            current_max = 0
            kadane_max = -float('inf')
            for val in temp:
                current_max += val
                kadane_max = max(kadane_max, current_max)
                if current_max < 0: current_max = 0
            max_sum = max(max_sum, kadane_max)
            
    return max_sum
```

---

### Problem 66: Binary Matrix Flip
**Problem Statement:**
Given a binary matrix, you can flip any row or any column. Find the maximum number of 1s you can get. (Or a variation: Minimum flips to make all elements same).

**Solution (Example variation):**
```python
def maxOnesAfterFlips(matrix):
    # Logic: Always make the first column all 1s by flipping rows.
    # Then for each other column, flip if it has more 0s than 1s.
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        if matrix[i][0] == 0:
            # Flip row
            for j in range(cols):
                matrix[i][j] = 1 - matrix[i][j]
                
    for j in range(1, cols):
        ones = sum(matrix[i][j] for i in range(rows))
        if ones < rows / 2:
            # Flip column
            for i in range(rows):
                matrix[i][j] = 1 - matrix[i][j]
                
    return sum(sum(row) for row in matrix)
```

---

### Problem 67: Island Perimeter
**Problem Statement:**
You are given `grid`, a 2D array representing a map where 1 represents land and 0 represents water. Find the perimeter of the island.

**Solution:**
```python
def islandPerimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r-1][c] == 1: perimeter -= 2
                if c > 0 and grid[r][c-1] == 1: perimeter -= 2
    return perimeter
```

---

### Problem 68: Island Variations
**Problem Statement:**
Count islands with specific properties (e.g., specific shape, size, or those surrounded by water but not touching edges).

**Solution (Closed Islands Example):**
```python
def countClosedIslands(grid):
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols: return False
        if grid[r][c] == 1: return True
        grid[r][c] = 1 # Mark visited
        res = True
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            res &= dfs(r + dr, c + dc)
        return res
        
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                if dfs(r, c): count += 1
    return count
```

---

### Problem 69: Rectangle Overlap
**Problem Statement:**
Given two rectangles, find if they overlap.

**Solution:**
```python
def isRectangleOverlap(rec1, rec2):
    # rec = [x1, y1, x2, y2]
    # Check if one rectangle is to the left, right, top, or bottom of the other
    return not (rec1[2] <= rec2[0] or # left
                rec1[0] >= rec2[2] or # right
                rec1[3] <= rec2[1] or # bottom
                rec1[1] >= rec2[3])   # top
```

---

### Problem 70: Max Area of Island
**Problem Statement:**
Find the maximum area of an island in a binary grid.

**Solution:**
```python
def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
    return max_area
```

## 🔥 SET 8 — Pascal + Combinatorics (10 Problems)

### Problem 71: Pascal Triangle
**Problem Statement:**
Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

**Solution:**
```python
def generatePascal(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
```

---

### Problem 72: Pascal II (Single Row Optimization)
**Problem Statement:**
Given an integer `rowIndex`, return the `rowIndex`-th row of Pascal's triangle. Optimize for O(k) space.

**Solution:**
```python
def getRow(rowIndex):
    row = [1] * (rowIndex + 1)
    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            row[j] += row[j-1]
    return row
```

---

### Problem 73: Nth Row (Direct Computation)
**Problem Statement:**
Compute the Nth row of Pascal's triangle using the formula `nCr = nCr-1 * (n-r+1)/r`.

**Solution:**
```python
def getNthRow(n):
    res = [1]
    prev = 1
    for r in range(1, n + 1):
        curr = prev * (n - r + 1) // r
        res.append(curr)
        prev = curr
    return res
```

---

### Problem 74: Binomial Coefficient
**Problem Statement:**
Compute `nCr` (n choose r) efficiently.

**Solution:**
```python
def nCr(n, r):
    if r > n: return 0
    if r == 0 or r == n: return 1
    if r > n // 2: r = n - r
    
    num = 1
    for i in range(r):
        num = num * (n - i) // (i + 1)
    return num
```

---

### Problem 75: Combinations
**Problem Statement:**
Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

**Solution:**
```python
def combine(n, k):
    res = []
    def backtrack(start, curr):
        if len(curr) == k:
            res.append(curr[:])
            return
        for i in range(start, n + 1):
            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(1, [])
    return res
```

---

### Problem 76: Subsets
**Problem Statement:**
Given an integer array `nums` of unique elements, return all possible subsets (the power set).

**Solution:**
```python
def subsets(nums):
    res = [[]]
    for num in nums:
        res += [curr + [num] for curr in res]
    return res
```

---

### Problem 77: Permutations
**Problem Statement:**
Given an array `nums` of distinct integers, return all the possible permutations.

**Solution:**
```python
def permute(nums):
    res = []
    def backtrack(curr):
        if len(curr) == len(nums):
            res.append(curr[:])
            return
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    backtrack([])
    return res
```

---

### Problem 78: Combination Sum
**Problem Statement:**
Given an array of distinct integers `candidates` and a `target` integer, return a list of all unique combinations where the chosen numbers sum to `target`. You may use the same number an unlimited number of times.

**Solution:**
```python
def combinationSum(candidates, target):
    res = []
    def backtrack(remain, curr, start):
        if remain == 0:
            res.append(curr[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= remain:
                curr.append(candidates[i])
                backtrack(remain - candidates[i], curr, i)
                curr.pop()
    backtrack(target, [], 0)
    return res
```

---

### Problem 79: Subsets with Duplicates
**Problem Statement:**
Given an integer array `nums` that may contain duplicates, return all possible subsets. The solution set must not contain duplicate subsets.

**Solution:**
```python
def subsetsWithDup(nums):
    nums.sort()
    res = [[]]
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            # Only add to subsets generated in the previous step
            new_subsets = [curr + [nums[i]] for curr in prev_new]
        else:
            new_subsets = [curr + [nums[i]] for curr in res]
        prev_new = new_subsets
        res += new_subsets
    return res
```

---

### Problem 80: Permutations II
**Problem Statement:**
Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in any order.

**Solution:**
```python
from collections import Counter

def permuteUnique(nums):
    res = []
    def backtrack(curr, counter):
        if len(curr) == len(nums):
            res.append(curr[:])
            return
        for num in counter:
            if counter[num] > 0:
                curr.append(num)
                counter[num] -= 1
                backtrack(curr, counter)
                counter[num] += 1
                curr.pop()
    backtrack([], Counter(nums))
    return res
```

## 🔥 SET 9 — String Basics + Medium (10 Problems)

### Problem 81: Largest Odd Substring
**Problem Statement:**
Given a string `num` representing a large integer, return the largest-valued odd integer (as a string) that is a non-empty substring of `num`, or an empty string `""` if no odd integer exists.

**Solution:**
```python
def largestOddNumber(num):
    # Iterate from right to left to find the first odd digit
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""
```

---

### Problem 82: Reverse Prefix
**Problem Statement:**
Given a 0-indexed string `word` and a character `ch`, reverse the segment of `word` that starts at index 0 and ends at the index of the first occurrence of `ch` (inclusive).

**Solution:**
```python
def reversePrefix(word, ch):
    idx = word.find(ch)
    if idx == -1: return word
    return word[:idx+1][::-1] + word[idx+1:]
```

---

### Problem 83: Reverse String
**Problem Statement:**
Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

**Solution:**
```python
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

---

### Problem 84: Palindrome Check
**Problem Statement:**
Check if a string is a palindrome (reads same forward and backward).

**Solution:**
```python
def isPalindrome(s):
    return s == s[::-1]
```

---

### Problem 85: Valid Palindrome (Ignore Symbols)
**Problem Statement:**
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

**Solution:**
```python
def isPalindrome(s):
    filtered = "".join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]
```

---

### Problem 86: First Unique Char
**Problem Statement:**
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

**Solution:**
```python
from collections import Counter

def firstUniqChar(s):
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
```

---

### Problem 87: Longest Common Prefix
**Problem Statement:**
Write a function to find the longest common prefix string amongst an array of strings.

**Solution:**
```python
def longestCommonPrefix(strs):
    if not strs: return ""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest
```

---

### Problem 88: String Compression
**Problem Statement:**
Given an array of characters `chars`, compress it using the following algorithm:
Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`:
If the group's length is 1, append the character to `s`.
Otherwise, append the character followed by the group's length.

**Solution:**
```python
def compress(chars):
    write = 0
    read = 0
    while read < len(chars):
        char = chars[read]
        count = 0
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        chars[write] = char
        write += 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    return write
```

---

### Problem 89: Group Anagrams
**Problem Statement:**
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

**Solution:**
```python
def groupAnagrams(strs):
    ans = {}
    for s in strs:
        key = "".join(sorted(s))
        if key not in ans: ans[key] = []
        ans[key].append(s)
    return list(ans.values())
```

---

### Problem 90: Check Rotation
**Problem Statement:**
Given two strings `s` and `goal`, return `True` if and only if `s` can become `goal` after some number of shifts on `s`.

**Solution:**
```python
def rotateString(s, goal):
    return len(s) == len(goal) and goal in (s + s)
```

## 🔥 SET 10 — String Frequency / Hashing (10 Problems)

### Problem 91: Balanced String
**Problem Statement:**
A string is balanced if all characters in the string have the same frequency. Given a string `s`, return `True` if `s` is balanced, otherwise return `False`.

**Solution:**
```python
from collections import Counter

def isBalanced(s):
    counts = Counter(s)
    freqs = set(counts.values())
    return len(freqs) == 1
```

---

### Problem 92: Valid Anagram
**Problem Statement:**
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

**Solution:**
```python
def isAnagram(s, t):
    return Counter(s) == Counter(t)
```

---

### Problem 93: Isomorphic Strings
**Problem Statement:**
Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

**Solution:**
```python
def isIsomorphic(s, t):
    if len(s) != len(t): return False
    mapping_s = {}
    mapping_t = {}
    for char_s, char_t in zip(s, t):
        if char_s in mapping_s:
            if mapping_s[char_s] != char_t: return False
        else:
            mapping_s[char_s] = char_t
            
        if char_t in mapping_t:
            if mapping_t[char_t] != char_s: return False
        else:
            mapping_t[char_t] = char_s
    return True
```

---

### Problem 94: Word Pattern
**Problem Statement:**
Given a `pattern` and a string `s`, find if `s` follows the same pattern.

**Solution:**
```python
def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words): return False
    
    p_to_w = {}
    w_to_p = {}
    
    for p, w in zip(pattern, words):
        if p in p_to_w:
            if p_to_w[p] != w: return False
        else:
            p_to_w[p] = w
            
        if w in w_to_p:
            if w_to_p[w] != p: return False
        else:
            w_to_p[w] = p
    return True
```

---

### Problem 95: Find All Anagrams
**Problem Statement:**
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`.

**Solution:**
```python
def findAnagrams(s, p):
    n, m = len(s), len(p)
    if m > n: return []
    
    p_count = Counter(p)
    s_count = Counter(s[:m])
    res = []
    
    if p_count == s_count: res.append(0)
    
    for i in range(m, n):
        s_count[s[i]] += 1
        s_count[s[i-m]] -= 1
        if s_count[s[i-m]] == 0: del s_count[s[i-m]]
        if s_count == p_count: res.append(i - m + 1)
        
    return res
```

---

### Problem 96: Frequency Sort
**Problem Statement:**
Given a string `s`, sort it in decreasing order based on the frequency of the characters.

**Solution:**
```python
def frequencySort(s):
    counts = Counter(s)
    # Sort keys by value in descending order
    sorted_chars = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    res = []
    for char, freq in sorted_chars:
        res.append(char * freq)
    return "".join(res)
```

---

### Problem 97: Top K Frequent
**Problem Statement:**
Given a non-empty array of integers, return the `k` most frequent elements.

**Solution:**
```python
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    # Use a min-heap to keep track of k most frequent
    return heapq.nlargest(k, count.keys(), key=count.get)
```

---

### Problem 98: Reorganize String
**Problem Statement:**
Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

**Solution:**
```python
def reorganizeString(s):
    res = []
    counts = Counter(s)
    # Max heap to always pick the most frequent char
    max_heap = [(-cnt, char) for char, cnt in counts.items()]
    heapq.heapify(max_heap)
    
    prev_cnt, prev_char = 0, ""
    while max_heap:
        cnt, char = heapq.heappop(max_heap)
        res.append(char)
        
        # Add the previous char back to heap if it still has count
        if prev_cnt < 0:
            heapq.heappush(max_heap, (prev_cnt, prev_char))
            
        cnt += 1 # decrease absolute count
        prev_cnt, prev_char = cnt, char
        
    res_str = "".join(res)
    return res_str if len(res_str) == len(s) else ""
```

---

### Problem 99: Count Substrings (Variations)
**Problem Statement:**
Count substrings with specific properties (e.g., all unique chars, at least k repeats).

**Solution (Example: Count substrings with unique characters):**
```python
def countUniqueSubstrings(s):
    # Total substrings = n * (n + 1) / 2
    # This example focuses on substrings where ALL chars are distinct
    n = len(s)
    count = 0
    l = 0
    seen = set()
    for r in range(n):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        # All substrings ending at r and starting between l and r are unique
        count += (r - l + 1)
    return count
```

---

### Problem 100: Longest Palindrome Length
**Problem Statement:**
Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

**Solution:**
```python
def longestPalindrome(s):
    counts = Counter(s)
    length = 0
    odd_found = False
    for cnt in counts.values():
        if cnt % 2 == 0:
            length += cnt
        else:
            length += cnt - 1
            odd_found = True
    return length + 1 if odd_found else length
```

## 🔥 SET 11 — Binary String / Greedy (10 Problems)

### Problem 101: Conveyor Belt (String Shift)
**Problem Statement:**
Given a binary string, you can perform cyclic shifts. Count how many shifts result in a valid property (e.g., starts with '1', or balanced).

**Solution (Example: Count shifts starting with '1'):**
```python
def countShiftsStartingWithOne(s):
    count = 0
    n = len(s)
    # Check all cyclic shifts
    for i in range(n):
        shifted = s[i:] + s[:i]
        if shifted[0] == '1':
            count += 1
    return count
```

---

### Problem 102: Balanced Binary Substrings
**Problem Statement:**
Given a binary string `s`, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

**Solution:**
```python
def countBinarySubstrings(s):
    groups = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)
    
    res = 0
    for i in range(1, len(groups)):
        res += min(groups[i], groups[i-1])
    return res
```

---

### Problem 103: Count Binary Substrings (General)
**Problem Statement:**
Count total substrings with equal number of 0s and 1s.

**Solution (Hashing approach):**
```python
def countEqualZeroOne(s):
    # Convert 0 to -1
    count = 0
    cur_sum = 0
    sum_map = {0: 1}
    for char in s:
        cur_sum += 1 if char == '1' else -1
        if cur_sum in sum_map:
            count += sum_map[cur_sum]
        sum_map[cur_sum] = sum_map.get(cur_sum, 0) + 1
    return count
```

---

### Problem 104: Max Consecutive Ones
**Problem Statement:**
Given a binary array `nums`, return the maximum number of consecutive 1's in the array.

**Solution:**
```python
def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count
```

---

### Problem 105: Flip Bits
**Problem Statement:**
Given a binary string, you can flip at most one '0' to '1'. Find the maximum consecutive '1's you can get.

**Solution:**
```python
def maxConsecutiveOnesWithFlip(s):
    l = 0
    zeros = 0
    max_len = 0
    for r in range(len(s)):
        if s[r] == '0': zeros += 1
        while zeros > 1:
            if s[l] == '0': zeros -= 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len
```

---

### Problem 106: Min Flips Alternating
**Problem Statement:**
Given a binary string `s`, you can flip '0' to '1' or vice versa. Return the minimum number of flips to make `s` alternating (e.g., "010101" or "101010").

**Solution:**
```python
def minFlips(s):
    def check(target):
        flips = 0
        for i in range(len(s)):
            if s[i] != target[i % 2]:
                flips += 1
        return flips
        
    return min(check("01"), check("10"))
```

---

### Problem 107: Split Binary String
**Problem Statement:**
Split a binary string into max number of balanced substrings (equal 0s and 1s).

**Solution:**
```python
def balancedStringSplit(s):
    res = 0
    balance = 0
    for char in s:
        if char == 'L': balance += 1
        else: balance -= 1
        if balance == 0:
            res += 1
    return res
```

---

### Problem 108: Remove K Digits
**Problem Statement:**
Given string `num` representing a non-negative integer, and an integer `k`, return the smallest possible integer after removing `k` digits from `num`.

**Solution:**
```python
def removeKdigits(num, k):
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If k > 0, remove from end
    final_stack = stack[:-k] if k > 0 else stack
    
    # Remove leading zeros
    return "".join(final_stack).lstrip('0') or "0"
```

---

### Problem 109: Binary Addition
**Problem Statement:**
Given two binary strings `a` and `b`, return their sum as a binary string.

**Solution:**
```python
def addBinary(a, b):
    res = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        v1 = int(a[i]) if i >= 0 else 0
        v2 = int(b[j]) if j >= 0 else 0
        total = v1 + v2 + carry
        res.append(str(total % 2))
        carry = total // 2
        i -= 1
        j -= 1
        
    return "".join(res[::-1])
```

---

### Problem 110: Longest Valid Parentheses
**Problem Statement:**
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

**Solution:**
```python
def longestValidParentheses(s):
    stack = [-1]
    max_len = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len
```

## 🔥 SET 12 — String Hard / Construction (10 Problems)

### Problem 111: Multiply Strings
**Problem Statement:**
Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Solution:**
```python
def multiply(num1, num2):
    if num1 == "0" or num2 == "0": return "0"
    res = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            total = mul + res[p2]
            res[p2] = total % 10
            res[p1] += total // 10
            
    # Convert res to string, skipping leading zeros
    start = 0
    while start < len(res) and res[start] == 0:
        start += 1
    return "".join(map(str, res[start:]))
```

---

### Problem 112: Add Strings
**Problem Statement:**
Given two non-negative integers, `num1` and `num2` represented as string, return the sum of `num1` and `num2` as a string.

**Solution:**
```python
def addStrings(num1, num2):
    res = []
    carry = 0
    i, j = len(num1) - 1, len(num2) - 1
    while i >= 0 or j >= 0 or carry:
        v1 = int(num1[i]) if i >= 0 else 0
        v2 = int(num2[j]) if j >= 0 else 0
        total = v1 + v2 + carry
        res.append(str(total % 10))
        carry = total // 10
        i -= 1
        j -= 1
    return "".join(res[::-1])
```

---

### Problem 113: String to Integer (atoi)
**Problem Statement:**
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

**Solution:**
```python
def myAtoi(s):
    s = s.strip()
    if not s: return 0
    sign = 1
    i = 0
    if s[0] == '-':
        sign = -1
        i += 1
    elif s[0] == '+':
        i += 1
        
    res = 0
    while i < len(s) and s[i].isdigit():
        res = res * 10 + int(s[i])
        i += 1
        
    res *= sign
    # Clamp to 32-bit signed integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    return max(INT_MIN, min(INT_MAX, res))
```

---

### Problem 114: Decode String
**Problem Statement:**
Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times.

**Solution:**
```python
def decodeString(s):
    stack = []
    cur_str = ""
    cur_num = 0
    for char in s:
        if char.isdigit():
            cur_num = cur_num * 10 + int(char)
        elif char == '[':
            stack.append((cur_str, cur_num))
            cur_str, cur_num = "", 0
        elif char == ']':
            prev_str, num = stack.pop()
            cur_str = prev_str + num * cur_str
        else:
            cur_str += char
    return cur_str
```

---

### Problem 115: Encode and Decode Strings
**Problem Statement:**
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

**Solution:**
```python
def encode(strs):
    # Format: length + # + string
    return "".join(f"{len(s)}#{s}" for s in strs)

def decode(s):
    res = []
    i = 0
    while i < len(s):
        j = s.find('#', i)
        length = int(s[i:j])
        res.append(s[j+1 : j+1+length])
        i = j + 1 + length
    return res
```

---

### Problem 116: Word Break
**Problem Statement:**
Given a string `s` and a dictionary of strings `wordDict`, return `True` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Solution:**
```python
def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    word_set = set(wordDict)
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]
```

---

### Problem 117: Interleaving String
**Problem Statement:**
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.

**Solution:**
```python
def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3): return False
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i > 0:
                dp[i][j] |= dp[i-1][j] and s1[i-1] == s3[i+j-1]
            if j > 0:
                dp[i][j] |= dp[i][j-1] and s2[j-1] == s3[i+j-1]
    return dp[len(s1)][len(s2)]
```

---

### Problem 118: Edit Distance
**Problem Statement:**
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. Operations: Insert, Delete, Replace.

**Solution:**
```python
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
```

---

### Problem 119: Substring with K Repeats
**Problem Statement:**
Given a string `s` and an integer `k`, return the length of the longest substring of `s` such that the frequency of each character in this substring is greater than or equal to `k`.

**Solution:**
```python
def longestSubstring(s, k):
    if len(s) < k: return 0
    for char in set(s):
        if s.count(char) < k:
            return max(longestSubstring(sub, k) for sub in s.split(char))
    return len(s)
```

---

### Problem 120: Min Insertions Palindrome
**Problem Statement:**
Given a string `s`, return the minimum number of insertions needed to make `s` a palindrome.

**Solution:**
```python
def minInsertions(s):
    n = len(s)
    # Result = n - length of Longest Palindromic Subsequence
    rev_s = s[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i-1] == rev_s[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return n - dp[n][n]
```

## 🔥 SET 13 — Special String Logic (10 Problems)

### Problem 121: Mirror Note
**Problem Statement:**
A "Mirror Note" is a string that reads the same when reflected (palindrome) but also follows specific character-to-character mapping (like 'b' maps to 'd', 'p' to 'q', etc.). For simplicity, check if a string is a standard palindrome.

**Solution:**
```python
def isMirrorNote(s):
    # Standard Palindrome check
    return s == s[::-1]
```

---

### Problem 122: Magical Swap
**Problem Statement:**
Two strings are "magically equal" if one swap in either string can make them equal.

**Solution:**
```python
def areMagicallyEqual(s1, s2):
    if s1 == s2: return False # At least one swap is required
    if len(s1) != len(s2): return False
    
    diff = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append(i)
            
    if len(diff) != 2: return False
    i, j = diff
    return s1[i] == s2[j] and s1[j] == s2[i]
```

---

### Problem 123: Buddy Strings
**Problem Statement:**
Given two strings `s` and `goal`, return `True` if you can swap two letters in `s` so the result is equal to `goal`, otherwise, return `False`.

**Solution:**
```python
def buddyStrings(s, goal):
    if len(s) != len(goal): return False
    if s == goal:
        # If strings are equal, we need at least one repeated char to swap
        return len(set(s)) < len(s)
    
    diffs = [(a, b) for a, b in zip(s, goal) if a != b]
    return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
```

---

### Problem 124: Palindrome II
**Problem Statement:**
Given a string `s`, return `True` if the `s` can be palindrome after deleting at most one character from it.

**Solution:**
```python
def validPalindrome(s):
    def is_pal(string, l, r):
        while l < r:
            if string[l] != string[r]: return False
            l += 1
            r -= 1
        return True
        
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return is_pal(s, l + 1, r) or is_pal(s, l, r - 1)
        l += 1
        r -= 1
    return True
```

---

### Problem 125: Backspace Compare
**Problem Statement:**
Given two strings `s` and `t`, return `True` if they are equal when both are typed into empty text editors. `#` means a backspace character.

**Solution:**
```python
def backspaceCompare(s, t):
    def build(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return "".join(stack)
        
    return build(s) == build(t)
```

---

### Problem 126: Subsequence Check
**Problem Statement:**
Given two strings `s` and `t`, return `True` if `s` is a subsequence of `t`, or `False` otherwise.

**Solution:**
```python
def isSubsequence(s, t):
    if not s: return True
    i = 0
    for char in t:
        if char == s[i]:
            i += 1
            if i == len(s): return True
    return False
```

---

### Problem 127: Longest Palindromic Substring
**Problem Statement:**
Given a string `s`, return the longest palindromic substring in `s`.

**Solution:**
```python
def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # Odd length
        tmp = expand(s, i, i)
        if len(tmp) > len(res): res = tmp
        # Even length
        tmp = expand(s, i, i + 1)
        if len(tmp) > len(res): res = tmp
    return res

def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1 : r]
```

---

### Problem 128: Count Palindromic Substrings
**Problem Statement:**
Given a string `s`, return the number of palindromic substrings in it.

**Solution:**
```python
def countSubstrings(s):
    count = 0
    for i in range(len(s)):
        count += expand_count(s, i, i)
        count += expand_count(s, i, i + 1)
    return count

def expand_count(s, l, r):
    cnt = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        cnt += 1
        l -= 1
        r += 1
    return cnt
```

---

### Problem 129: Remove Duplicate Letters
**Problem Statement:**
Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

**Solution:**
```python
def removeDuplicateLetters(s):
    last_occ = {c: i for i, c in enumerate(s)}
    stack = []
    visited = set()
    
    for i, char in enumerate(s):
        if char not in visited:
            while stack and char < stack[-1] and i < last_occ[stack[-1]]:
                visited.remove(stack.pop())
            visited.add(char)
            stack.append(char)
    return "".join(stack)
```

---

### Problem 130: Lexicographically Smallest String
**Problem Statement:**
Given a string `s`, you can perform at most one swap. Return the lexicographically smallest string possible.

**Solution:**
```python
def smallestString(s):
    chars = list(s)
    # Strategy: Find first index where we can swap with a smaller char from the right
    for i in range(len(chars)):
        min_idx = i
        for j in range(len(chars) - 1, i, -1):
            if chars[j] < chars[min_idx]:
                # Find the smallest char, and if there's a tie, the rightmost one
                if min_idx == i or chars[j] < chars[min_idx]:
                    min_idx = j
        
        if min_idx != i:
            chars[i], chars[min_idx] = chars[min_idx], chars[i]
            break
    return "".join(chars)
```

🚀 LEETCODE SET (UNCHANGED)
1, 15, 18, 26, 27, 28, 49, 53, 75, 88,
121, 125, 136, 141, 169, 189, 205, 217, 219, 242,
283, 344, 347, 350, 383, 387, 389, 392, 409, 415,
424, 438, 448, 459, 485, 496, 525, 560, 567, 605,
680, 704, 733, 796, 844, 905, 917, 977, 1002, 1021,
1047, 1071, 1108, 1207, 1252, 1299, 1346, 1351, 1365, 1389