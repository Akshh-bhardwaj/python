# 📝 Python Variables and Types

Python is dynamically typed. This means you do not need to declare a variable's data type when creating it; the interpreter infers the type at runtime.

---

## 🔑 1. Primitive Data Types

Python has four primary primitive data types:

| Type | Description | Example |
| :--- | :--- | :--- |
| **`int`** | Arbitrary-precision integers | `x = 42` |
| **`float`** | Double-precision floating point numbers | `y = 3.14` |
| **`str`** | Unicode character sequences (immutable) | `text = "Hello"` |
| **`bool`** | Logical values | `is_active = True` |

---

## 🔄 2. Type Casting and Introspection

- **Introspection**: You can check a variable's type using `type(var)` or `isinstance(var, type)`.
- **Casting**: Convert from one type to another using constructor functions (`int()`, `float()`, `str()`, `bool()`).

```python
num = int("100")      # String to integer
decimal = float("3.1")# String to float
text = str(42)        # Integer to string
flag = bool(1)        # Integer to boolean (True)
```
