# 🧠 Python Practice - Complete Guide (50 Questions)

---

## 🎯 SECTION 1: BASIC INPUT/OUTPUT & CONDITIONALS

### Q1: Greet with Name
**Problem:** Take a person's name as input and print a greeting message.

**Example:**
```
Input: John
Output: Hello, John!
```

**What to Use:**
- `input()` function to take user input
- `print()` function with f-strings for formatting
- String concatenation or f-strings

**What NOT to Use:**
- ❌ Don't use `eval()` on user input
- ❌ Don't forget to convert input types when needed
- ❌ Don't hardcode names

**Concepts:**
- Input/Output operations
- String manipulation
- Basic variables

**Solution Approach:**
```python
# GOOD:
name = input("Enter your name: ")
print(f"Hello, {name}!")

# ALSO GOOD:
name = input()
greeting = f"Hello, {name}!"
print(greeting)
```

---

### Q2: Sum and Product of Two Numbers
**Problem:** Take two numbers as input and calculate their sum and product.

**Example:**
```
Input: 5, 3
Output:
Sum: 8
Product: 15
```

**What to Use:**
- `input()` to get numbers
- `int()` or `float()` to convert strings to numbers
- Arithmetic operators: `+` and `*`
- f-strings for formatted output

**What NOT to Use:**
- ❌ Don't mix string and integer without conversion
- ❌ Don't use `eval()` for user input
- ❌ Don't assume input is always valid

**Concepts:**
- Type conversion
- Arithmetic operations
- Variable storage

**Solution Approach:**
```python
# GOOD:
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print(f"Sum: {num1 + num2}")
print(f"Product: {num1 * num2}")

# ALTERNATIVE:
num1, num2 = int(input()), int(input())
sum_result = num1 + num2
product_result = num1 * num2
print(f"Sum: {sum_result}, Product: {product_result}")
```

---

### Q3: Adult or Minor Classification
**Problem:** Take age as input and print whether the person is an adult (≥18) or minor.

**Example:**
```
Input: 25
Output: Adult

Input: 15
Output: Minor
```

**What to Use:**
- `if-else` conditional statements
- Comparison operators: `>=`, `<`
- `int()` for type conversion

**What NOT to Use:**
- ❌ Don't use multiple unnecessary if statements
- ❌ Don't use nested ifs when simple if-else works
- ❌ Don't forget to convert input to integer

**Concepts:**
- Boolean conditions
- Decision making
- Comparison operators

**Solution Approach:**
```python
# GOOD:
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# ALSO GOOD (Ternary):
age = int(input("Enter age: "))
status = "Adult" if age >= 18 else "Minor"
print(status)
```

---

### Q4: Square and Cube
**Problem:** Take a number and print its square and cube.

**Example:**
```
Input: 5
Output:
Square: 25
Cube: 125
```

**What to Use:**
- Exponentiation operator: `**`
- Or `pow()` function
- `int()` for conversion

**What NOT to Use:**
- ❌ Don't multiply the number 3 times manually
- ❌ Don't use math.pow() unnecessarily (** is better)

**Concepts:**
- Exponentiation
- Mathematical operations

**Solution Approach:**
```python
# GOOD:
num = int(input("Enter number: "))
print(f"Square: {num ** 2}")
print(f"Cube: {num ** 3}")

# ALTERNATIVE:
num = int(input())
square = pow(num, 2)
cube = pow(num, 3)
print(f"Square: {square}\nCube: {cube}")
```

---

### Q5: Even or Odd
**Problem:** Check if a number is even or odd.

**Example:**
```
Input: 7
Output: Odd

Input: 12
Output: Even
```

**What to Use:**
- Modulo operator: `%`
- `if-else` statement
- Comparison with 0

**What NOT to Use:**
- ❌ Don't use division and check remainder manually
- ❌ Don't use complex logic

**Concepts:**
- Modulo operator
- Remainder calculation
- Conditional logic

**Solution Approach:**
```python
# GOOD:
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# ALTERNATIVE (One-liner):
num = int(input())
print("Even" if num % 2 == 0 else "Odd")
```

---

### Q6: Positive, Negative, or Zero
**Problem:** Check if a number is positive, negative, or zero.

