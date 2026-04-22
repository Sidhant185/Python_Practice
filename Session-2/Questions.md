# 🧠 Python Practice — Lists & Arrays (15 Questions)

A comprehensive guide to list manipulation, searching, and advanced algorithms.

---

## 🎯 SECTION 1: BASIC LIST OPERATIONS

### Q1: Sum of List Elements
**Problem:** Take a list of numbers as input and print their sum.

**Example:**
```
Input: [1, 2, 3, 4, 5]
Output: Sum = 15
```

**What to Use:**
- `sum()` built-in function (RECOMMENDED)
- Loop with accumulator variable
- List comprehension (optional)

**What NOT to Use:**
- ❌ Don't hardcode list values
- ❌ Don't manually add each element

**Concepts:**
- List basics
- Accumulator pattern
- Built-in functions

**Solution Approach:**
```python
# BEST (Built-in):
numbers = [1, 2, 3, 4, 5]
print(f"Sum = {sum(numbers)}")

# GOOD (Loop):
numbers = list(map(int, input("Enter numbers: ").split()))
total = 0
for num in numbers:
    total += num
print(f"Sum = {total}")

# GETTING INPUT:
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(f"Sum = {sum(numbers)}")
```

**Key Points:**
- `sum()` returns 0 for empty list
- Input parsing with `.split()` and `map()`
- List comprehension for type conversion

---

### Q2: Find Maximum and Minimum
**Problem:** Find the maximum and minimum values in a list.

**Example:**
```
Input: [3, 1, 9, 2, 8]
Output:
Maximum: 9
Minimum: 1
```

**What to Use:**
- `max()` and `min()` built-in functions (RECOMMENDED)
- Manual loop to compare values
- Sorting approach

**What NOT to Use:**
- ❌ Don't hardcode values
- ❌ Don't assume list is sorted

**Solution Approach:**
```python
# BEST (Built-in):
numbers = [3, 1, 9, 2, 8]
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

# GOOD (Manual loop):
numbers = [3, 1, 9, 2, 8]
max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")

# WITH INPUT:
numbers = list(map(int, input().split()))
print(f"Max: {max(numbers)}, Min: {min(numbers)}")
```

**Key Points:**
- Initialize min/max with first element
- Compare during iteration
- Handle edge cases (empty list)

---

### Q3: Count Even and Odd Numbers
**Problem:** Count how many even and odd numbers are in a list.

**Example:**
```
Input: [1, 2, 3, 4, 5, 6]
Output:
Even count: 3 (2, 4, 6)
Odd count: 3 (1, 3, 5)
```

**What to Use:**
- Loop through list
- Modulo operator: `%`
- Accumulator variables for counting
- List comprehension (optional)

**What NOT to Use:**
- ❌ Don't use multiple loops

**Solution Approach:**
```python
# GOOD (Loop):
numbers = [1, 2, 3, 4, 5, 6]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even: {even_count}, Odd: {odd_count}")

# ELEGANT (List comprehension):
numbers = [1, 2, 3, 4, 5, 6]
even_count = len([n for n in numbers if n % 2 == 0])
odd_count = len([n for n in numbers if n % 2 == 1])
print(f"Even: {even_count}, Odd: {odd_count}")
```

**Key Points:**
- Use modulo `%` to check even/odd
- Initialize counters to 0
- Increment appropriately

---

### Q4: Reverse List Without Built-in
**Problem:** Reverse a list WITHOUT using built-in `.reverse()` or slicing.

**Example:**
```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

**What to Use:**
- Two-pointer approach
- Create new list and append from end
- Manual loop with indices

**What NOT to Use:**
- ❌ Don't use `.reverse()` method
- ❌ Don't use slicing `[::-1]`
- ❌ Don't use `reversed()` function

**Solution Approach:**
```python
# GOOD (Two-pointer - In-place):
def reverse_list(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))

# GOOD (New list from end):
numbers = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])
print(reversed_list)
```

**Key Points:**
- Two-pointer starts at opposite ends
- Swap elements during iteration
- Works in O(n) time, O(1) space

---

### Q5: Remove Duplicates from List
**Problem:** Remove duplicate elements from a list while maintaining order.

**Example:**
```
Input: [1, 2, 2, 3, 3, 3, 4, 5, 5]
Output: [1, 2, 3, 4, 5]
```

**What to Use:**
- Loop with new list and checking (maintains order)
- Set conversion (fastest, loses order)
- Dictionary/set tracking

**What NOT to Use:**
- ❌ Don't use nested loops (inefficient)

**Solution Approach:**
```python
# GOOD (Maintains order with list):
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)

# FASTEST (Using set - loses order):
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(numbers))
print(unique)

# MAINTAINS ORDER (Using dict - Python 3.7+):
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(dict.fromkeys(numbers))
print(unique)

