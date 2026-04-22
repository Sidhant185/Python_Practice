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

---

---

# 🧵 Python Practice — Strings (10 Questions)

A comprehensive guide to string manipulation, parsing, and advanced string operations.

---

## 🎯 SECTION 1: BASIC STRING OPERATIONS

### Q16: Reverse a String
**Problem:** Reverse a given string without using built-in reverse functions.

**Example:**
```
Input: "Hello"
Output: "olleH"

Input: "Python"
Output: "nohtyP"
```

**What to Use:**
- String slicing: `str[::-1]` (simplest)
- Loop with index from end to start
- Recursion (for learning)

**What NOT to Use:**
- ❌ Don't use `.reverse()` (works on lists, not strings)
- ❌ Don't manually build character by character inefficiently

**Concepts:**
- String indexing
- String slicing
- Iteration in reverse

**Solution Approach:**
```python
# BEST (String slicing):
text = "Hello"
reversed_text = text[::-1]
print(reversed_text)  # olleH

# GOOD (Loop with index):
text = "Hello"
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print(reversed_text)

# GOOD (Using reversed() function):
text = "Hello"
reversed_text = "".join(reversed(text))
print(reversed_text)
```

**Key Points:**
- Slicing `[::-1]` is most Pythonic
- Start from end, go backwards with step -1
- String concatenation in loops is slow; use `join()`

---

### Q17: Check Palindrome String
**Problem:** Check if a string is a palindrome (reads same forwards and backwards).

**Example:**
```
Input: "racecar"
Output: Palindrome

Input: "hello"
Output: Not a Palindrome

Input: "A man a plan a canal Panama"
Output: Palindrome (ignoring spaces and case)
```

**What to Use:**
- Compare string with its reverse
- Remove spaces and convert to lowercase
- Two-pointer approach

**What NOT to Use:**
- ❌ Don't forget to handle spaces and case sensitivity
- ❌ Don't hardcode checks for each character

**Concepts:**
- String comparison
- String transformation
- Case handling

**Solution Approach:**
```python
# SIMPLE (Compare with reverse):
text = "racecar"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# GOOD (Ignoring spaces and case):
text = "A man a plan a canal Panama"
cleaned = text.lower().replace(" ", "")
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# WITH INPUT:
text = input("Enter text: ")
cleaned = "".join(text.lower().split())
is_palindrome = cleaned == cleaned[::-1]
print("Palindrome" if is_palindrome else "Not a Palindrome")

# TWO-POINTER (For learning):
text = "racecar"
left, right = 0, len(text) - 1
is_palindrome = True
while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print("Palindrome" if is_palindrome else "Not a Palindrome")
```

**Key Points:**
- Remove spaces with `.replace(" ", "")` or `.split()`
- Convert to lowercase for case-insensitive comparison
- Two-pointer is more efficient for very long strings

---

### Q18: Count Vowels and Consonants
**Problem:** Count the number of vowels and consonants in a string.

**Example:**
```
Input: "Hello World"
Output:
Vowels: 3 (e, o, o)
Consonants: 7 (H, l, l, W, r, l, d)
```

**What to Use:**
- Loop through string
- Check if character is vowel using `in` operator
- `isalpha()` to check if character is letter

**What NOT to Use:**
- ❌ Don't count spaces as consonants
- ❌ Don't forget case-insensitivity

**Concepts:**
- Character checking
- String iteration
- Membership testing with `in`

**Solution Approach:**
```python
# GOOD (Loop approach):
text = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

# ELEGANT (List comprehension):
text = "Hello World"
vowels = "aeiou"
vowel_count = sum(1 for char in text.lower() if char in vowels)
consonant_count = sum(1 for char in text if char.isalpha() and char.lower() not in vowels)

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
```

**Key Points:**
- Use `.isalpha()` to check if character is a letter
- Convert to lowercase for comparison
- Ignore spaces, numbers, and special characters

---

### Q19: Remove Spaces
**Problem:** Remove all spaces from a string.

**Example:**
```
Input: "Hello World Python"
Output: "HelloWorldPython"
```

