# Topic 6: Design Patterns in Python

Design patterns are documented solutions to common software design problems. Python's dynamic nature allows patterns to be implemented more concisely than in strictly-typed languages.

---

## 1. Creational Patterns

Creational patterns abstract the instantiation process.

### A. Singleton Pattern
Ensures a class has only one instance and provides a global point of access to it.
- In Python, this is commonly implemented by overriding the `__new__` method to cache the instance.
- Another Pythonic way is using a metaclass or a module-level import.

```python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### B. Factory Pattern
Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

---

## 2. Structural Patterns

Structural patterns explain how to assemble objects and classes into larger structures.

### Decorator Pattern
Dynamically adds responsibilities to objects.
*Note: This refers to the Object-Oriented Decorator pattern (wrapping an object inside another class matching its interface), which is distinct from Python's syntactic function/method decorators.*

---

## 3. Behavioral Patterns

Behavioral patterns handle communication between objects.

### A. Observer Pattern
A subscription mechanism to notify multiple objects about any events that happen to the object they're observing.
- **Subject**: Holds the state and notifies registered observers.
- **Observer**: Subscribes to updates.

### B. Strategy Pattern
Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
- In Python, since functions are first-class citizens, the Strategy pattern can often be implemented simply by passing functions as arguments.