**Example:**
```
Input: -5
Output: Negative

Input: 0
Output: Zero

Input: 10
Output: Positive
```

**What to Use:**
- `if-elif-else` for multiple conditions
- Comparison operators: `>`, `<`, `==`

**What NOT to Use:**
- ❌ Don't use nested ifs when elif works
- ❌ Don't check conditions out of logical order

**Concepts:**
- Multiple conditions
- Elif statements
- Logical flow

**Solution Approach:**
```python
# GOOD:
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

---

### Q7: Age Category
**Problem:** Categorize age into Child (<13), Teen (13-19), or Adult (≥20).

**Example:**
```
Input: 10
Output: Child

Input: 15
Output: Teen

Input: 25
Output: Adult
```

**What to Use:**
- `if-elif-else` statements
- Range checking with `and` operator
- Proper boundary conditions

**What NOT to Use:**
- ❌ Don't use overlapping conditions
- ❌ Don't forget boundary values (13, 19, 20)

**Concepts:**
- Range validation
- Logical AND
- Multiple conditions

**Solution Approach:**
```python
# GOOD:
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age <= 19:  # 13 to 19
    print("Teen")
else:  # 20+
    print("Adult")

# ALTERNATIVE:
age = int(input())
if age < 13:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teen"
else:
    category = "Adult"
print(category)
```

---

### Q8: Maximum of Three Numbers
**Problem:** Find and print the largest of three numbers.

**Example:**
```
Input: 5, 8, 3
Output: 8
```

**What to Use:**
- `max()` built-in function (RECOMMENDED)
- `if-elif-else` for manual comparison
- Nested conditions for logical comparison

**What NOT to Use:**
- ❌ Don't manually check each pair multiple times
- ❌ Avoid unnecessary complexity

**Concepts:**
- Comparison logic
- Built-in functions
- Nested conditions

**Solution Approach:**
```python
# BEST (Using max()):
a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))

# GOOD (Manual approach):
a, b, c = int(input()), int(input()), int(input())
if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)
```

---

### Q9: Divisibility Check
**Problem:** Check if a number is divisible by both 5 and 3.

**Example:**
```
Input: 15
Output: Yes, divisible by both 5 and 3

Input: 10
Output: No
```

**What to Use:**
- Modulo operator: `%`
- Logical AND operator: `and`
- Comparison with 0

**What NOT to Use:**
- ❌ Don't use `or` when you mean `and`
- ❌ Don't check conditions separately without combining

**Concepts:**
- Divisibility check
- Logical operators
- Multiple conditions

**Solution Approach:**
```python
# GOOD:
num = int(input("Enter number: "))
if num % 5 == 0 and num % 3 == 0:
    print("Yes, divisible by both")
else:
    print("No")

# ALTERNATIVE:
num = int(input())
if num % 15 == 0:  # If divisible by both 3 and 5, then by 15
    print("Yes")
else:
    print("No")
```

---

### Q10: Grade Assignment
**Problem:** Take marks (0-100) and assign a grade (A, B, C, Fail).

**Example:**
```
Input: 85
Output: A

Input: 72
Output: B

Input: 35
Output: Fail
```

**What to Use:**
- `if-elif-else` statements
- Range checking
- Proper boundaries (e.g., 90-100 for A)

**What NOT to Use:**
- ❌ Don't hardcode marks (use ranges)
- ❌ Don't have overlapping ranges

**Concepts:**
- Range-based conditions
- Grading logic

**Typical Grade Scale:**
- A: 90-100
- B: 80-89
- C: 70-79
- Fail: 0-69

**Solution Approach:**
```python
# GOOD:
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("Fail")
```

---

### Q11: Leap Year Check
**Problem:** Check if a year is a leap year.

**Rules:**
- Divisible by 4 → Leap Year
- BUT if divisible by 100 → NOT leap year
- BUT if divisible by 400 → IS leap year

**Example:**
```
Input: 2024
Output: Leap Year

Input: 1900
Output: Not a Leap Year