**What to Use:**
- `replace()` method: `str.replace(" ", "")`
- List comprehension with join
- `split()` and `join()`

**What NOT to Use:**
- ❌ Don't loop and manually build (inefficient)

**Concepts:**
- String replacement
- String splitting and joining

**Solution Approach:**
```python
# SIMPLEST (Using replace):
text = "Hello World Python"
result = text.replace(" ", "")
print(result)  # HelloWorldPython

# GOOD (Using split and join):
text = "Hello World Python"
result = "".join(text.split())
print(result)

# LIST COMPREHENSION:
text = "Hello World Python"
result = "".join(char for char in text if char != " ")
print(result)
```

**Key Points:**
- `replace()` is simplest and fastest
- `split()` without args removes all whitespace
- Remove all spaces vs. collapse multiple spaces

---

### Q20: Find Frequency of Characters
**Problem:** Count the frequency of each character in a string (ignoring spaces).

**Example:**
```
Input: "hello world"
Output:
h: 1
e: 1
l: 3
o: 2
w: 1
r: 1
d: 1
```

**What to Use:**
- Dictionary to store counts
- `collections.Counter` (Pythonic)
- Loop with `.get()` method

**What NOT to Use:**
- ❌ Don't count spaces
- ❌ Don't use nested loops for counting

**Concepts:**
- Dictionary/hash map
- Counter data structure
- Character frequency analysis

**Solution Approach:**
```python
# PYTHONIC (Using Counter):
from collections import Counter
text = "hello world"
frequency = Counter(char for char in text if char != " ")

for char, count in frequency.most_common():
    print(f"{char}: {count}")

# GOOD (Dictionary):
text = "hello world"
frequency = {}
for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

for char, count in frequency.items():
    print(f"{char}: {count}")

# SIMPLE (Manual dictionary):
text = "hello world"
frequency = {}
for char in text:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

for char, count in sorted(frequency.items()):
    print(f"{char}: {count}")
```

**Key Points:**
- Counter is built for this task
- `.get(key, default)` for safe dictionary access
- Ignore spaces and special characters
- `.most_common()` gives sorted by frequency

---

## 🔧 SECTION 2: INTERMEDIATE STRING OPERATIONS

### Q21: Check Anagram
**Problem:** Check if two strings are anagrams (contain same characters in different order).

**Example:**
```
Input: "listen", "silent"
Output: Anagram

Input: "hello", "world"
Output: Not an Anagram
```

**What to Use:**
- Sort and compare: `sorted(str1) == sorted(str2)`
- Use Counter and compare
- Character frequency comparison

**What NOT to Use:**
- ❌ Don't check character by character manually
- ❌ Don't forget to ignore case and spaces

**Concepts:**
- Character sorting
- Frequency comparison
- Case normalization

**Solution Approach:**
```python
# BEST (Sort approach):
str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an Anagram")

# GOOD (Using Counter):
from collections import Counter
str1 = "listen"
str2 = "silent"

if Counter(str1) == Counter(str2):
    print("Anagram")
else:
    print("Not an Anagram")

# WITH SPACES AND CASE (Ignoring them):
str1 = "The Eyes"
str2 = "They See"

cleaned1 = "".join(str1.lower().split())
cleaned2 = "".join(str2.lower().split())

if sorted(cleaned1) == sorted(cleaned2):
    print("Anagram")
else:
    print("Not an Anagram")
```

**Key Points:**
- Sorting is O(n log n) but simple
- Counter is O(n) and intuitive
- Remove spaces and convert to lowercase
- Check length first for optimization

---

### Q22: First Non-Repeating Character
**Problem:** Find the first character that appears only once in the string.

**Example:**
```
Input: "leetcode"
Output: 'l'

Input: "loveleetcode"
Output: 'v'

Input: "aabb"
Output: None (or "No unique character")
```

**What to Use:**
- Dictionary to store frequencies
- Counter for counting
- Loop through string to find first unique

**What NOT to Use:**
- ❌ Don't check each character with `.count()` (inefficient)

