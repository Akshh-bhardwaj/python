# 🗃️ Python Collections

Python has four built-in collection data types to store groups of data:

---

## 🔑 1. Lists (`[]`)
- Ordered, mutable sequence of items.
- Allows duplicate elements.

```python
fruits = ["apple", "banana"]
fruits.append("cherry") # Modifies the list
```

---

## 🔒 2. Tuples (`()`)
- Ordered, immutable sequence of items.
- Used to protect read-only data.

```python
coordinates = (10, 20)
# coordinates[0] = 15 -> Raises TypeError
```

---

## 🚫 3. Sets (`{}`)
- Unordered, mutable, and unindexed collection.
- Contains only unique elements.

```python
unique_ids = {101, 102, 102} # Stores {101, 102}
```

---

## 📖 4. Dictionaries (`{key: value}`)
- Ordered (as of Python 3.7+), mutable key-value mapping.
- No duplicate keys allowed.

```python
user = {"name": "Aksh", "role": "Dev"}
user["level"] = 1 # Adds new key-value pair
```
