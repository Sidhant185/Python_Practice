---

---

## Problem 1: Isomorphic Strings

**Problem Statement:**
In an ancient library, secret messages are stored on magical scrolls. Each scroll contains a message string written using lowercase English letters.

To unlock a scroll, the librarian is allowed to replace characters in the original message following a fixed rule.

**Task:**
Determine whether the original message `s` can be transformed into the target message `t` by replacing its characters.

- Each character in `s` must always be replaced with the same character in `t`
- The order of characters must be preserved
- No two different characters from `s` may map to the same character in `t`
- A character is allowed to map to itself

Return `true` if transformation is possible, otherwise `false`.

**Input Format:**
- First line: string `s` (original message)
- Second line: string `t` (target message)

**Output Format:**
- Print `true` if the scroll can be unlocked
- Otherwise, print `false`

**Constraints:**
- 1 ≤ |s|, |t| ≤ 2 × 10⁴
- |s| == |t|
- Both strings contain valid ASCII English letters

**Examples:**
```python
# Example 1
s = "egg"
t = "add"
Output: true

# Example 2
s = "badc"
t = "baba"
Output: false
```

**Solution Approach:**
Use two dictionaries to maintain bijection (one-to-one mapping):
- One to map characters from `s` to `t`
- One to ensure no two characters from `s` map to the same character in `t`

---

## Problem 2: Maximum Odd-Even Frequency Difference

**Problem Statement:**
You are given a string `s` consisting only of lowercase English letters.

Define the difference:
```
diff = freq(a1) − freq(a2)
```

Where:
- `a1` is a character whose frequency in `s` is odd
- `a2` is a character whose frequency in `s` is even

Compute and return the maximum possible value of `diff`.

**Input Format:**
- A single string `s`

**Output Format:**
- Return an integer representing the maximum difference

**Constraints:**
- 3 ≤ s.length ≤ 100
- s contains only lowercase English letters (a–z)
- The string contains at least one character with odd frequency
- The string contains at least one character with even frequency

**Examples:**
```python
# Example
s = "aaaaabbc"
Output: 3  # 'a' has freq 5 (odd), 'b' has freq 2 (even), diff = 5 - 2 = 3
```

**Solution Approach:**
Count frequency of each character, find max odd frequency and min even frequency, return their difference.

---

## Problem 3: Latest Possible Time

**Problem Statement:**
You are given a string `time` representing a clock time in the format `hh:mm`.

Some digits in the string may be hidden and are represented by the character '?'.

**Task:**
Replace every hidden digit ('?') with an appropriate numeric digit such that:
- The resulting time is valid (between 00:00 and 23:59)
- The resulting time is the latest possible valid time

**Input Format:**
- A single string `time` in the format `hh:mm`
- Hidden digits are represented using '?'

**Output Format:**
- Return a string representing the latest valid time

**Constraints:**
- `time` is always in the format `hh:mm`
- 00 ≤ hh ≤ 23
- 00 ≤ mm ≤ 59
- Hidden characters may appear at any digit position
- It is guaranteed that at least one valid time can be formed

**Examples:**
```python
# Example 1
time = "2?:?0"
Output: "23:50"

# Example 2
time = "?3:22"
Output: "23:22"
```

**Solution Approach:**
Use greedy replacement starting from the leftmost '?', selecting the largest digit possible while maintaining validity.

---

## Problem 4: The Stubborn Keyboard

**Problem Statement:**
Your friend is typing their name on a keyboard, but there's a catch! Some keys on the keyboard are stubborn and may get long-pressed.

When a key is long-pressed, the corresponding character may appear multiple times consecutively instead of just once.

**Task:**
Determine whether the typed string could have been produced from name by long-pressing some characters (possibly none).

**Rules for Long Pressing:**
- Each character in `name` must appear in order in `typed`
- A character may appear more than once consecutively in `typed`
- No extra or mismatched characters are allowed

**Input Format:**
- A string `name` representing the original name
- A string `typed` representing the typed output