**Concepts:**
- Frequency tracking
- Ordered iteration
- Hash map lookup

**Solution Approach:**
```python
# GOOD (Dictionary approach):
text = "leetcode"
frequency = {}

# Count frequencies
for char in text:
    frequency[char] = frequency.get(char, 0) + 1

# Find first non-repeating
for char in text:
    if frequency[char] == 1:
        print(f"First non-repeating: {char}")
        break
else:
    print("No unique character")

# PYTHONIC (Using Counter):
from collections import Counter
text = "leetcode"
frequency = Counter(text)

for char in text:
    if frequency[char] == 1:
        print(f"First non-repeating: {char}")
        break
else:
    print("No unique character")

# ONE-LINER:
text = "leetcode"
result = next((c for c in text if text.count(c) == 1), None)
print(result or "No unique character")
```

**Key Points:**
- Count frequencies first
- Iterate original string to preserve order
- Use dictionary for O(1) lookup
- Handle case when no unique character exists

---

### Q23: Longest Word in Sentence
**Problem:** Find the longest word in a sentence.

**Example:**
```
Input: "The quick brown fox jumps"
Output: "quick" (or "brown") - 5 characters

Input: "Python programming is fun"
Output: "programming" - 11 characters
```

**What to Use:**
- `split()` to get words
- `max()` with key parameter
- Loop to track longest

**What NOT to Use:**
- ❌ Don't hardcode word lengths
- ❌ Don't include punctuation

**Concepts:**
- String splitting
- Key-based comparison
- String length

**Solution Approach:**
```python
# SIMPLEST (Using max):
sentence = "The quick brown fox jumps"
words = sentence.split()
longest = max(words, key=len)
print(f"Longest word: {longest}")

# GOOD (Loop approach):
sentence = "The quick brown fox jumps"
words = sentence.split()
longest = ""
max_length = 0

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest = word

print(f"Longest word: {longest}")

# WITH LENGTH:
sentence = "The quick brown fox jumps"
words = sentence.split()
longest = max(words, key=len)
print(f"Longest word: {longest} ({len(longest)} characters)")

# REMOVING PUNCTUATION:
import string
sentence = "The quick brown fox jumps!"
words = sentence.translate(str.maketrans('', '', string.punctuation)).split()
longest = max(words, key=len)
print(f"Longest word: {longest}")
```

**Key Points:**
- `split()` without args removes all whitespace
- `max(items, key=len)` finds longest by length
- Remove punctuation for accurate comparison
- Handle empty input

---

### Q24: Capitalize First Letter of Each Word
**Problem:** Capitalize the first letter of each word in a string.

**Example:**
```
Input: "hello world python"
Output: "Hello World Python"

Input: "the quick brown fox"
Output: "The Quick Brown Fox"
```

**What to Use:**
- `title()` method (built-in)
- List comprehension with capitalize
- Loop through words

**What NOT to Use:**
- ❌ Don't manually handle each character

**Concepts:**
- String methods
- Word iteration
- Case transformation

**Solution Approach:**
```python
# SIMPLEST (Using title):
text = "hello world python"
result = text.title()
print(result)  # Hello World Python

# GOOD (Using capitalize):
text = "hello world python"
words = text.split()
result = " ".join(word.capitalize() for word in words)
print(result)

# MANUAL APPROACH:
text = "hello world python"
result = ""
capitalize_next = True

for char in text:
    if char == " ":
        result += char
        capitalize_next = True
    elif capitalize_next:
        result += char.upper()
        capitalize_next = False
    else:
        result += char

print(result)

# CASE-SENSITIVE (title can have issues):
text = "iPhone and iPad"
result = " ".join(word[0].upper() + word[1:] for word in text.split())
print(result)  # IPhone And IPad
```

**Key Points:**
- `.title()` is simplest but treats apostrophes oddly
- `.capitalize()` only capitalizes first character of word
- `.upper()` converts entire string to uppercase
- Manual loop for custom capitalization rules

---

### Q25: Remove Duplicates from String
**Problem:** Remove duplicate characters from a string while maintaining order.

