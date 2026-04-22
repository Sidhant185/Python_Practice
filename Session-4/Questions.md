
---

---

## Problem 1: Pair Sum Checker

**Problem Statement:**
Given a list of integers and a value `x`, check if any two numbers in the list sum to `x`. Return "Yes" or "No".

**Examples:**
```python
# Example 1
n = 5
arr = [8, 1, 4, 6, 2]
x = 10
Output: "Yes" # (8, 2) or (4, 6) sum to 10
```

**What to Use / NOT Use:**
* ✅ Use: Hash set for O(n) lookup.
* ❌ Avoid: O(n²) nested loops.

**Key Concepts:**
* For each number `num`, check if `(x - num)` exists in the set of previously seen numbers.

**Solution:**
```python
def pairSumChecker(arr, x):
    seen = set()
    for num in arr:
        if x - num in seen:
            return "Yes"
        seen.add(num)
    return "No"
```

**Complexity Analysis:**
- Time: O(n)
- Space: O(n)

---

## Problem 2: Nearby Duplicate

**Problem Statement:**
Check if there exist two indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

**Examples:**
```python
# Example
nums = [1, 2, 3, 1]
k = 3
Output: True # nums[0] == nums[3] and |0-3| <= 3
```

**What to Use / NOT Use:**
* ✅ Use: Dictionary (value → last index) or a Sliding Window Hash Set.
* ❌ Avoid: Nested loops.

**Key Concepts:**
* Track the last index where each value was seen. If the difference is within `k`, return `True`.

**Solution:**
```python
def containsNearbyDuplicate(nums, k):
    last_seen = {}
    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    return False
```

**Complexity Analysis:**
- Time: O(n)
- Space: O(n)

---

## Problem 3: Garden Plot Allocation

**Problem Statement:**
Given a list of 0s and 1s representing a flowerbed, check if `k` new plants can be placed without any two plants being adjacent.

**Examples:**
```python
# Example 1
arr = [1, 0, 0, 0, 1]
k = 1
Output: True

# Example 2
arr = [1, 0, 0, 0, 1]
k = 2
Output: False
```

**What to Use / NOT Use:**
* ✅ Use: Greedy placement.
* ❌ Avoid: Overcomplicating with backtracking unless necessary.

**Key Concepts:**
* A plant can be placed if the current spot, previous spot, and next spot are all empty (0).

**Solution:**
```python
def canPlaceFlowers(flowerbed, k):
    count = 0
    f = [0] + flowerbed + [0] # Handle boundary conditions
    for i in range(1, len(f) - 1):
        if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            count += 1
    return count >= k
```

---

## Problem 4: Minimize Height Difference I

**Problem Statement:**
Modify each tower height by adding or subtracting `k`. Find the minimum possible difference between the tallest and shortest towers.

**Examples:**
```python
arr = [1, 5, 8, 10]
k = 2
Output: 5
```

**What to Use / NOT Use:**
* ✅ Use: Sorting + Greedy range minimization.

**Key Concepts:**
* Sort the array. For each tower `i`, calculate potential new max and min after adjusting by `k`.

**Solution:**
```python
def getMinDiff(arr, k):
    arr.sort()
    n = len(arr)
    ans = arr[-1] - arr[0]
    
    for i in range(n - 1):
        # Potential min and max after adjustment
        mini = min(arr[0] + k, arr[i + 1] - k)
        maxi = max(arr[-1] - k, arr[i] + k)
        ans = min(ans, maxi - mini)
    return ans
```

---

## Problem 5: Minimize Height Difference II

**Problem Statement:**
Same as Problem 4, but ensure no tower height becomes negative after modification.

**Examples:**
```python
arr = [1, 5, 8, 10]
k = 2
Output: 5
```