**Output Format:**
- Return `True` if `typed` can be a valid long-pressed version of `name`
- Otherwise, return `False`

**Examples:**
```python
# Example 1
name = "alex"
typed = "aaleex"
Output: True  # 'a' is pressed twice, rest once each

# Example 2
name = "abc"
typed = "abcd"
Output: False  # Extra character 'd'
```

**Solution Approach:**
Use two pointers to traverse both strings, allowing consecutive duplicate characters in `typed` but ensuring all characters from `name` appear in order.

---

## Problem 5: Divide String Into Groups of Size k

**Problem Statement:**
You are given:
- A string `s`
- An integer `k` representing the group size
- A character `fill`

The string must be divided into consecutive groups of size `k` following these rules:
- The first group contains the first `k` characters
- The second group contains the next `k` characters, and so on
- If the final group contains fewer than `k` characters, append the `fill` character until the group reaches size `k`

**Input Format:**
- A string `s`
- An integer `k`
- A character `fill`

**Output Format:**
- Return an array (list) of strings representing the groups

**Constraints:**
- 1 ≤ s.length ≤ 100
- s contains only lowercase English letters
- 1 ≤ k ≤ 100
- fill is a lowercase English letter

**Examples:**
```python
# Example 1
s = "abcdefghi"
k = 3
fill = "x"
Output: ["abc", "def", "ghi"]

# Example 2
s = "abcd"
k = 3
fill = "x"
Output: ["abc", "dxx"]
```

**Solution Approach:**
Iterate through the string in chunks of size `k`, pad the last group if needed.

---

## Problem 6: Linear Search

**Problem Statement:**
A digital inventory system maintains a list of product IDs. Unlike optimized systems, this list is not sorted, which means the system must examine each element sequentially when performing a search.

**Task:**
Find whether the target exists in the list.
- If the target is found, return its index position
- If the target is not found, return -1

**Input Format:**
- An integer array `nums` representing the list of integers (not necessarily sorted)
- An integer `target` representing the value to be searched

**Output Format:**
- Return a single integer:
  - the index of the target if it exists
  - -1 if the target does not exist in the array

**Constraints:**
- 1 ≤ nums.length ≤ 10⁴
- -10⁴ < nums[i], target < 10⁴
- The elements of the array may be unsorted
- If duplicates exist, return the first occurrence of the target

**Examples:**
```python
# Example 1
nums = [5, 8, 1, 3, 9, 6]
target = 3
Output: 3

# Example 2
nums = [4, 7, 2, 11, 19]
target = 5
Output: -1
```

**Solution Approach:**
Simple iteration through array, checking each element.

---

## Problem 7: Binary Search

**Problem Statement:**
A financial analytics system stores transaction IDs in a list that is always maintained in ascending order to allow fast searching.

**Task:**
Determine whether the target exists in the sorted list.
- If the target is found, return its index position
- If the target is not found, return -1

The solution must be efficient and work in logarithmic time.

**Input Format:**
- An integer array `nums` representing the sorted list of integers
- An integer `target` representing the value to be searched

**Output Format:**
- Return a single integer:
  - the index of the target if it exists
  - -1 if the target does not exist in the array

**Constraints:**
- 1 ≤ nums.length ≤ 10⁴
- -10⁴ < nums[i], target < 10⁴
- All integers in the array are unique
- The array is sorted in ascending order
- The solution must run in O(log n) time complexity

**Examples:**
```python
# Example 1
nums = [1, 2, 4, 5, 6, 8, 9]
target = 4
Output: 2

# Example 2
nums = [1, 2, 4, 5, 6, 8, 9]
target = 3
Output: -1
```

**Solution Approach:**
Classic binary search with left and right pointers.

---

## Problem 8: First and Last Index of an Element

**Problem Statement:**
Given a sorted array `nums` in non-decreasing order, find the starting and ending position of a given target value.

If the target is not found in the array, return `[-1, -1]`.

You must write an algorithm with O(log n) runtime complexity.

