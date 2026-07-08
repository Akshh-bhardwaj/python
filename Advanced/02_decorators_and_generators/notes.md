# Topic 2: Decorators & Generators in Python

Decorators and generators are two of Python's most powerful syntactic structures, allowing for elegant modification of function behavior and lazy evaluation of data sequences.

---

## 1. Closures

A **closure** is a function object that remembers values in enclosing scopes even if they are not present in memory.
Closures are the building blocks of decorators.

### Conditions for a Closure:
1. There must be a nested function (function inside a function).
2. The nested function must refer to a value defined in the enclosing function.
3. The enclosing function must return the nested function.

---

## 2. Advanced Decorators

Decorators allow you to wrap another function to extend its behavior without permanently modifying it.

### A. Nested Decorators (Decorator Chaining)
Decorators are executed from the bottom up (inside out).
```python
@decorator_one
@decorator_two
def func():
    pass
# Equivalent to: func = decorator_one(decorator_two(func))
```

### B. Parameterized Decorators (Decorators with Arguments)
To pass arguments to a decorator, you need three levels of functions:
1. Outer function to accept the arguments.
2. Middle function to accept the target function.
3. Inner function to wrap the logic and execute it.

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator
```

### C. Class-based Decorators
Instead of functions, classes can be decorators if they implement `__call__`.
```python
class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)
```

---

## 3. Iterators vs. Generators

### Iterators:
An iterator is an object that implements the Iterator Protocol:
- `__iter__()`: Returns the iterator object itself.
- `__next__()`: Returns the next item in the sequence. Raises `StopIteration` when there are no more items.

### Generators:
Generators are a simple way to create iterators using the `yield` statement.
- When a generator function is called, it returns a generator object without executing the function.
- Execution happens only when `__next__()` is called.
- The state of the generator is suspended and resumed dynamically, allowing low memory consumption (lazy evaluation).

```python
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
```