**Solution:**
```python
def getMinDiffII(arr, k):
    arr.sort()
    n = len(arr)
    ans = arr[-1] - arr[0]
    
    for i in range(n - 1):
        if arr[i + 1] < k: continue # Height cannot be negative
        mini = min(arr[0] + k, arr[i + 1] - k)
        maxi = max(arr[-1] - k, arr[i] + k)
        ans = min(ans, maxi - mini)
    return ans
```

---

## Problem 6: Snake Pattern Matrix

**Problem Statement:**
Print the matrix in a snake-like pattern: left-to-right for even rows, right-to-left for odd rows.

**Examples:**
```python
matrix = [
 [45, 48, 54],
 [21, 89, 87],
 [70, 78, 15]
]

Output: 45 48 54 87 89 21 70 78 15
```

**Key Concepts:**
* Check row index `% 2`. If 0, iterate normally. If 1, iterate in reverse.

**Solution:**
```python
def snakePattern(matrix):
    res = []
    for i in range(len(matrix)):
        if i % 2 == 0:
            for j in range(len(matrix[0])):
                res.append(matrix[i][j])
        else:
            for j in range(len(matrix[0]) - 1, -1, -1):
                res.append(matrix[i][j])
    return res
```

---

## Problem 7: Transpose of Matrix

**Problem Statement:**
Swap rows with columns of a given matrix.

**Examples:**
```python
matrix = [
 [1, 2, 3],
 [4, 5, 6]
]

Output:
1 4
2 5
3 6
```

**Solution:**
```python
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # Create new matrix with swapped dimensions
    res = [[0] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            res[c][r] = matrix[r][c]
    return res
```

---

## Problem 8: Toeplitz Matrix

**Problem Statement:**
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

**Examples:**
```python
matrix = [
 [1, 2, 3, 4],
 [5, 1, 2, 3],
 [9, 5, 1, 2]
]

Output: True
```

**Solution:**
```python
def isToeplitzMatrix(matrix):
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[0])):
            if matrix[r][c] != matrix[r-1][c-1]:
                return False
    return True
```

---

## Problem 9: Rotate Matrix 90° Clockwise

**Problem Statement:**
Rotate an `N x N` matrix 90 degrees clockwise in-place.

**Examples:**
```python
matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

Output:
7 4 1
8 5 2
9 6 3
```

**Key Concepts:**
1. Transpose the matrix.
2. Reverse each row.

**Solution:**
```python
def rotate(matrix):
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse Rows
    for i in range(n):
        matrix[i].reverse()
```

---

## Problem 10: Pascal Triangle

**Problem Statement:**
Generate the first `numRows` of Pascal's triangle.

**Examples:**
```python
numRows = 5
Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

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

---

## Problem 11: Exit Point of Matrix

**Problem Statement:**
Given a matrix of 0s and 1s, start at (0,0) moving right. When you hit a 1, turn 90° clockwise and change the 1 to 0. Find the coordinates where you exit the matrix.

**Examples:**
```python
matrix = [
 [0, 1, 0],
 [0, 1, 1],
 [0, 0, 0]
]
Output: 1 0
```

**Solution:**
```python
def exitPoint(matrix):
    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, 0
    dir = 0 # 0: East, 1: South, 2: West, 3: North
    
    while True:
        if matrix[r][c] == 1:
            dir = (dir + 1) % 4
            matrix[r][c] = 0
            
        # Try moving
        prev_r, prev_c = r, c
        if dir == 0: c += 1
        elif dir == 1: r += 1
        elif dir == 2: c -= 1
        elif dir == 3: r -= 1
        
        # Check exit
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return f"{prev_r} {prev_c}"
```

---

## Problem 12: Hourglass Sum

**Problem Statement:**
Find the maximum sum of an hourglass pattern in a 6x6 matrix.

**Examples:**
```python
matrix = [
 [6, 2, 1, 3],
 [4, 2, 1, 5],
 [9, 2, 8, 7],
 [4, 1, 2, 9]
]
Output: 30 # Sum of top-left hourglass
```

**Solution:**
```python
def hourglassSum(matrix):
    max_sum = float('-inf')
    for r in range(len(matrix) - 2):
        for c in range(len(matrix[0]) - 2):
            top = sum(matrix[r][c:c+3])
            mid = matrix[r+1][c+1]
            bot = sum(matrix[r+2][c+3])
            max_sum = max(max_sum, top + mid + bot)
    return max_sum