**Input Format:**
- An integer `n` representing the size of the list
- A sorted list `nums` of `n` integers
- An integer `target` to search for

**Output Format:**
- Return a list of two integers `[first_index, last_index]` representing the starting and ending position of the target value
- If the target is not found, return `[-1, -1]`

**Constraints:**
- 0 ≤ n ≤ 10⁵
- −10⁹ ≤ nums[i] ≤ 10⁹
- −10⁹ ≤ target ≤ 10⁹
- The array is sorted in non-decreasing order

**Examples:**
```python
# Example
n = 6
nums = [5, 7, 7, 8, 8, 10]
target = 8
Output: [3, 4]
# Explanation: The target 8 appears at indices 3 and 4.
```

**Solution Approach:**
Use two binary searches - one to find the leftmost occurrence and one for the rightmost.

---

## Problem 9: Number of Occurrence

**Problem Statement:**
Imagine you're a librarian with a long shelf of books arranged in sorted order by their ID numbers. A visitor asks: "How many books with ID = target are here?"

**Task:**
Quickly count how many times the target appears in the sorted list.

**Rules:**
- The shelf (array) is sorted in non-decreasing order
- You must answer efficiently in O(log n) time using binary search with O(1) extra space

**Input Format:**
- First line: `arr[]` → space-separated sorted integers
- Second line: `target` → the integer whose occurrences we need to count

**Output Format:**
- A single integer representing the number of times target occurs in `arr[]`

**Constraints:**
- 1 ≤ arr.size() ≤ 10⁶
- 1 ≤ arr[i] ≤ 10⁶
- 1 ≤ target ≤ 10⁶

**Examples:**
```python
# Example
arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
Output: 4
```

**Solution Approach:**
Find first and last occurrence using binary search, return the difference.

---

## Problem 10: Find Index of Extra Element in Sorted Arrays

**Problem Statement:**
You are given two sorted arrays `arr1` and `arr2` of distinct elements in non-decreasing order. The array `arr1` contains all elements of `arr2` with exactly one extra element inserted somewhere in between.

**Task:**
Find and return the 0-based index of this extra element in `arr1`.

**Input Format:**
- First line: integer `n` representing size of `arr1`
- Second line: `n` space-separated integers for `arr1`
- Third line: integer `m` representing size of `arr2` (where m = n - 1)
- Fourth line: `m` space-separated integers for `arr2`

**Output Format:**
- Return an integer representing the 0-based index of the extra element in `arr1`

**Constraints:**
- 2 ≤ arr1.length ≤ 10⁴
- 1 ≤ arr2.length ≤ 10⁴
- arr1.length = arr2.length + 1
- −10⁹ ≤ arr1[i], arr2[i] ≤ 10⁹
- Both arrays are sorted in non-decreasing order
- All elements in each array are distinct

**Examples:**
```python
# Example
arr1 = [2, 4, 6, 8, 9, 10, 12]
arr2 = [2, 4, 6, 8, 10, 12]
Output: 4
# Explanation: Element 9 at index 4 is extra in arr1.
```

**Solution Approach:**
Use binary search to compare elements at corresponding positions.

---

## Problem 11: Floor in a Sorted Array

**Problem Statement:**
Imagine you're climbing a staircase of numbers arranged in sorted order. You're standing at a target step `x`. Your task is to find the highest step (largest number) that is less than or equal to `x`.

This step is called the floor of `x`. If no such step exists, return -1.

If there are multiple identical steps equal to the floor, return the last index (0-based).

**Input Format:**
- First line: `arr[]` → space-separated sorted integers
- Second line: `x` → the target integer

**Output Format:**
- A single integer representing the index (0-based) of the floor of `x`
- If no floor exists, output -1

**Constraints:**
- 1 ≤ arr.size() ≤ 10⁶
- 1 ≤ arr[i] ≤ 10⁶
- 0 ≤ x ≤ arr[n-1]

**Examples:**
```python
# Example
arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
Output: 1  # arr[1] = 2 is the largest number <= 5
```

