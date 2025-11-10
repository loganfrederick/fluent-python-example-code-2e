- Closures are essential for callbacks
- A decorator is a callable that takes a function as input and returns a new function or callable object
- "Class decorators" are a special case of function decorators that operate on classes rather than functions

```python
def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

# Output of target():
running inner()
# If we wanted to output 'running target()', 
# we would need to call func at some point
```

Three essential facts make a good summary of decorators:
1. Decorators are functions or callable objects
2. A decorator may replace the decorated function with a new function
3. Decorators are executed immediately when a module is loaded

As an exaxmple of number three, see registration.py.