# OPTIMIZED (Using set for O(1) lookup):
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
seen = set()
unique = []
for num in numbers:
    if num not in seen:
        seen.add(num)
        unique.append(num)
print(unique)
```

**Key Points:**
- `not in` check for membership
- Set conversion is fastest but loses order
- Dict method preserves insertion order (Python 3.7+)

---

## 🔧 SECTION 2: INTERMEDIATE LIST OPERATIONS

### Q6: Find Second Largest Number
**Problem:** Find the second largest number in a list.

**Example:**
```
Input: [5, 2, 9, 1, 7, 6]
Output: Second Largest = 7
```

**What to Use:**
- Sorting: `sorted()` then access second-last element
- Manual loop to track largest and second-largest

**Solution Approach:**
```python
# GOOD (Sorting):
numbers = [5, 2, 9, 1, 7, 6]
unique_sorted = sorted(set(numbers), reverse=True)
if len(unique_sorted) < 2:
    print("No second largest")
else:
    print(f"Second Largest: {unique_sorted[1]}")

# GOOD (Manual loop):
numbers = [5, 2, 9, 1, 7, 6]
largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(f"Second Largest: {second_largest}")
```

**Key Points:**
- Handle duplicates by converting to set
- Track two variables: largest and second_largest

---

### Q7: Rotate List by K Steps
**Problem:** Rotate a list to the right by k positions.

**Example:**
```
Input: [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
```

**What to Use:**
- Slicing: `arr[-k:] + arr[:-k]`
- Modulo for circular behavior

**Solution Approach:**
```python
# BEST (Slicing):
def rotate_list(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

numbers = [1, 2, 3, 4, 5]
print(rotate_list(numbers, 2))
```

**Key Points:**
- Use modulo to handle k > length
- Slicing approach is most readable

---

### Q8: Merge Two Lists
**Problem:** Merge two lists into one.

**Example:**
```
Input: [1, 2, 3], [4, 5, 6]
Output: [1, 2, 3, 4, 5, 6]
```

**What to Use:**
- `+` operator for concatenation (simplest)
- `.extend()` method (modifies original)

**Solution Approach:**
```python
# SIMPLEST:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print(merged)

# USING extend:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
```

**Key Points:**
- `+` creates new list
- `.extend()` modifies original

---

### Q9: Find Frequency of Each Element
**Problem:** Count how many times each element appears in the list.

**Example:**
```
Input: [1, 2, 2, 3, 3, 3, 2]
Output:
1: 1 time
2: 3 times
3: 3 times
```

**What to Use:**
- Dictionary to store counts
- `collections.Counter` (Pythonic)

**Solution Approach:**
```python
# PYTHONIC (Using Counter):
from collections import Counter
numbers = [1, 2, 2, 3, 3, 3, 2]
frequency = Counter(numbers)
for num, count in frequency.items():
    print(f"{num}: {count} times")

# GOOD (Dictionary):
numbers = [1, 2, 2, 3, 3, 3, 2]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

for num, count in frequency.items():
    print(f"{num}: {count} times")
```

**Key Points:**
- Dictionary maps element to count
- Counter is built for this task

---

### Q10: Move All Zeros to End
**Problem:** Move all zeros to end while maintaining order of non-zeros.

**Example:**
```
Input: [1, 0, 2, 0, 3, 0, 4]
Output: [1, 2, 3, 4, 0, 0, 0]
```

**What to Use:**
- Two-pointer approach (in-place)
- Separate lists and concatenate

**Solution Approach:**
```python
# BEST (Two-pointer):
def move_zeros(arr):
    non_zero_index = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    
    while non_zero_index < len(arr):
        arr[non_zero_index] = 0
        non_zero_index += 1
    
    return arr

numbers = [1, 0, 2, 0, 3, 0, 4]
print(move_zeros(numbers))

# GOOD (Separate and combine):
def move_zeros(arr):
    non_zeros = [x for x in arr if x != 0]
    zeros = [0] * arr.count(0)
    return non_zeros + zeros
```

**Key Points:**
- Two-pointer is most efficient O(n), O(1)
- Maintain order of non-zero elements

---

## 🚀 SECTION 3: ADVANCED ALGORITHMS

### Q11: Find Missing Number in Range
**Problem:** Find the missing number from a sequence 1 to n.

**Example:**
```
Input: [1, 2, 4, 5, 6]
Output: Missing = 3
```

**What to Use:**
- Mathematical formula: sum - actual_sum
- Set difference

**Solution Approach:**
```python
# BEST (Mathematical):
def find_missing(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(find_missing([1, 2, 4, 5, 6]))

# GOOD (Set difference):
def find_missing(arr):
    complete = set(range(1, len(arr) + 2))
    return complete.difference(set(arr)).pop()
```

**Key Points:**
- Sum formula is O(1) space
- Mathematical approach is optimal

---

### Q12: Find Intersection of Two Lists
**Problem:** Find common elements between two lists.

**Example:**
```
Input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: [3, 4]
```

**What to Use:**
- Set intersection (fastest)
- List comprehension (maintains order)

**Solution Approach:**
```python
# BEST (Set):
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = list(set(list1) & set(list2))
print(intersection)

# MAINTAINS ORDER:
intersection = [x for x in list1 if x in list2]
print(intersection)
```

**Key Points:**
- Set intersection is O(n+m)
- List comprehension maintains order

---

### Q13: Find Pairs with Given Sum
**Problem:** Find all pairs that sum to a target.

**Example:**
```
Input: [1, 5, 7, -1, 5], target = 6
Output: [(1, 5), (7, -1)]
```

**What to Use:**
- Hash set (O(n) time)
- Two-pointer (sorted)

**Solution Approach:**
```python
# BEST (Hash set):
def find_pairs(arr, target):
    seen = set()
    pairs = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    
    return list(pairs)

print(find_pairs([1, 5, 7, -1, 5], 6))

# TWO-POINTER (Sorted):
def find_pairs(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    pairs = []
    
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            pairs.append((arr[left], arr[right]))
            left += 1
        elif s < target:
            left += 1
        else:
            right -= 1
    return pairs
```

**Key Points:**
- Hash set gives O(n) complexity
- Complement = target - current number

---

### Q14: Kadane's Algorithm (Maximum Subarray Sum)
**Problem:** Find contiguous subarray with largest sum.

**Example:**
```
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: Maximum Sum = 6 (subarray [4, -1, 2, 1])
```

**What to Use:**
- Kadane's algorithm (O(n), O(1))
- Dynamic programming

**Solution Approach:**
```python
# BEST (Kadane's Algorithm):
def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Max Sum: {max_subarray_sum(numbers)}")
```

**Key Points:**
- Track current and maximum sum
- O(n) time, O(1) space

---

### Q15: Flatten a 2D List
**Problem:** Convert a 2D list into 1D.

**Example:**
```
Input: [[1, 2], [3, 4], [5, 6]]
Output: [1, 2, 3, 4, 5, 6]
```

**What to Use:**
- List comprehension (Pythonic)
- Nested loops

**Solution Approach:**
```python
# BEST (List comprehension):
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [item for row in matrix for item in row]
print(flattened)

# GOOD (Nested loops):
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = []
for row in matrix:
    for item in row:
        flattened.append(item)
print(flattened)

# PYTHONIC (itertools):
import itertools
flattened = list(itertools.chain(*matrix))
print(flattened)
```

**Key Points:**
- List comprehension is most Pythonic
- Works for irregular lists too

---

## 📊 COMPARISON TABLE

| Problem | Best Approach | Time | Space |
|---------|---------------|------|-------|
| Sum | `sum()` | O(n) | O(1) |
| Max/Min | `max()/min()` | O(n) | O(1) |
| Reverse | Two-pointer | O(n) | O(1) |
| Remove Duplicates | Set | O(n) | O(n) |
| Second Largest | Sort unique | O(n log n) | O(n) |
| Rotate | Slicing | O(n) | O(n) |
| Merge | `+` | O(n+m) | O(n+m) |
| Frequency | Counter | O(n) | O(n) |
| Move Zeros | Two-pointer | O(n) | O(1) |
| Find Missing | Math | O(n) | O(1) |
| Intersection | Set & | O(n+m) | O(n) |
| Pairs | Hash set | O(n) | O(n) |
| Max Subarray | Kadane's | O(n) | O(1) |
| Flatten | List comp | O(n) | O(n) |

---

## 🎓 KEY PATTERNS

1. **Accumulator**: Sum, frequency, count
2. **Two-pointer**: Reverse, pairs, zeros
3. **Hash lookup**: Duplicates, intersection, pairs
4. **Sorting**: Second largest, two-pointer
5. **Dynamic Programming**: Kadane's algorithm

---

## ⚠️ COMMON MISTAKES

1. Empty lists, single elements, duplicates
2. Inefficient nested loops (use hash sets)
3. Modifying list while iterating
4. Not using built-in functions
5. Off-by-one errors in slicing
6. Index out of bounds
7. Ignoring time/space complexity
🧠 Practice — Lists (15 Questions)
🔹 Basic

Q1 Take list input and print sum
Q2 Find max and min in list
Q3 Count even and odd numbers
Q4 Reverse list (without built-in)
Q5 Remove duplicates

🔹 Medium

Q6 Find second largest number
Q7 Rotate list by k steps
Q8 Merge two lists
Q9 Find frequency of each element
Q10 Move all zeros to end

🔹 Advanced Thinking

Q11 Find missing number in range
Q12 Find intersection of two lists
Q13 Find pairs with given sum
Q14 Kadane’s Algorithm (max subarray sum)
Q15 Flatten a 2D list