Input: 2000
Output: Leap Year
```

**What to Use:**
- `if-elif-else` statements
- Modulo operator: `%`
- Proper order of conditions (check 400 first!)

**What NOT to Use:**
- ❌ Don't reverse the condition order
- ❌ Don't miss the 400 rule

**Solution Approach:**
```python
# GOOD (Correct order):
year = int(input("Enter year: "))
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

# ALTERNATIVE (Compact):
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

---

### Q12: Vowel or Consonant
**Problem:** Check if a character is a vowel or consonant.

**Example:**
```
Input: a
Output: Vowel

Input: b
Output: Consonant
```

**What to Use:**
- String methods: `.lower()` for case-insensitivity
- `in` operator for checking vowels
- List or string of vowels

**What NOT to Use:**
- ❌ Don't hardcode multiple if statements for each letter
- ❌ Don't forget uppercase/lowercase variations

**Concepts:**
- String operations
- Membership checking with `in`
- Case normalization

**Solution Approach:**
```python
# GOOD:
char = input("Enter character: ").lower()
if char in "aeiou":
    print("Vowel")
elif char.isalpha():
    print("Consonant")
else:
    print("Not a letter")

# ALTERNATIVE:
vowels = ['a', 'e', 'i', 'o', 'u']
char = input().lower()
if char in vowels:
    print("Vowel")
else:
    print("Consonant")
```

---

### Q13: Valid Triangle Check
**Problem:** Check if three given sides can form a valid triangle.

**Rule:** The sum of any two sides must be greater than the third side.

**Example:**
```
Input: 3, 4, 5
Output: Valid Triangle

Input: 1, 2, 5
Output: Invalid Triangle
```

**What to Use:**
- Triangle inequality theorem
- `and` operator for combining conditions
- Three separate checks

**What NOT to Use:**
- ❌ Don't miss any side combination
- ❌ Don't use `>=` instead of `>`

**Solution Approach:**
```python
# GOOD:
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if (a + b > c) and (b + c > a) and (a + c > b):
    print("Valid Triangle")
else:
    print("Invalid Triangle")

# ALTERNATIVE:
sides = sorted([a, b, c])
if sides[0] + sides[1] > sides[2]:
    print("Valid")
else:
    print("Invalid")
```

---

### Q14: Even AND Divisible by 3
**Problem:** Check if a number is both even AND divisible by 3.

**Example:**
```
Input: 12
Output: Yes

Input: 8
Output: No
```

**What to Use:**
- Modulo operator: `%`
- Logical AND operator: `and`

**What NOT to Use:**
- ❌ Don't use `or` instead of `and`

**Solution Approach:**
```python
# GOOD:
num = int(input())
if num % 2 == 0 and num % 3 == 0:
    print("Yes")
else:
    print("No")

# ALTERNATIVE:
if num % 6 == 0:  # Divisible by both 2 and 3
    print("Yes")
```

---

### Q15: Simple Calculator
**Problem:** Create a simple calculator that performs arithmetic operations (+, -, *, /).

**Example:**
```
Input: +, 10, 5
Output: 15

Input: *, 4, 3
Output: 12
```

**What to Use:**
- `if-elif-else` for operator selection
- Proper type conversion
- Handle division by zero

**What NOT to Use:**
- ❌ Don't forget to convert inputs to numbers
- ❌ Don't forget to handle division by zero
- ❌ Don't use `eval()`

**Solution Approach:**
```python
# GOOD:
operator = input("Enter operator (+, -, *, /): ")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator")
```

---

## 🔁 SECTION 2: LOOPS & ITERATIONS

### Q16: Print Numbers 1-100
**Problem:** Print all numbers from 1 to 100.

**Example:**
```
Output:
1
2
3
...
100
```

**What to Use:**
- `for` loop with `range()`
- `range(1, 101)` for 1 to 100 inclusive

**What NOT to Use:**
- ❌ Don't manually hardcode numbers
- ❌ Don't start from 0 and go to 99

**Concepts:**
- For loops
- Range function

**Solution Approach:**
```python
# GOOD:
for i in range(1, 101):
    print(i)

# ALTERNATIVE:
for i in range(100):
    print(i + 1)
```

---

### Q17: Print Even Numbers 1-100
**Problem:** Print only even numbers from 1 to 100.

