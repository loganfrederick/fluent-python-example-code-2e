"""
generator_expressions.py

A tutorial on Python generator expressions.

Generator expressions are similar to list comprehensions, but they create
generator objects instead of lists. They're memory-efficient because they
generate values on-the-fly rather than storing them all in memory.
"""

# ============================================================================
# 1. BASIC GENERATOR EXPRESSION
# ============================================================================

print("=" * 60)
print("1. BASIC GENERATOR EXPRESSION")
print("=" * 60)

# List comprehension (creates a list):
numbers_list = [i * 2 for i in range(5)]
print(f"List comprehension: {numbers_list}")
print(f"Type: {type(numbers_list)}")

# Generator expression (creates a generator object):
numbers_gen = (i * 2 for i in range(5))
print(f"\nGenerator expression: {numbers_gen}")
print(f"Type: {type(numbers_gen)}")

# To get values from a generator, iterate over it:
print(f"Values from generator: {list(numbers_gen)}")

# Note: Once exhausted, generators can't be reused
print(f"After consuming: {list(numbers_gen)}")  # Empty!

# Syntax: (expression for item in iterable)
# - Uses parentheses () instead of square brackets []
# - Creates a generator object, not a list


# ============================================================================
# 2. MEMORY EFFICIENCY: LIST vs GENERATOR
# ============================================================================

print("\n" + "=" * 60)
print("2. MEMORY EFFICIENCY: LIST vs GENERATOR")
print("=" * 60)

import sys

# List comprehension - stores all values in memory
large_list = [x ** 2 for x in range(1000000)]
print(f"List size: {sys.getsizeof(large_list):,} bytes")

# Generator expression - generates values on demand
large_gen = (x ** 2 for x in range(1000000))
print(f"Generator size: {sys.getsizeof(large_gen):,} bytes")

# The generator is MUCH smaller because it doesn't store all values!
# It only stores the code to generate them.


# ============================================================================
# 3. USING GENERATOR EXPRESSIONS
# ============================================================================

print("\n" + "=" * 60)
print("3. USING GENERATOR EXPRESSIONS")
print("=" * 60)

# Example 1: Direct iteration
print("Iterating over generator:")
gen = (x * 2 for x in range(5))
for value in gen:
    print(f"  {value}", end=" ")
print()

# Example 2: Converting to list (if needed)
gen = (x ** 2 for x in range(5))
squares_list = list(gen)
print(f"\nSquares as list: {squares_list}")

# Example 3: Using with functions that accept iterables
gen = (x for x in range(10) if x % 2 == 0)
print(f"Sum of even numbers: {sum(gen)}")

# Example 4: Using with max/min
gen = (len(word) for word in ["hello", "world", "python"])
print(f"Max word length: {max(gen)}")


# ============================================================================
# 4. GENERATOR EXPRESSIONS WITH CONDITIONS
# ============================================================================

print("\n" + "=" * 60)
print("4. GENERATOR EXPRESSIONS WITH CONDITIONS")
print("=" * 60)

# Filter even numbers
evens_gen = (x for x in range(10) if x % 2 == 0)
print(f"Even numbers: {list(evens_gen)}")

# Filter and transform
squares_of_evens = (x ** 2 for x in range(10) if x % 2 == 0)
print(f"Squares of evens: {list(squares_of_evens)}")

# Conditional expression (ternary)
numbers = [-2, -1, 0, 1, 2, 3]
abs_gen = (x if x >= 0 else -x for x in numbers)
print(f"Absolute values: {list(abs_gen)}")


# ============================================================================
# 5. NESTED GENERATOR EXPRESSIONS
# ============================================================================

print("\n" + "=" * 60)
print("5. NESTED GENERATOR EXPRESSIONS")
print("=" * 60)

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_gen = (num for row in matrix for num in row)
print(f"Matrix: {matrix}")
print(f"Flattened: {list(flattened_gen)}")

# Cartesian product
list_a = [1, 2, 3]
list_b = ['a', 'b']
pairs_gen = ((a, b) for a in list_a for b in list_b)
print(f"\nList A: {list_a}")
print(f"List B: {list_b}")
print(f"Cartesian product: {list(pairs_gen)}")


# ============================================================================
# 6. WHEN TO USE GENERATOR EXPRESSIONS
# ============================================================================

print("\n" + "=" * 60)
print("6. WHEN TO USE GENERATOR EXPRESSIONS")
print("=" * 60)

# Use generator expressions when:
# 1. You only need to iterate once
# 2. Memory is a concern (large datasets)
# 3. You're passing to functions that accept iterables (sum, max, min, etc.)

# Example: Processing large file-like data
def process_numbers(numbers_gen):
    """Process numbers from a generator."""
    total = 0
    count = 0
    for num in numbers_gen:
        total += num
        count += 1
    return total, count

# Generator expression - memory efficient
large_gen = (x for x in range(1000000) if x % 2 == 0)
total, count = process_numbers(large_gen)
print(f"Processed {count:,} numbers, total: {total:,}")