**Solution Approach:**
Binary search for the largest element ≤ x.

---

## Problem 12: Ceil in a Sorted Array

**Problem Statement:**
Imagine you're climbing a staircase of numbers arranged in sorted order. You're standing at a target step `x`. Your task is to find the lowest step (smallest number) that is greater than or equal to `x`.

This step is called the ceil of `x`. If no such step exists, return -1.

**Input Format:**
- First line: `arr[]` → space-separated sorted integers
- Second line: `x` → the target integer

**Output Format:**
- A single integer representing the index (0-based) of the ceil of `x`
- If no ceil exists, output -1

**Constraints:**
- 1 ≤ arr.size() ≤ 10⁶
- 1 ≤ arr[i] ≤ 10⁶
- 0 ≤ x ≤ arr[n-1]

**Examples:**
```python
# Example 1
arr = [1, 2, 8, 10, 11, 12, 19]
x = 5
Output: 2  # arr[2] = 8 is the smallest number >= 5

# Example 2
arr = [1, 2, 8, 10, 11, 12, 19]
x = 20
Output: -1  # No element >= 20
```

**Solution Approach:**
Binary search for the smallest element ≥ x.

---

## Problem 13: Next Greater Letter

**Problem Statement:**
Imagine you are given a circular list of lowercase English letters arranged in sorted order. Your task is to find the next letter in alphabetical order that comes after a given target letter.

**Rules:**
- The list is considered circular
- If the target letter is greater than or equal to all letters in the list, wrap around and return the first letter
- Determine the smallest letter in the list that is strictly greater than the given target letter

**Input:**
- A sorted list of lowercase English letters `letters`
- A lowercase English letter `target`

**Output:**
- Return a single lowercase English letter
- The returned letter must be the smallest character in `letters` that is strictly greater than `target`
- If no such letter exists, return the first element of the list

**Constraints:**
- 2 ≤ letters.length ≤ 10⁴
- letters[i] is a lowercase English letter
- The array `letters` is sorted in non-decreasing order
- The array contains at least two distinct characters
- `target` is a lowercase English letter

**Examples:**
```python
# Example 1
letters = ['c', 'f', 'j']
target = 'a'
Output: 'c'

# Example 2
letters = ['c', 'f', 'j']
target = 'c'
Output: 'f'

# Example 3
letters = ['c', 'f', 'j']
target = 'k'
Output: 'c'  # Wrap around
```

**Solution Approach:**
Binary search to find the smallest letter > target, or return first element if none found.

---

## Problem 14: Search in an Almost Sorted Array

**Problem Statement:**
Imagine you're a detective searching through a shuffled archive. The archive was originally sorted, but during storage, some files slipped slightly out of place — each file might be at its correct position, or shifted to one of its adjacent slots.

**Task:**
Find the exact index of a given file ID (target). If the file isn't present, return -1.

**Rules of the search:**
- The archive is almost sorted (each element may be at i, i-1, or i+1)
- You must return the 0-based index of the target
- If not found, return -1

**Input Format:**
- First line: `arr[]` → space-separated integers (almost sorted array)
- Second line: `target` → the integer to search for

**Output Format:**
- A single integer representing the index of target in `arr[]`
- If not found, output -1

**Constraints:**
- 1 ≤ arr.size() ≤ 10⁵
- -10⁹ ≤ arr[i] ≤ 10⁹
- -10⁹ ≤ target ≤ 10⁹

**Examples:**
```python
# Example
arr = [10, 3, 40, 20, 50, 80, 70]
target = 40
Output: 2
```

**Solution Approach:**
Modified binary search that checks current, left, and right neighbors of mid.

---

## Problem 15: Find Peak Element

**Problem Statement:**
You are given a 0-indexed integer array `nums` representing the heights of mountains arranged in a line.

A peak element is an element that is strictly greater than its adjacent neighbors.

**Task:**
Find and return the index of any peak element.

