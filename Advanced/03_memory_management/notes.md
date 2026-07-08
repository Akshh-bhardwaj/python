# Topic 3: Memory Management & Performance in Python

Python abstracts memory management, but for high-performance systems and large scale software development, understanding the internals of garbage collection, optimizations like slots, and handling references is critical.

---

## 1. Reference Counting & Garbage Collection

CPython uses two primary strategies for garbage collection (GC):
1. **Reference Counting**: Every Python object has a field (`ob_refcnt` in C) tracking how many variables/objects point to it. When `ref_count` drops to `0`, Python immediately deallocates the memory.
2. **Generational Garbage Collection**: Reference counting cannot resolve **reference cycles** (e.g., object A references object B, and object B references object A). To fix this, Python runs a generational cyclic collector that runs periodically.

### Generations
The collector divides objects into 3 generations (0, 1, and 2).
- Fresh objects start in Generation 0.
- If they survive a GC collection cycle, they are promoted to Generation 1, then eventually to Generation 2.
- Generation 0 is collected frequently; Generation 2 is collected rarely.

---

## 2. Optimizing Memory with `__slots__`

By default, Python classes store their attributes in a dynamic dictionary called `__dict__`. While highly flexible, dictionaries consume significant memory because they are hash maps.

By defining `__slots__` in a class, Python allocates space for attributes statically in a small array of references.
- Reduces memory usage significantly (often >50% reduction for large lists of objects).
- Increases attribute access speed.
- **Side effect**: Instances cannot have custom attributes added dynamically unless they are listed in `__slots__`.

```python
class OptimizedClass:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## 3. Weak References (`weakref`)

A **weak reference** is a reference to an object that does not prevent that object from being garbage collected.
- Regular assignments create **strong references** (incrementing the reference count).
- Weak references are useful for building caches, registry systems, and observer graphs where you do not want to keep objects alive just because they are registered.

Use the `weakref` module to create weak references or dictionaries.
```python
import weakref

class LargeObject:
    pass

obj = LargeObject()
r = weakref.ref(obj)  # Creating a weak reference
```
If `obj` is deleted, `r()` returns `None`.