**Example:**
```
Output:
2
4
6
...
100
```

**What to Use:**
- `for` loop with step parameter: `range(2, 101, 2)`
- OR check with modulo inside loop

**What NOT to Use:**
- ❌ Don't hardcode all even numbers

**Concepts:**
- Range with step
- Loop optimization

**Solution Approach:**
```python
# BEST (Using step):
for i in range(2, 101, 2):
    print(i)

# GOOD (Using modulo):
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
```

---

### Q18: Sum of Numbers 1 to N
**Problem:** Calculate the sum of all numbers from 1 to n.

**Example:**
```
Input: 10
Output: 55
```

**What to Use:**
- `for` loop with accumulator
- `sum()` built-in function
- Mathematical formula: n*(n+1)/2

**What NOT to Use:**
- ❌ Don't manually add all numbers

**Concepts:**
- Accumulator pattern
- Mathematical optimization

**Solution Approach:**
```python
# GOOD (Loop):
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print(total)

# BEST (Formula):
n = int(input())
print(n * (n + 1) // 2)
```

---

### Q19: Factorial of a Number
**Problem:** Calculate the factorial of a number (n! = n × (n-1) × ... × 1).

**Example:**
```
Input: 5
Output: 120
```

**What to Use:**
- `for` loop with accumulator
- Multiplication in loop
- Handle edge case: 0! = 1

**Solution Approach:**
```python
# GOOD:
n = int(input("Enter number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# ALTERNATIVE (Using math library):
import math
print(math.factorial(n))
```

---

### Q20: Reverse a Number
**Problem:** Reverse the digits of a number (e.g., 123 → 321).

**Example:**
```
Input: 456
Output: 654
```

**What to Use:**
- `while` loop with modulo and division
- OR string slicing: `str(num)[::-1]`

**Solution Approach:**
```python
# GOOD (Mathematical):
num = int(input("Enter number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(reversed_num)

# SIMPLE (String):
num = int(input())
print(int(str(num)[::-1]))
```

---

### Q21: Count Digits
**Problem:** Count the total number of digits in a number.

**Example:**
```
Input: 12345
Output: 5 digits
```

**What to Use:**
- `while` loop with division
- OR string length: `len(str(num))`

**Solution Approach:**
```python
# GOOD (Mathematical):
num = int(input())
count = 0
while num > 0:
    count += 1
    num //= 10
print(f"Number of digits: {count}")

# SIMPLE (String):
num = input()
print(f"Number of digits: {len(num)}")
```

---

### Q22: Sum of Digits
**Problem:** Calculate the sum of all digits in a number.

**Example:**
```
Input: 123
Output: 6
```

**What to Use:**
- `while` loop with modulo
- OR string iteration
- Accumulator variable

**Solution Approach:**
```python
# GOOD (Mathematical):
num = int(input())
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num //= 10
print(f"Sum of digits: {digit_sum}")

# SIMPLE (String):
num = input()
print(sum(int(digit) for digit in num))
```

---

### Q23: Palindrome Number
**Problem:** Check if a number reads the same forwards and backwards.

**Example:**
```
Input: 121
Output: Palindrome

Input: 123
Output: Not a Palindrome
```

**What to Use:**
- Reverse the number and compare
- String comparison method

**Solution Approach:**
```python
# GOOD:
num = int(input())
original = num
reversed_num = 0

while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

if original == reversed_num:
    print("Palindrome")
else:
    print("Not a Palindrome")

# SIMPLE (String):
num_str = input()
if num_str == num_str[::-1]:
    print("Palindrome")
```

---

### Q24: Multiplication Table
**Problem:** Print the multiplication table of a number up to 10.

**Example:**
```
Input: 5
Output:
5 × 1 = 5
5 × 2 = 10
...
5 × 10 = 50
```

**What to Use:**
- `for` loop with range(1, 11)
- String formatting for output

**Solution Approach:**
```python
# GOOD:
num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")
```

---

### Q25: Fibonacci Series
**Problem:** Print the first n terms of the Fibonacci series (1, 1, 2, 3, 5, 8, ...).

**Example:**
```
Input: 7
Output: 1 1 2 3 5 8 13
```

