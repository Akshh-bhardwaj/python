# 📁 File Handling & Exception Management

Robust scripts require secure file I/O operations and graceful handling of runtime exceptions.

---

## 🔒 1. File Handling with Context Managers

Always open files using the `with` statement. It automatically closes the file after the block is exited, avoiding resource leaks.

```python
# Write file
with open("data.txt", "w") as f:
    f.write("Line content")

# Read file
with open("data.txt", "r") as f:
    content = f.read()
```

---

## 🚦 2. Exception Handling

Handle runtime errors using `try`, `except`, and `finally` blocks:
- **`try`**: Code block that might raise an error.
- **`except`**: Code block that executes if an error is caught.
- **`finally`**: Code block that executes unconditionally (ideal for cleanup tasks).

```python
try:
    num = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught division error: {e}")
finally:
    print("Cleanup actions complete.")
```
