# 🔄 Python Control Flow

Control flow structures direct the order in which code statements are executed. Python uses indentation to define code blocks.

---

## 🚦 1. Conditionals (`if`, `elif`, `else`)

Executes blocks of code based on logical conditions.

```python
x = 10
if x > 15:
    print("Greater than 15")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")
```

---

## 🔁 2. Loops

- **`for` loop**: Iterates over a sequence (list, range, string).
- **`while` loop**: Repeats as long as a boolean condition evaluates to `True`.

```python
# Iterating over range
for i in range(3):
    print(i) # Outputs 0, 1, 2

# While loop
count = 0
while count < 3:
    print(count)
    count += 1
```

---

## 🛠️ 3. Control Flow Statements
- **`break`**: Terminates the loop prematurely.
- **`continue`**: Skips the current iteration and goes to the next.
- **`pass`**: A null statement acting as a placeholder.