**What to Use:**
- `for` loop to generate n terms
- Two variables to track previous numbers

**Solution Approach:**
```python
# GOOD:
n = int(input("Enter n: "))
a, b = 1, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# ALTERNATIVE:
n = int(input())
fib_list = [1, 1]
for i in range(2, n):
    fib_list.append(fib_list[i-1] + fib_list[i-2])
print(fib_list[:n])
```

---

## 🎨 SECTION 3: PATTERNS

### Q26: Increasing Star Pattern
**Problem:** Print a pattern of increasing stars.

```
Expected Output:
*
**
***
****
```

**What to Use:**
- Nested loops
- String multiplication: `"*" * n`

**Solution Approach:**
```python
# GOOD:
n = 4
for i in range(1, n + 1):
    print("*" * i)

# ALTERNATIVE:
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
```

---

### Q27: Decreasing Star Pattern
**Problem:** Print a pattern of decreasing stars.

```
Expected Output:
****
***
**
*
```

**What to Use:**
- Nested loops
- Reverse iteration

**Solution Approach:**
```python
# GOOD:
n = 4
for i in range(n, 0, -1):
    print("*" * i)
```

---

### Q28: Number Pattern
**Problem:** Print a pattern where each row contains numbers up to the row number.

```
Expected Output:
1
12
123
1234
```

**What to Use:**
- Nested loops
- String concatenation

**Solution Approach:**
```python
# GOOD:
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

---

## 🧮 SECTION 4: LOGIC HEAVY (PRIME, GCD, LCM)

### Q29: Prime Number Check
**Problem:** Check if a number is prime (divisible only by 1 and itself).

**Example:**
```
Input: 17
Output: Prime

Input: 20
Output: Not Prime
```

**What to Use:**
- `for` loop from 2 to sqrt(n)
- Modulo operator to check divisibility
- `break` to exit early

**What NOT to Use:**
- ❌ Don't check all numbers up to n
- ❌ Don't forget 2 is prime

**Concepts:**
- Prime numbers
- Optimization (sqrt rule)

**Solution Approach:**
```python
# GOOD:
num = int(input())
if num < 2:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "Not Prime")
```

---

### Q30: All Primes from 1-100
**Problem:** Print all prime numbers between 1 and 100.

**Expected Output:**
```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

**What to Use:**
- Sieve of Eratosthenes (efficient)
- Nested loops with prime checking

**Solution Approach:**
```python
# GOOD (Sieve of Eratosthenes):
is_prime = [True] * 101
is_prime[0] = is_prime[1] = False

for i in range(2, int(100 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 101, i):
            is_prime[j] = False

primes = [i for i in range(2, 101) if is_prime[i]]
print(primes)

# SIMPLE (Nested loops):
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
```

---

### Q31: GCD (Greatest Common Divisor)
**Problem:** Find the GCD of two numbers.

**Example:**
```
Input: 12, 8
Output: 4
```

**What to Use:**
- Euclidean algorithm
- `math.gcd()` built-in function

**Solution Approach:**
```python
# BEST (Using built-in):
import math
a = int(input())
b = int(input())
print(f"GCD: {math.gcd(a, b)}")

# GOOD (Euclidean algorithm):
a, b = int(input()), int(input())
while b:
    a, b = b, a % b
print(f"GCD: {a}")
```

---

### Q32: LCM (Least Common Multiple)
**Problem:** Find the LCM of two numbers.

**Formula:** LCM(a, b) = (a × b) / GCD(a, b)

**Example:**
```
Input: 12, 8
Output: 24
```

**What to Use:**
- GCD calculation first
- `math.lcm()` (Python 3.9+)

**Solution Approach:**
```python
# BEST (Using built-in - Python 3.9+):
import math
a, b = int(input()), int(input())
print(f"LCM: {math.lcm(a, b)}")

# GOOD (Using GCD):
import math
a, b = int(input()), int(input())
lcm = (a * b) // math.gcd(a, b)
print(f"LCM: {lcm}")
```

---

## 🔄 SECTION 5: LOOP CONTROL (BREAK, CONTINUE)

### Q33: Skip Multiples of 3
**Problem:** Print numbers 1-50 but skip all multiples of 3.

