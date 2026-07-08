# Topic 1: Advanced Object-Oriented Programming (OOP) in Python

Python's object-oriented paradigm is dynamic and highly flexible. Understanding advanced OOP concepts allows you to write frameworks, libraries, and highly reusable components.

---

## 1. Method Resolution Order (MRO) & C3 Linearization

When multiple inheritance is used in Python, the interpreter needs a deterministic path to resolve method calls. Python uses the **C3 Linearization** algorithm to compute the Method Resolution Order (MRO).

### Key Rules of C3 Linearization:
- **Subclasses before superclasses**: A child class must be searched before its parent classes.
- **Local precedence ordering**: If a class inherits from multiple parents, say `class A(B, C)`, then `B` must be checked before `C` in the search order.
- **Monotonicity**: If a class `D` inherits from `A` and `B`, the relative order of `A` and `B` in any MRO must not contradict the order established in other MROs.

You can inspect the resolution order using the class attribute `__mro__` or the method `mro()`.
```python
print(MyClass.__mro__)
```

---

## 2. Metaclasses & Dynamic Class Creation

In Python, classes are objects themselves. The object responsible for creating class objects is called a **metaclass**. By default, Python uses `type` as the metaclass.

### Custom Metaclass
A metaclass inherits from `type` and overrides the `__new__` or `__init__` methods.
- `__new__(mcs, name, bases, attrs)`: Executed before class creation; used to modify the class attributes or bases before class object construction.
- `__init__(cls, name, bases, attrs)`: Executed after the class object has been created; used to initialize the class object.

```python
class Meta(type):
    def __new__(mcs, name, bases, attrs):
        # Intercept and modify attributes here
        attrs['custom_attribute'] = "Added by metaclass"
        return super().__new__(mcs, name, bases, attrs)
```

---

## 3. The Descriptor Protocol

Descriptors are python objects that define the access behavior of other objects' attributes. They implement one or more of the descriptor protocol methods:
- `__get__(self, instance, owner)`: Retrieve an attribute value.
- `__set__(self, instance, value)`: Set an attribute value.
- `__delete__(self, instance)`: Delete an attribute.

### Types of Descriptors:
1. **Data Descriptors**: Define both `__get__` and `__set__`. They take precedence over instance dictionary lookups.
2. **Non-data Descriptors**: Define only `__get__`. They can be overridden by instance dictionary assignments.

Descriptors are the underlying mechanism for properties (`@property`), class methods (`@classmethod`), and static methods (`@staticmethod`).

---

## 4. Abstract Base Classes (ABCs)

Abstract Base Classes provide a way to define interfaces in Python, ensuring that inheriting subclasses implement specific methods. The `abc` module is used to construct them.

- Use the `@abc.abstractmethod` decorator to declare abstract methods.
- A class inheriting from an ABC cannot be instantiated unless all abstract methods are overridden.

```python
from abc import ABC, abstractmethod

class DBConnection(ABC):
    @abstractmethod
    def connect(self):
        pass
```