**Assumptions:**
- nums[-1] = -∞
- nums[n] = -∞
- This means the first or last element can also be a peak if it is greater than its only neighbor

Your solution must run in O(log n) time.

**Input:**
- An integer array `nums`

**Output:**
- Return the index of any peak element

**Constraints:**
- 1 <= nums.length <= 1000
- -2³¹ <= nums[i] <= 2³¹ - 1
- nums[i] != nums[i + 1] for all valid i

**Examples:**
```python
# Example
nums = [1, 2, 3, 1]
Output: 2  # nums[2] = 3 is a peak
```

**Solution Approach:**
Binary search comparing middle element with neighbors to find the peak direction.

---

## Problem 16: Search a 2D Matrix II

**Problem Statement:**
You are working as a data analyst in a logistics company. The company stores shipment IDs in a large 2D grid. The racks follow two rules:
- Each row is sorted in ascending order from left to right
- Each column is sorted in ascending order from top to bottom

**Task:**
Given a shipment ID (target), determine whether the shipment exists in the warehouse grid.

**Input Format:**
- The first line contains two integers `m` and `n` — the number of rows and columns in the matrix
- The next `m` lines each contain `n` integers, representing one row of the matrix
- The last line contains a single integer `target`

**Output Format:**
- Print `True` if target exists in the matrix
- Print `False` otherwise

**Constraints:**
- 1 ≤ m, n ≤ 300
- -10⁹ ≤ matrix[i][j] ≤ 10⁹
- -10⁹ ≤ target ≤ 10⁹
- All rows are sorted in ascending order
- All columns are sorted in ascending order

**Examples:**
```python
# Example
matrix = [
  [1,  4,  7,  11, 15],
  [2,  5,  8,  12, 19],
  [3,  6,  9,  16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
Output: True
```

**Solution Approach:**
Start from top-right or bottom-left corner and move based on comparisons.

---

## Problem 17: Search a 2D Matrix I

**Problem Statement:**
You are managing a warehouse inventory system. Items are stored in racks arranged as a 2D grid. The racks follow two strict rules:
- Each rack (row) is sorted in non-decreasing order of item IDs
- The first item ID of a rack is always greater than the last item ID of the previous rack

This arrangement ensures that if you flatten the racks into a single list, the entire inventory is sorted.

**Task:**
Given an item ID (target), determine whether the item exists in the warehouse.

**Input Format:**
- The first line contains two integers `m` and `n` — the number of rows and columns in the matrix
- The next `m` lines each contain `n` integers, representing one row of the matrix
- The last line contains a single integer `target`

**Output Format:**
- Print `True` if target exists in the matrix
- Print `False` otherwise

**Constraints:**
- 1 ≤ m, n ≤ 100
- -10⁴ ≤ matrix[i][j], target ≤ 10⁴

**Examples:**
```python
# Example
matrix = [
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
target = 3
Output: True
```

**Solution Approach:**
Treat the 2D matrix as a flattened sorted 1D array and perform binary search.

---

## Problem 18: Search in Rotated Sorted Array

**Problem Statement:**
There is an integer array `nums` sorted in ascending order containing distinct integers. Before being passed to your function, the array is possibly rotated at an unknown index such that the resulting array remains partially sorted.

**Task:**
Given the rotated sorted array `nums` and an integer `target`, return the index of the target if it is present in the array. If the target is not found, return -1.

**Input Format:**
- An integer `n` representing the size of the array
- A rotated sorted list `nums` of `n` distinct integers
- An integer `target` to search for

**Output Format:**
- Return an integer representing the index of target in the array
- If the target is not found, return -1

**Constraints:**
- 1 ≤ n ≤ 5000
- −10⁴ ≤ nums[i] ≤ 10⁴
- All values in `nums` are distinct
- `nums` was originally sorted in ascending order and then possibly rotated
- −10⁴ ≤ target ≤ 10⁴

**Examples:**
```python
# Example
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
Output: 4
```

**Solution Approach:**
Binary search identifying which half is sorted, then determining which half contains the target.

---