**Example:**
```
Output: 1 2 4 5 7 8 10 11 13 14 ...
```

**What to Use:**
- `for` loop from 1 to 50
- `continue` statement to skip
- Modulo operator

**Solution Approach:**
```python
# GOOD:
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i, end=" ")

# ALTERNATIVE:
for i in range(1, 51):
    if i % 3 != 0:
        print(i, end=" ")
```

---

### Q34: Stop Loop When Sum Exceeds 100
**Problem:** Keep adding numbers and stop when sum exceeds 100.

**Example:**
```
Output: Sum = 105
Numbers added: 14
```

**What to Use:**
- `while` loop
- Accumulator variable
- `break` statement

**Solution Approach:**
```python
# GOOD:
total = 0
num = 1
while True:
    total += num
    if total > 100:
        break
    num += 1
print(f"Total: {total}, Numbers added: {num}")
```

---

### Q35: Guessing Game
**Problem:** Create a number guessing game until correct.

**Example:**
```
I'm thinking of a number between 1-100.
Guess: 50
Too high!
Guess: 25
Too low!
Guess: 37
Correct!
```

**What to Use:**
- `while True` loop with `break`
- Comparison operators
- `random.randint()`

**Solution Approach:**
```python
# GOOD:
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    
    if guess == secret:
        print(f"Correct! You got it in {attempts} attempts!")
        break
    elif guess < secret:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
```

---

## 🎯 SECTION 6: FUNCTIONS - BASICS

### Q36: Function to Print Name
**Problem:** Create a function that takes a name and prints a greeting.

**Example:**
```
greet("Alice")
Output: Hello, Alice!
```

**What to Use:**
- `def` keyword to define function
- Parameter in function signature
- `print()` statement

**Solution Approach:**
```python
# GOOD:
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

# ALTERNATIVE (Return value):
def get_greeting(name):
    return f"Hello, {name}!"

print(get_greeting("Charlie"))
```

---

### Q37: Function to Add Two Numbers
**Problem:** Create a function that returns the sum of two numbers.

**Example:**
```
add(5, 3)
Output: 8
```

**What to Use:**
- `def` keyword
- Function parameters
- `return` statement

**Solution Approach:**
```python
# GOOD:
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

---

### Q38: Function to Check Even/Odd
**Problem:** Create a function that checks if a number is even or odd.

**Example:**
```
check_even_odd(7)
Output: Odd
```

**Solution Approach:**
```python
# GOOD:
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))
print(check_even_odd(10))
```

---

### Q39: Function to Find Max of 2 Numbers
**Problem:** Create a function that returns the maximum of two numbers.

**Example:**
```
max_of_two(15, 8)
Output: 15
```

**Solution Approach:**
```python
# GOOD:
def max_of_two(a, b):
    return a if a > b else b

print(max_of_two(15, 8))

# ALTERNATIVE:
def max_of_two(a, b):
    return max(a, b)
```

---

## 🧩 SECTION 7: FUNCTIONS - MEDIUM

### Q40: Function to Calculate Factorial
**Problem:** Create a function that calculates factorial.

**Solution Approach:**
```python
# GOOD (Iterative):
def factorial(n):
    if n < 0:
        return "Error: Negative number"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
```

---

### Q41: Function to Check Prime
**Problem:** Create a function that checks if a number is prime.

**Solution Approach:**
```python
# GOOD:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))
print(is_prime(20))
```

---

### Q42: Function to Reverse a Number
**Problem:** Create a function that reverses a number.

**Solution Approach:**
```python
# GOOD:
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return reversed_num

print(reverse_number(456))

# SIMPLE (String):
def reverse_number(num):
    return int(str(num)[::-1])
```

---

### Q43: Function to Count Digits
**Problem:** Create a function that counts digits in a number.

**Solution Approach:**
```python
# GOOD:
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

print(count_digits(12345))

# SIMPLE:
def count_digits(num):
    return len(str(abs(num)))
```

---

### Q44: Function to Sum of Digits
**Problem:** Create a function that calculates the sum of digits.

**Solution Approach:**
```python
# GOOD:
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

print(sum_of_digits(123))

