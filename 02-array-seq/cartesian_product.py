"""
cartesian_product.py

Demonstrates how to use Python list comprehensions to find the cartesian product
of two lists.

The cartesian product of two lists A and B is the set of all ordered pairs (a, b)
where a is from A and b is from B.
"""

# ============================================================================
# BASIC CARTESIAN PRODUCT WITH LIST COMPREHENSION
# ============================================================================

print("=" * 60)
print("CARTESIAN PRODUCT WITH LIST COMPREHENSION")
print("=" * 60)

# Example 1: Simple cartesian product
list_a = [1, 2, 3]
list_b = ['a', 'b']

# Traditional way with nested for loops:
cartesian_traditional = []
for a in list_a:
    for b in list_b:
        cartesian_traditional.append((a, b))

print(f"\nList A: {list_a}")
print(f"List B: {list_b}")
print(f"\nTraditional way (nested loops):")
print(f"  {cartesian_traditional}")

# List comprehension way (much more concise!):
cartesian_comprehension = [(a, b) for a in list_a for b in list_b]
print(f"\nList comprehension:")
print(f"  {cartesian_comprehension}")

# Syntax: [(a, b) for a in list_a for b in list_b]
# Read as: "for each a in list_a, for each b in list_b, create tuple (a, b)"


# ============================================================================
# MORE EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("MORE EXAMPLES")
print("=" * 60)

# Example 2: Cartesian product of numbers
numbers = [1, 2, 3]
colors = ['red', 'blue']
combinations = [(num, color) for num in numbers for color in colors]
print(f"\nNumbers: {numbers}")
print(f"Colors: {colors}")
print(f"All combinations: {combinations}")

# Example 3: Cartesian product with strings
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = [(rank, suit) for suit in suits for rank in ranks]
print(f"\nSuits: {suits}")
print(f"Ranks: {ranks}")
print(f"Total cards: {len(cards)}")
print(f"First 5 cards: {cards[:5]}")
print(f"Last 5 cards: {cards[-5:]}")

# Example 4: Cartesian product with filtering
# Only include pairs where the number is greater than the index
list_x = [1, 2, 3, 4]
list_y = [0, 1, 2]
filtered_pairs = [(x, y) for x in list_x for y in list_y if x > y]
print(f"\nList X: {list_x}")
print(f"List Y: {list_y}")
print(f"Pairs where x > y: {filtered_pairs}")

# Example 5: Cartesian product with transformation
# Create pairs and calculate their product
nums1 = [2, 3, 4]
nums2 = [5, 6]
products = [(a, b, a * b) for a in nums1 for b in nums2]
print(f"\nNumbers 1: {nums1}")
print(f"Numbers 2: {nums2}")
print(f"Pairs with products: {products}")


# ============================================================================
# COMPARISON: NESTED LOOPS vs LIST COMPREHENSION
# ============================================================================

print("\n" + "=" * 60)
print("COMPARISON: NESTED LOOPS vs LIST COMPREHENSION")
print("=" * 60)

# Task: Create all pairs from two lists

list1 = [10, 20]
list2 = ['x', 'y', 'z']

# Method 1: Traditional nested for loops
result1 = []
for item1 in list1:
    for item2 in list2:
        result1.append((item1, item2))
print(f"\nNested loops: {result1}")

# Method 2: List comprehension (more Pythonic!)
result2 = [(item1, item2) for item1 in list1 for item2 in list2]
print(f"List comprehension: {result2}")

# Both produce the same result, but list comprehension is:
# - More concise (one line vs multiple lines)
# - More readable (once you understand the syntax)
# - More Pythonic (follows Python best practices)


# ============================================================================
# CARTESIAN PRODUCT OF MORE THAN TWO LISTS
# ============================================================================

print("\n" + "=" * 60)
print("CARTESIAN PRODUCT OF MORE THAN TWO LISTS")
print("=" * 60)

# You can extend this pattern to more than two lists
list_a = [1, 2]
list_b = ['a', 'b']
list_c = ['x', 'y']

# Three-way cartesian product
triples = [(a, b, c) for a in list_a for b in list_b for c in list_c]
print(f"\nList A: {list_a}")
print(f"List B: {list_b}")
print(f"List C: {list_c}")
print(f"All triples: {triples}")
print(f"Total combinations: {len(triples)}")


# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Cartesian Product with List Comprehension:
  [(a, b) for a in list_a for b in list_b]

Key Points:
  1. The cartesian product creates all possible pairs from two lists
  2. List comprehensions make this concise and readable
  3. Read nested comprehensions from left to right:
     - "for each a in list_a, for each b in list_b, create (a, b)"
  4. You can add conditions: [(a, b) for a in A for b in B if condition]
  5. You can extend to more lists: [(a, b, c) for a in A for b in B for c in C]

Note: For very large lists, consider using itertools.product() which is
more memory-efficient as it returns an iterator.
""")
