"""
list_comprehension_example.py

A beginner-friendly tutorial on Python list comprehensions.

List comprehensions are a concise way to create lists in Python.
They're more readable and often faster than equivalent for loops.
"""

# ============================================================================
# 1. BASIC LIST COMPREHENSION
# ============================================================================

print("=" * 60)
print("1. BASIC LIST COMPREHENSION")
print("=" * 60)

# Traditional way with a for loop:
numbers = []
for i in range(5):
    numbers.append(i * 2)
print(f"Traditional way: {numbers}")

# List comprehension way (much more concise!):
numbers = [i * 2 for i in range(5)]
print(f"List comprehension: {numbers}")

# Syntax: [expression for item in iterable]
# - expression: what to do with each item (i * 2)
# - item: the variable name (i)
# - iterable: what to iterate over (range(5))


# ============================================================================
# 2. LIST COMPREHENSION WITH STRINGS
# ============================================================================

print("\n" + "=" * 60)
print("2. LIST COMPREHENSION WITH STRINGS")
print("=" * 60)

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Original: {words}")
print(f"Uppercase: {upper_words}")

# Get the length of each word
word_lengths = [len(word) for word in words]
print(f"Word lengths: {word_lengths}")


# ============================================================================
# 3. LIST COMPREHENSION WITH CONDITIONAL FILTERING
# ============================================================================

print("\n" + "=" * 60)
print("3. LIST COMPREHENSION WITH CONDITIONAL FILTERING")
print("=" * 60)

# Traditional way: filter even numbers
numbers = list(range(10))
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Traditional way (even numbers): {even_numbers}")

# List comprehension way:
even_numbers = [num for num in range(10) if num % 2 == 0]
print(f"List comprehension (even numbers): {even_numbers}")

# Syntax: [expression for item in iterable if condition]
# Only items that satisfy the condition are included


# ============================================================================
# 4. CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
# ============================================================================

print("\n" + "=" * 60)
print("4. CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)")
print("=" * 60)

# Transform values based on a condition
numbers = list(range(10))
# If number is even, keep it; if odd, multiply by 10
transformed = [num if num % 2 == 0 else num * 10 for num in numbers]
print(f"Original: {numbers}")
print(f"Transformed (even stays, odd * 10): {transformed}")

# Syntax: [value_if_true if condition else value_if_false for item in iterable]


# ============================================================================
# 5. NESTED LIST COMPREHENSIONS
# ============================================================================

print("\n" + "=" * 60)
print("5. NESTED LIST COMPREHENSIONS")
print("=" * 60)

# Create a multiplication table (2D list)
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication table (5x5):")
for row in multiplication_table:
    print(row)

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"\nOriginal matrix: {matrix}")
print(f"Flattened: {flattened}")

# Read nested comprehensions from left to right:
# [num for row in matrix for num in row]
# means: for each row in matrix, for each num in row, include num


# ============================================================================
# 6. PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("6. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Extract numbers from a string
text = "I have 3 cats and 2 dogs"
numbers = [int(char) for char in text if char.isdigit()]
print(f"Text: '{text}'")
print(f"Numbers found: {numbers}")

# Example 2: Square only positive numbers
numbers = [-2, -1, 0, 1, 2, 3, 4]
squared_positives = [num ** 2 for num in numbers if num > 0]
print(f"\nOriginal: {numbers}")
print(f"Squared positives: {squared_positives}")

# Example 3: Create a list of tuples
names = ["Alice", "Bob", "Charlie"]
name_lengths = [(name, len(name)) for name in names]
print(f"\nNames: {names}")
print(f"Name-length pairs: {name_lengths}")

# Example 4: Filter and transform
temperatures = [20, 25, 30, 15, 35, 10]
hot_days = [f"{temp}°C" for temp in temperatures if temp >= 25]
print(f"\nTemperatures: {temperatures}")
print(f"Hot days (>=25°C): {hot_days}")


# ============================================================================
# 7. COMPARISON: FOR LOOP vs LIST COMPREHENSION
# ============================================================================

print("\n" + "=" * 60)
print("7. COMPARISON: FOR LOOP vs LIST COMPREHENSION")
print("=" * 60)

# Task: Get squares of even numbers from 0 to 9

# Method 1: Traditional for loop
result1 = []
for num in range(10):
    if num % 2 == 0:
        result1.append(num ** 2)
print(f"For loop: {result1}")

# Method 2: List comprehension (more Pythonic!)
result2 = [num ** 2 for num in range(10) if num % 2 == 0]
print(f"List comprehension: {result2}")

# Both produce the same result, but list comprehension is:
# - More concise (one line vs multiple lines)
# - More readable (once you understand the syntax)
# - Often faster (Python optimizes list comprehensions)


# ============================================================================
# 8. COMMON PATTERNS AND TIPS
# ============================================================================

print("\n" + "=" * 60)
print("8. COMMON PATTERNS AND TIPS")
print("=" * 60)

# Pattern 1: Simple transformation
original = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in original]
print(f"Doubled: {doubled}")

# Pattern 2: Filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Pattern 3: Filter and transform
words = ["python", "java", "c++", "javascript", "go"]
long_words = [word.upper() for word in words if len(word) > 4]
print(f"Long words (uppercase): {long_words}")

# Pattern 4: Multiple conditions
numbers = list(range(20))
filtered = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(f"Numbers divisible by both 2 and 3: {filtered}")

# Tip: If your list comprehension gets too complex, consider using a for loop
# Readability is more important than brevity!


# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
List Comprehension Syntax:
  [expression for item in iterable]
  [expression for item in iterable if condition]
  [value_if_true if condition else value_if_false for item in iterable]

Key Points:
  1. List comprehensions create new lists
  2. They're more concise than for loops
  3. They're often faster than equivalent for loops
  4. Use them when the logic is simple and readable
  5. If it gets too complex, use a regular for loop instead

Remember: Readability counts! Don't sacrifice clarity for brevity.
""")