## Problem 19: Search in Rotated Sorted Array II

**Problem Statement:**
You are given an integer array `nums` that was originally sorted in ascending order, but may have been rotated at an unknown index.

Unlike the previous version, the array may contain duplicate values.

**Task:**
Given the rotated sorted array `nums` and an integer `target`, determine whether target exists in the array.

Return `true` if the target is found, otherwise return `false`.

**Input Format:**
- First line contains an integer `n` — the size of the array
- Second line contains `n` space-separated integers representing the rotated sorted array `nums` (may contain duplicates)
- Third line contains an integer `target` — the value to search for

**Output Format:**
- Print `true` if the target exists in the array
- Print `false` otherwise

**Constraints:**
- 1 ≤ n ≤ 5000
- -10⁴ ≤ nums[i] ≤ 10⁴
- `nums` was originally sorted in ascending order and then possibly rotated
- `nums` may contain duplicate values
- -10⁴ ≤ target ≤ 10⁴

**Examples:**
```python
# Example
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
Output: true
```

**Solution Approach:**
Binary search with handling for duplicate values by shrinking search space when boundaries equal mid.

---

## Problem 20: Koko Eating Bananas

**Problem Statement:**
Koko loves bananas. There are `n` piles of bananas, where the i-th pile has `piles[i]` bananas. The guards are away and will return in `h` hours.

Koko can choose an eating speed `k` (bananas per hour). Each hour:
- She selects one pile and eats up to `k` bananas
- If the pile has fewer than `k` bananas, she eats all of them and rests for the remainder of that hour

Koko wants to eat as slowly as possible but still finish all the bananas before the guards return.

**Task:**
Return the minimum integer `k` such that Koko can eat all the bananas within `h` hours.

**Input Format:**
- `piles`: an array of integers, where `piles[i]` represents the number of bananas in the i-th pile
- `h`: an integer representing the number of hours before the guards return

**Output Format:**
- A single integer `k` → the minimum bananas per hour Koko must eat to finish all piles within `h` hours

**Constraints:**
- 1 ≤ piles.length ≤ 10⁴
- piles.length ≤ h ≤ 10⁹
- 1 ≤ piles[i] ≤ 10⁹

**Examples:**
```python
# Example
piles = [3, 6, 7, 11]
h = 8
Output: 4
```

**Solution Approach:**
Binary search on the eating speed, calculating hours needed for each speed.

---

## Problem 21: Sorting the Treasure Chest

**Problem Statement:**
A group of explorers discovered a chest filled with numbered coins. The coins were scattered randomly inside, and the explorers needed to arrange them neatly in ascending order before presenting them to the king.

**Task:**
Help the explorers sort the coins. Given an array of integers `nums`, return the array sorted in ascending order.

**Input Format:**
- An integer array `nums` of length n

**Output Format:**
- The sorted array in ascending order

**Constraints:**
- 1 ≤ nums.length ≤ 5 × 10⁴
- -5 × 10⁴ ≤ nums[i] ≤ 5 × 10⁴

**Examples:**
```python
# Example
nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
```

**Solution Approach:**
Can use built-in sort, merge sort, quick sort, or heap sort depending on requirements.

---

## Problem 22: Squares of a Sorted Array

**Problem Statement:**
You are given an integer array `nums` sorted in non-decreasing order.

**Task:**
Square each number in the array and return a new array containing these squares, also sorted in non-decreasing order.

Note: Since the array contains both negative and positive numbers, squaring them and then keeping the same order will not always give the correct result.

**Input Format:**
- The first line contains an integer `n` — the number of elements in the array
- The second line contains `n` space-separated integers representing the array `nums`, sorted in non-decreasing order

**Output Format:**
- Print `n` space-separated integers representing the sorted squares of the input array

**Constraints:**
- 1 ≤ n ≤ 10⁵
- -10⁴ ≤ nums[i] ≤ 10⁴
- The array `nums` is already sorted in non-decreasing order

**Examples:**
```python
# Example
nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
```