**Example:**
```
Input: "programming"
Output: "progamin"

Input: "aabbccdd"
Output: "abcd"
```

**What to Use:**
- Dictionary/set to track seen characters
- List and maintain order
- `dict.fromkeys()` (Python 3.7+)

**What NOT to Use:**
- ❌ Don't use set conversion (loses order)
- ❌ Don't use nested loops

**Concepts:**
- Order preservation
- Set operations
- Hash map for tracking

**Solution Approach:**
```python
# GOOD (Using dict and order):
text = "programming"
seen = set()
result = ""

for char in text:
    if char not in seen:
        result += char
        seen.add(char)

print(result)  # progamin

# PYTHONIC (dict.fromkeys - Python 3.7+):
text = "programming"
result = "".join(dict.fromkeys(text))
print(result)  # progamin

# LIST COMPREHENSION (With tracking):
text = "programming"
seen = set()
result = "".join(char for char in text if not (char in seen or seen.add(char)))
print(result)

# ALTERNATIVE (Using list):
text = "programming"
result = []
for char in text:
    if char not in result:
        result.append(char)
print("".join(result))
```

**Key Points:**
- Track seen characters in a set for O(1) lookup
- Check membership before adding
- `dict.fromkeys()` preserves insertion order (Python 3.7+)
- Remove `not in result` is O(n) for lists

---

## 📊 QUICK REFERENCE - STRINGS

| Problem | Best Approach | Time | Space |
|---------|---------------|------|-------|
| **Reverse** | Slicing `[::-1]` | O(n) | O(n) |
| **Palindrome** | Compare with reverse | O(n) | O(n) |
| **Vowel/Consonant Count** | Loop with `in` | O(n) | O(1) |
| **Remove Spaces** | `replace()` | O(n) | O(n) |
| **Frequency** | Counter | O(n) | O(k) |
| **Anagram** | Sort and compare | O(n log n) | O(n) |
| **First Unique** | Dict + loop | O(n) | O(k) |
| **Longest Word** | `max()` with key | O(n) | O(n) |
| **Capitalize** | `title()` | O(n) | O(n) |
| **Remove Duplicates** | Dict + order | O(n) | O(k) |

---

## 🎓 KEY STRING CONCEPTS

### String Methods
- `.upper()`, `.lower()` - Case conversion
- `.replace()` - Replace substring
- `.split()` - Split into list
- `.join()` - Combine list to string
- `.strip()` - Remove leading/trailing whitespace
- `.isalpha()`, `.isdigit()` - Character checks

### String Operations
- Slicing: `str[start:end:step]`
- Concatenation: `str1 + str2`
- Repetition: `str * n`
- Membership: `char in str`
- Length: `len(str)`

### Common Patterns
1. **Frequency Counting** - Use Counter or dict
2. **Character Validation** - Use `in` with strings
3. **Word Processing** - `split()` and iterate
4. **String Building** - Use `join()` not `+`
5. **Order Preservation** - Track with dict/set

---

## ⚠️ COMMON STRING MISTAKES

1. **Using `+` in loops** - O(n²) complexity; use `join()`
2. **Forgetting `.lower()` for comparisons** - Case sensitivity issues
3. **Not handling spaces** - `split()` vs `replace()`
4. **Checking membership with `.count()`** - Use `in` instead
5. **Modifying string in loop** - Strings are immutable; build new string
6. **Losing order with sets** - Use dict/set with order tracking
7. **Not stripping input** - Use `.strip()` for user input
8. **Inefficient character checking** - Use `in` with strings, not loops
9. **Assuming ASCII only** - Unicode characters behave differently
10. **Not considering edge cases** - Empty strings, single character, special chars

---

## 💡 PROGRESSION PATH

1. **Basic Operations** (Q16-Q20): Reversal, palindrome, vowel/consonant, spaces, frequency
2. **Intermediate** (Q21-Q25): Anagrams, unique chars, longest word, capitalization, deduplication

Start with basic string operations and progress to more complex manipulations!