# SIMPLE:
def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))
```

---

## 🚀 SECTION 8: FUNCTIONS - ADVANCED

### Q45: Function to Get Nth Fibonacci Term
**Problem:** Create a function that returns the nth term of Fibonacci.

**Example:**
```
fib(7)
Output: 13
```

**Solution Approach:**
```python
# GOOD (Iterative):
def fibonacci(n):
    if n <= 0:
        return "Error"
    elif n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

print(fibonacci(7))
```

---

### Q46: Function to Check Palindrome
**Problem:** Create a function that checks if a number is a palindrome.

**Solution Approach:**
```python
# GOOD:
def is_palindrome(num):
    original = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return original == reversed_num

print(is_palindrome(121))

# SIMPLE:
def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
```

---

### Q47: Function to Calculate GCD
**Problem:** Create a function that calculates GCD.

**Solution Approach:**
```python
# GOOD:
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(12, 8))

# USING BUILT-IN:
import math
def gcd(a, b):
    return math.gcd(a, b)
```

---

### Q48: Function to Calculate LCM
**Problem:** Create a function that calculates LCM.

**Solution Approach:**
```python
# GOOD:
import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

print(lcm(12, 8))
```

---

## 🏆 SECTION 9: ADVANCED FUNCTION LOGIC

### Q49: Function Returning List of Primes Till N
**Problem:** Create a function that returns all primes up to n.

**Example:**
```
get_primes(20)
Output: [2, 3, 5, 7, 11, 13, 17, 19]
```

**Solution Approach:**
```python
# GOOD (Sieve):
def get_primes(n):
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(2, n + 1) if is_prime[i]]

print(get_primes(20))
```

---

### Q50: Calculator Using Functions
**Problem:** Create a calculator using functions for each operation.

**Example:**
```
Input: +, 10, 5
Output: 15
```

**Solution Approach:**
```python
# GOOD:
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator(operator, a, b):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return subtract(a, b)
    elif operator == '*':
        return multiply(a, b)
    elif operator == '/':
        return divide(a, b)
    else:
        return "Invalid operator"

op = input("Operator: ")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
result = calculator(op, num1, num2)
print(f"Result: {result}")
```

---

## 📝 SUMMARY OF KEY CONCEPTS

| Concept | Questions | Key Points |
|---------|-----------|-----------|
| **Input/Output** | Q1-Q2 | Use `input()`, `print()`, f-strings |
| **Conditionals** | Q3-Q15 | `if-elif-else`, comparison operators |
| **For Loops** | Q16-Q25 | `range()`, loops, accumulation |
| **While Loops** | Q20, Q22, Q34 | Conditions, breaking, division/modulo |
| **Patterns** | Q26-Q28 | Nested loops, string multiplication |
| **Prime Numbers** | Q29-Q30 | Optimization, sqrt rule, Sieve |
| **GCD/LCM** | Q31-Q32 | Euclidean algorithm, formulas |
| **Break/Continue** | Q33-Q35 | Loop control, game logic |
| **Functions** | Q36-Q50 | Definition, parameters, return, logic |

---

## 🎓 PROGRESSION GUIDE

1. **Master Basics First** (Q1-Q15): Inputs, outputs, conditionals
2. **Learn Loops** (Q16-Q25): For/while loops, accumulation
3. **Practice Patterns** (Q26-Q28): Nested loops
4. **Tackle Math** (Q29-Q32): Prime checks, GCD, LCM
5. **Control Flow** (Q33-Q35): Break, continue, games
6. **Master Functions** (Q36-Q50): Reusability, logic

---

## ⚠️ COMMON MISTAKES TO AVOID

1. **Not converting input types** → Use `int()`, `float()`
2. **Forgetting loop increments** → Use `+=`, `//=`
3. **Off-by-one errors** → Check boundaries carefully
4. **Not handling edge cases** → 0, 1, negative numbers
5. **Using inefficient algorithms** → Optimize with sqrt, Sieve
6. **Not breaking early** → Use `break` in loops
7. **Forgetting to return** → Functions must `return` values
8. **Division by zero** → Always check if divisor is 0
9. **Hardcoding values** → Use parameters and variables
10. **Not reading carefully** → Understand all requirements first