**Solution Approach:**
Two-pointer approach: squares are largest at both ends, so fill result array from end.

---

## Problem 23: The Archivist's Cleanup

**Problem Statement:**
In an ancient digital library, an archivist stores records as rows of characters. Each record has the same length, and when all records are placed one below another, they form a rectangular grid.

Over time, some columns of this grid became corrupted. A column is considered valid only if the characters from top to bottom are in non-decreasing lexicographical order (alphabetical order).

The archivist can delete entire columns to restore order.

**Task:**
Determine how many columns must be deleted so that every remaining column is lexicographically sorted from top to bottom.

**Input Format:**
- The first line contains an integer `n` — the number of strings
- The next `n` lines each contain a string of lowercase English letters
- All strings have the same length

**Output Format:**
- Print a single integer — the number of columns that need to be deleted

**Constraints:**
- n ≥ 1
- All strings have same length

**Examples:**
```python
# Example
records = [
  "cba",
  "daf",
  "ghi"
]
Output: 1  # Column 0: c, d, g (sorted); Column 1: b, a, h (not sorted); Column 2: a, f, i (sorted)
# So delete 1 column
```

**Solution Approach:**
Check each column vertically to see if characters are in non-decreasing order.

---

## Problem 24: Relative Ranks

**Problem Statement:**
You are given an integer array `score` of size `n`, where `score[i]` represents the score of the ith athlete in a competition.

All scores are unique.

Athletes are ranked based on their scores:
- The athlete with the highest score gets "Gold Medal"
- The second highest gets "Silver Medal"
- The third highest gets "Bronze Medal"
- From 4th position onward, the athlete gets their position number as a string (for example, "4", "5")

**Task:**
Return an array `answer` where `answer[i]` is the rank of the ith athlete.

**Input Format:**
- First line: Integer `n`
- Second line: `n` space-separated integers representing scores

**Output Format:**
- Print `n` space-separated strings representing ranks in original order

**Constraints:**
- 1 <= n <= 10⁴
- 0 <= score[i] <= 10⁶
- All scores are unique

**Examples:**
```python
# Example 1
scores = [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

# Example 2
scores = [10, 3, 8, 9, 4]
Output: ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
```

**Solution Approach:**
Create index-score pairs, sort by score descending, assign ranks, then reorder to original positions.

---

## Problem 25: Two Numbers Unlock the Target

**Problem Statement:**
Imagine you're a treasure hunter with a sorted list of gems, each gem having a numerical value. You're told there are two gems in this list that together match a secret target value.

**Task:**
Find the exact positions of these two gems in the list.

**Rules:**
- The list is 1-indexed (the first gem is at position 1)
- You cannot use the same gem twice
- There is exactly one solution guaranteed
- You must solve it using only constant extra space (no big storage tricks)

**Input Format:**
- `numbers`: a sorted array of integers (non-decreasing order)
- `target`: an integer representing the desired sum

**Output Format:**
- An array `[index1, index2]` of length 2, representing the 1-based indices of the two numbers that sum to target

**Constraints:**
- 2 ≤ numbers.length ≤ 3 × 10⁴
- -1000 ≤ numbers[i] ≤ 1000
- numbers is sorted in non-decreasing order
- -1000 ≤ target ≤ 1000
- Exactly one solution exists

**Examples:**
```python
# Example
numbers = [2, 7, 11, 15]
target = 9
Output: [1, 2]
# Explanation: numbers[0] + numbers[1] = 2 + 7 = 9
```

**Solution Approach:**
Two-pointer technique: one from start, one from end, adjust based on sum.

---

## Problem 26: Largest Number

**Problem Statement:**
You are given a list of non-negative integers `nums`.

**Task:**
Arrange them such that they form the largest possible number.

Since the result may be very large, return it as a string instead of an integer.

**Input Format:**
- First line: Integer `n`
- Second line: `n` space-separated non-negative integers

**Output Format:**
- Print a single string representing the largest possible number formed by arranging the given integers