```

---

## Problem 13: Largest Odd Number in String

**Problem Statement:**
Given a string `num`, return the largest-valued odd integer that is a non-empty substring of `num`.

**Examples:**
```python
num = "52"
Output: "5"
```

**Solution:**
```python
def largestOddNumber(num):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""
```

---

## Problem 14: Reverse Prefix of Word

**Problem Statement:**
Reverse the string from start until the first occurrence of a character `ch`.

**Examples:**
```python
word = "abcdefd", ch = "d"
Output: "dcbaefd"
```

**Solution:**
```python
def reversePrefix(word, ch):
    idx = word.find(ch)
    if idx == -1: return word
    return word[:idx+1][::-1] + word[idx+1:]
```

---

## Problem 15: Balanced String

**Problem Statement:**
Check if all characters in the string appear an equal number of times.

**Examples:**
```python
s = "abacbc"
Output: True # a:2, b:2, c:2
```

**Solution:**
```python
from collections import Counter

def isBalanced(s):
    counts = Counter(s)
    return len(set(counts.values())) == 1
```

---

## Problem 16: Conveyor Belt

**Problem Statement:**
Count the maximum number of operations where you can shift '1' over '0' (e.g., "10" becomes "01").

**Examples:**
```python
s = "1001101"
Output: 4
```

**Solution:**
```python
def maxConveyorShifts(s):
    res = 0
    res, ones = 0, 0
    for i in range(len(s)):
        if s[i] == '1':
            ones += 1
        elif i > 0 and s[i-1] == '1':
            res += ones
    return res
```

---

## Problem 17: Multiply Strings

**Problem Statement:**
Multiply two numeric strings without using built-in big integer libraries.

**Examples:**
```python
num1 = "2", num2 = "3"
Output: "6"
```

**Solution:**
```python
def multiply(num1, num2):
    if num1 == "0" or num2 == "0": return "0"
    res = [0] * (len(num1) + len(num2))
    for i in range(len(num1)-1, -1, -1):
        for j in range(len(num2)-1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            total = mul + res[p2]
            res[p2] = total % 10
            res[p1] += total // 10
            
    start = 0
    while start < len(res) and res[start] == 0: start += 1
    return "".join(map(str, res[start:]))
```

---

## Problem 18: Balanced Binary Substrings

**Problem Statement:**
Count the number of non-empty substrings that have the same number of 0s and 1s, and all 0s and 1s are grouped consecutively.

**Examples:**
```python
s = "0100110101"
Output: 4 # "01", "10", "0011", "10"
```

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

## Problem 19: Mirror Note Check (Palindrome)

**Problem Statement:**
Clean a string (remove non-alphanumeric, lowercase) and check if it's a palindrome.

**Examples:**
```python
s = "A man, a plan, a canal: Panama"
Output: True
```

**Solution:**
```python
def isPalindrome(s):
    filtered = "".join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]
```

---

## Problem 20: Magical Scroll Swap

**Problem Statement:**
Check if swapping two characters in string `s` can make it equal to `goal`.

**Examples:**
```python
s = "ab", goal = "ba"
Output: True
```

**Solution:**
```python
def buddyStrings(s, goal):
    if len(s) != len(goal): return False
    if s == goal:
        return len(set(s)) < len(s)
    
    diffs = [i for i in range(len(s)) if s[i] != goal[i]]
    if len(diffs) != 2: return False
    
    i, j = diffs
    return s[i] == goal[j] and s[j] == goal[i]
```

