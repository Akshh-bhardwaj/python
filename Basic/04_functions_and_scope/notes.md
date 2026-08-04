# 🛠️ Python Functions & Scope

Functions are blocks of organized, reusable code defined using the `def` keyword.

---

## 📥 1. Parameters & Arguments

- **Positional & Keyword**: Standard arguments.
- **Default Parameters**: Arguments that take a fallback value if not specified.
- **`*args`**: Captures a variable number of positional arguments as a tuple.
- **`**kwargs`**: Captures a variable number of keyword arguments as a dictionary.

```python
def make_connection(host, port=8000, *args, **kwargs):
    # host: positional
    # port: default parameter
```

---

## 🌐 2. Variable Scope

Scope determines the visibility of variables:
- **Local Scope**: Variables declared inside a function; accessible only within it.
- **Global Scope**: Variables declared at the script level; accessible everywhere.
- **`global` keyword**: Used to modify a global variable inside a local context.