**Constraints:**
- 1 <= n <= 100
- 0 <= nums[i] <= 10⁹

**Important Note:**
If the resulting number contains leading zeros (for example, input: 0 0), the output should be "0" and not "00".

**Examples:**
```python
# Example 1
nums = [10, 2]
Output: "210"

# Example 2
nums = [3, 30, 34, 5, 9]
Output: "9534330"
```

**Solution Approach:**
Custom comparator: sort by comparing concatenations of pairs (a+b vs b+a).

---

## Problem 27: Maximum Units on a Truck

**Problem Statement:**
You are given a 2D array `boxTypes` where each element `boxTypes[i] = [numberOfBoxes, numberOfUnitsPerBox]`.

- `numberOfBoxes` represents the number of boxes available of that type
- `numberOfUnitsPerBox` represents the number of units contained in each box of that type

You are also given an integer `truckSize`, which is the maximum number of boxes that can be loaded onto the truck.

**Task:**
Determine the maximum total number of units that can be loaded onto the truck without exceeding the given `truckSize`.

**Input Format:**
- The first line contains an integer `n` — the number of box types
- The second line contains `2*n` space-separated integers representing boxTypes in flattened form:
  `[numberOfBoxes1, numberOfUnits1, numberOfBoxes2, numberOfUnits2, ...]`
- The third line contains an integer `truckSize` — the maximum number of boxes the truck can carry

**Output Format:**
- Print a single integer representing the maximum total number of units that can be loaded onto the truck

**Constraints:**
- 1 ≤ n ≤ 1000
- 1 ≤ numberOfBoxes ≤ 1000
- 1 ≤ numberOfUnitsPerBox ≤ 1000
- 1 ≤ truckSize ≤ 10⁶

**Examples:**
```python
# Example
boxTypes = [[1,3], [2,2], [3,1]]
truckSize = 4
Output: 8
# Explanation: Take all boxes of type 1 (1 box with 3 units each) and 3 boxes of type 2 (3*2=6 units)
# Total: 1 box -> 3 units, 3 boxes -> 6 units, total = 9? No wait...
# Take 1 box of type 1 (3 units) and 3 boxes of type 2 (2 units each = 6 units). Total = 9? Let me recalculate
# Actually: 1 + 3 = 4 boxes with 3 + 6 = 9 units. But output is 8, so...
# Take 1 box of type 1 (3 units) and 1 box of type 2 (2 units) = 2 boxes with 5 units? No...
# Take 4 boxes total with max units: 1 of type 1 (3 units) + can take 3 of type 2 (6 units) = 4 boxes, 9 units? Still not 8
# Actually must be: 2 of type 2 (4 units) + 2 of type 1? No type 1 has 1 box only. Greedy: type 1 (1 box, 3 units) + type 2 (3 boxes, 6 units) = 4 boxes, 9 units total
# Wait, the output says 8. Let me reread... maybe (1 box, 3 units) + (3 boxes, 2 units each) but we have only truckSize=4
# So 1 + 3 = 4 total boxes, 3 + 3*2 = 3 + 6 = 9 units. Output should be 9 but it says 8
# Must be there's an issue with my calculation or the example. Using greedy approach of highest units per box should work.
```

**Solution Approach:**
Greedy approach: sort by units per box descending, fill truck with highest value boxes first.

---

## Problem 28: Repeated DNA Sequences

**Problem Statement:**
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

Given a string `s` that represents a DNA sequence, return all the 10-letter-long sequences that occur more than once.

Print results in sorted order separated by space.

**Input:**
- One line containing string `s`

**Output:**
- Print all repeated 10-letter sequences in sorted order separated by space

**Constraints:**
- 1 ≤ s.length ≤ 10⁵
- s[i] is either 'A', 'C', 'G', or 'T'

**Examples:**
```python
# Example
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: "AAAAACCCCC CCCCCAAAAA"
```

**Solution Approach:**
Use a sliding window of size 10 with a hash set to track seen sequences and count occurrences.

---
