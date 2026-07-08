# Topic 5: Metaprogramming & Introspection in Python

Metaprogramming is the writing of computer programs that write or manipulate other programs (or themselves) as their data, or that do work at compile-time that would otherwise be done at runtime.

---

## 1. Introspection (`inspect` module)

Introspection refers to the ability of a program to examine the type, properties, and structure of an object at runtime. Python is highly introspective.

### Standard Introspection Functions:
- `type(obj)`: Get the type of an object.
- `dir(obj)`: List attributes and methods of an object.
- `hasattr(obj, name)`, `getattr(obj, name)`, `setattr(obj, name, val)`: Dynamic attribute checking, retrieving, and setting.

### The `inspect` Module
The `inspect` module provides advanced introspection features.
- Inspecting function signatures (`inspect.signature`).
- Getting source code dynamically (`inspect.getsource`).
- Inspecting the current call stack (`inspect.stack()`).

---

## 2. Dynamic Code Execution (`eval` & `exec`)

Python allows running dynamic Python source code represented as strings.

- `eval(expression, globals, locals)`: Evaluates a single Python expression and returns the result.
- `exec(object, globals, locals)`: Executes dynamic Python statements (loops, class definitions, multi-line blocks) and returns `None`.

> [!WARNING]
> Security risk: Never run `eval()` or `exec()` on untrusted input as it can execute arbitrary shell commands or code.

---

## 3. Type Hinting & Protocols

Python is dynamically typed but supports static type checking via type hints.

### Type Hints (`typing` module)
Provides type annotations for parameters, return values, and variables.
```python
def add_nums(x: int, y: int) -> int:
    return x + y
```

### Structural Subtyping (Protocols)
In Python 3.8+, `typing.Protocol` allows for **static duck typing**.
- A class doesn't need to inherit from a protocol explicitly.
- It satisfies the protocol simply by implementing the matching signatures.

```python
from typing import Protocol

class Reader(Protocol):
    def read(self) -> str: ...
```
Any class defining a `read()` method returning a string will satisfy the `Reader` interface during static analysis checks.
