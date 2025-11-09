# Major Types of Python Collections

## Collections Module Types:

1. **`namedtuple`** — Creates tuple subclasses with named fields for readable, immutable records.

2. **`deque`** — Double-ended queue. Supports O(1) appends/pops from both ends. Useful for queues and stacks.

3. **`Counter`** — Dict subclass for counting hashable objects. Tracks element frequencies.

4. **`OrderedDict`** — Dict subclass that remembers insertion order (less needed in Python 3.7+ since regular dicts are ordered).

5. **`defaultdict`** — Dict subclass that provides default values for missing keys via a factory function.

6. **`ChainMap`** — Groups multiple dicts into a single mapping view. Useful for layered configurations.

7. **`UserDict`, `UserList`, `UserString`** — Wrapper classes for creating custom dict/list/string-like types.

## Collections Abstract Base Classes (collections.abc):

These ABCs define protocols for different types of collections and are useful for type checking and creating custom collection types:

1. **`Sequence`** — Abstract base class for ordered collections that support indexing and iteration. Examples: `list`, `tuple`, `str`, `bytes`, `range`. Sequences are collections that maintain order and allow access by integer index.

2. **`MutableSequence`** — Abstract base class for mutable sequences. Examples: `list`, `bytearray`. Extends `Sequence` with methods for modification.

3. **`Mapping`** — Abstract base class for key-value mappings. Examples: `dict`, `collections.OrderedDict`, `collections.defaultdict`.

4. **`MutableMapping`** — Abstract base class for mutable mappings. Example: `dict`.

5. **`Set`** — Abstract base class for collections of unique elements. Examples: `set`, `frozenset`.

6. **`MutableSet`** — Abstract base class for mutable sets. Example: `set`.

7. **`Collection`** — Base abstract base class for all collection types. Defines the basic protocol (`__len__`, `__iter__`, `__contains__`).

## Built-in Collection Types:

- **`list`** — Mutable, ordered sequences
- **`tuple`** — Immutable, ordered sequences  
- **`dict`** — Mutable key-value mappings (ordered since Python 3.7)
- **`set`** — Mutable, unordered collections of unique elements
- **`frozenset`** — Immutable version of set

## Example Usage in frenchdeck.py

In your `frenchdeck.py`, `namedtuple` creates a `Card` with `rank` and `suit` fields, making the deck implementation cleaner than using regular tuples.

Additionally, the `FrenchDeck` class implements the sequence protocol by defining `__len__` and `__getitem__`, making it behave like a sequence collection. This allows it to support iteration, slicing, and other sequence operations without explicitly inheriting from `Sequence`.

