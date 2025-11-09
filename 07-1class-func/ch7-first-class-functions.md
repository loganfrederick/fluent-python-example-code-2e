"First-Class Objects" defined as:
- Created at runtime
- Assigned to a variable or element in a data structure
- Passed as an argument to a function
- Returned as the result of a function

In Python, all functions are first-class objects.

# Higher-Order Functions

A higher-order function is a function that takes one or more functions as arguments, or returns a function as its result.

## Example of a higher-order function

```python
def higher_order_function(func):
    return func()
```

```python
fruits = ['apple', 'banana', 'cherry']
sorted_fruits = sorted(fruits, key=len)
print(sorted_fruits)
```

# List Comprehensions and Generators Replace Map, Filter, and Reduce

List comprehensions are often preferred in Python for readability, while generators are better for memory efficiency.

## Map

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)
```

### Using List Comprehension

```python
numbers = [1, 2, 3, 4, 5]
squared = [x * x for x in numbers]
print(squared)
```

### Using Generator Expression

```python
numbers = [1, 2, 3, 4, 5]
squared_gen = (x * x for x in numbers)
squared = list(squared_gen)
print(squared)
```

Or if you only need to iterate once:

```python
numbers = [1, 2, 3, 4, 5]
squared_gen = (x * x for x in numbers)
for num in squared_gen:
    print(num)
```