# Use list comprehensions when:
# 1. You need to access elements multiple times
# 2. You need indexing (e.g., my_list[0])
# 3. The dataset is small and memory isn't a concern


# ============================================================================
# 7. COMPARISON: LIST COMPREHENSION vs GENERATOR EXPRESSION
# ============================================================================

print("\n" + "=" * 60)
print("7. COMPARISON: LIST COMPREHENSION vs GENERATOR EXPRESSION")
print("=" * 60)

# Task: Get squares of even numbers from 0 to 9

# Method 1: List comprehension
result_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"List comprehension: {result_list}")
print(f"Type: {type(result_list)}")
print(f"Can access by index: result_list[0] = {result_list[0]}")

# Method 2: Generator expression
result_gen = (x ** 2 for x in range(10) if x % 2 == 0)
print(f"\nGenerator expression: {result_gen}")
print(f"Type: {type(result_gen)}")
print(f"Converted to list: {list(result_gen)}")
# Note: Can't access by index directly - must convert to list first


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Reading and processing large files (conceptual)
# Instead of: lines = [line.strip() for line in file]  # Loads all into memory
# Use: lines_gen = (line.strip() for line in file)  # Processes one at a time

# Example 2: Finding the longest word
words = ["python", "generator", "expression", "comprehension", "memory"]
longest = max((word for word in words), key=len)
print(f"Words: {words}")
print(f"Longest word: {longest}")

# Example 3: Sum of squares
numbers = range(100)
sum_of_squares = sum(x ** 2 for x in numbers)
print(f"\nSum of squares from 0-99: {sum_of_squares:,}")

# Example 4: Filtering and counting
text = "Hello World Python"
vowel_count = sum(1 for char in text.lower() if char in 'aeiou')
print(f"\nText: '{text}'")
print(f"Vowel count: {vowel_count}")

# Example 5: Chaining generators
numbers = range(20)
# First filter evens, then square them
squared_evens = (x ** 2 for x in (n for n in numbers if n % 2 == 0))
print(f"\nSquared even numbers (0-19): {list(squared_evens)}")


# ============================================================================
# 9. COMMON PATTERNS
# ============================================================================

print("\n" + "=" * 60)
print("9. COMMON PATTERNS")
print("=" * 60)

# Pattern 1: Simple transformation
gen = (x * 2 for x in range(5))
print(f"Doubled: {list(gen)}")

# Pattern 2: Filtering
gen = (x for x in range(10) if x % 2 == 0)
print(f"Evens: {list(gen)}")

# Pattern 3: Filter and transform
gen = (word.upper() for word in ["hello", "world"] if len(word) > 4)
print(f"Long words uppercase: {list(gen)}")

# Pattern 4: Using with built-in functions
numbers = range(100)
print(f"Sum: {sum(x for x in numbers if x % 3 == 0)}")
print(f"Max: {max(x for x in numbers if x % 7 == 0)}")
print(f"Any: {any(x > 50 for x in numbers)}")
print(f"All: {all(x < 100 for x in numbers)}")


# ============================================================================
# 10. PERFORMANCE CONSIDERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("10. PERFORMANCE CONSIDERATIONS")
print("=" * 60)

import time

# For small datasets, the difference is negligible
small_range = range(1000)

# List comprehension
start = time.time()
result_list = [x ** 2 for x in small_range]
list_time = time.time() - start

# Generator expression (converted to list for comparison)
start = time.time()
result_gen = list(x ** 2 for x in small_range)
gen_time = time.time() - start

print(f"Small dataset (1000 items):")
print(f"  List comprehension: {list_time:.6f} seconds")
print(f"  Generator expression: {gen_time:.6f} seconds")

# For large datasets, generators save memory
# But if you need to convert to list anyway, use list comprehension directly!

# Key insight: Use generators when you DON'T need the full list
# Example: sum(x for x in range(1000000))  # Don't create list!
# Not: sum([x for x in range(1000000)])  # Creates unnecessary list


# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Generator Expression Syntax:
  (expression for item in iterable)
  (expression for item in iterable if condition)
  (value_if_true if condition else value_if_false for item in iterable)

Key Differences from List Comprehensions:
  1. Uses parentheses () instead of square brackets []
  2. Creates a generator object, not a list
  3. Values are generated on-demand (lazy evaluation)
  4. Much more memory-efficient for large datasets
  5. Can only be iterated once (then it's exhausted)

When to Use Generator Expressions:
  ✓ When memory is a concern (large datasets)
  ✓ When you only need to iterate once
  ✓ When passing to functions that accept iterables (sum, max, min, etc.)
  ✓ When you don't need indexing or multiple passes

When to Use List Comprehensions:
  ✓ When you need to access elements multiple times
  ✓ When you need indexing (my_list[0])
  ✓ When the dataset is small
  ✓ When you need to modify the list later

Remember: Generator expressions are memory-efficient but can only be used once.
If you need the full list, consider using a list comprehension instead.
""")

