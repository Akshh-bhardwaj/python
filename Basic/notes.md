# 🐍 Python Basics: Notes & Concepts

This document covers the foundational concepts of Python syntax, data types, control flow, functions, file handling, and basic error management.

---

## 1. Variables & Primitive Data Types

Python is dynamically typed—you do not need to declare a variable's type explicitly. The type is determined at runtime.

### Data Types:
- **`int`**: Arbitrary-precision integers (e.g., `x = 42`).
- **`float`**: Double-precision floating-point numbers (e.g., `y = 3.14`).
- **`str`**: Immutable sequence of Unicode characters (e.g., `name = "Aksh"`). Supports formatting using f-strings: `f"Hello, {name}"`.
- **`bool`**: Boolean values (`True` or `False`).

```python
# Type casting
age = int("25")
height = float("1.75")
status = bool(1) # True
```

---

## 2. Core Collections

Python has four built-in collection data types:

| Collection | Ordering | Mutability | Duplicates | Key Characteristics |
| :--- | :--- | :--- | :--- | :--- |
| **List (`[]`)** | Ordered | Mutable | Allowed | Dynamic array, indexed access |
| **Tuple (`()`)** | Ordered | Immutable | Allowed | Fixed size, read-only, hashable |
| **Set (`{}`)** | Unordered | Mutable | Unique | Hash table based, no duplicate keys |
| **Dict (`{k:v}`)**| Ordered (3.7+) | Mutable | Unique keys | Key-value pairs, fast lookup |

### Basic Operations:
```python
# List operations
fruits = ["apple", "banana"]
fruits.append("cherry")

# Dictionary operations
user = {"name": "Aksh", "role": "Developer"}
user["level"] = 1

# Set operations (for membership testing and unique filters)
unique_ids = {101, 102, 102} # {101, 102}
```

---

## 3. Control Flow

Control flow structures dictate execution pathways using indentation.

### Conditionals:
```python
x = 10
if x > 15:
    print("Greater than 15")
elif x == 10:
    print("Equal to 10")
else:
    print("Smaller or equal")
```

### Loops:
- **`for` loop**: Iterates over a sequence (list, range, string).
- **`while` loop**: Execution loops until a condition is no longer met.

```python
# For Loop with range
for i in range(3): # 0, 1, 2
    print(i)

# While Loop
count = 0
while count < 3:
    print(count)
    count += 1
```

---

## 4. Functions & Scope

Functions are blocks of reusable code defined using the `def` keyword.

### Parameters & Arguments:
- **Positional/Keyword**: Standard arguments.
- **`*args`**: Arbitrary positional arguments (tuple).
- **`**kwargs`**: Arbitrary keyword arguments (dict).

```python
def greet(name, msg="Welcome"):
    return f"{msg}, {name}!"

def print_args(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

# Call: print_args(1, 2, a=3, b=4)
```

---

## 5. File Operations

Always use the `with` statement when opening files to ensure they are closed automatically, avoiding resource leaks.

```python
# Writing to a file
with open("output.txt", "w") as f:
    f.write("Hello, World!")

# Reading from a file
with open("output.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## 6. Exception Handling

Handle runtime errors gracefully using `try`, `except`, and `finally` blocks.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
finally:
    print("This runs unconditionally (useful for cleanup)")
```
