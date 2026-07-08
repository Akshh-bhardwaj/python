# 🐍 Advanced Python: Topics, Notes & Codes

Welcome to the **Advanced Python Learning Repository**! This repository has been upgraded from a basic collection of scripts to a comprehensive reference suite of advanced Python concepts, design patterns, testing strategies, concurrency paradigms, and internals.

---

## 📂 Repository Structure

The repository is organized into two primary tracks:
- **`Basic/`**: Contains basic scripts (`hello.py`, `chatbot.py`, `turtle_test.py`) for syntax verification and foundational practices.
- **`Advanced/`**: Focuses on advanced principles, where each topic contains a `notes.md` file for deep technical theory and an executable `example.py` file to demonstrate the concepts.

---

## 📚 Advanced Topics Curriculum

| Module | Topic Name | Description | Key Subtopics Covered |
| :--- | :--- | :--- | :--- |
| **01** | [Advanced OOP](file:///Users/akshit/Desktop/CODE/python/Advanced/01_advanced_oop) | Metaprogramming and complex structures | C3 Linearization & MRO, Metaclasses (`__new__` / `__init__`), Descriptors (`__get__` / `__set__`), Abstract Base Classes (ABCs) |
| **02** | [Decorators & Generators](file:///Users/akshit/Desktop/CODE/python/Advanced/02_decorators_and_generators) | Behavior modification and lazy evaluation | Closures, Parameterized Decorators, Class Decorators, Custom Iterators, Lazy-loading Generators |
| **03** | [Memory Management](file:///Users/akshit/Desktop/CODE/python/Advanced/03_memory_management) | Python runtime memory internals & optimizations | Reference counting, Reference cycles, Cyclic GC, Object optimization using `__slots__`, Weak references (`weakref`) |
| **04** | [Concurrency & Asyncio](file:///Users/akshit/Desktop/CODE/python/Advanced/04_concurrency_and_asyncio) | Parallelism models and context execution | Global Interpreter Lock (GIL), Multi-Threading (I/O-bound), Multiprocessing (CPU-bound), Event loop cooperative multitasking |
| **05** | [Metaprogramming & Introspection](file:///Users/akshit/Desktop/CODE/python/Advanced/05_metaprogramming) | Self-modifying code and dynamic analysis | Advanced introspection (`inspect` module), Dynamic execution (`eval` & `exec`), Static type-hinting & `typing.Protocol` |
| **06** | [Design Patterns](file:///Users/akshit/Desktop/CODE/python/Advanced/06_design_patterns) | Enterprise software architecture patterns | Singleton Metaclass, Factory pattern, Observer subscription system |
| **07** | [Testing & Logging](file:///Users/akshit/Desktop/CODE/python/Advanced/07_testing_and_logging) | Production-grade execution and safety | Structured multi-level logging, Custom exception chaining (`raise from`), `unittest` framework with `patch` and `MagicMock` |

---

## 🚀 How to Run the Code

To execute any of the advanced python demonstration files, run them using Python 3:

```bash
# Example: Running the Advanced OOP examples
python3 Advanced/01_advanced_oop/example.py

# Example: Running the Concurrency and Asyncio examples
python3 Advanced/04_concurrency_and_asyncio/example.py

# Example: Running the Logger, Custom Exceptions & Unit tests
python3 Advanced/07_testing_and_logging/example.py
```
Each file is completely self-contained and outputs descriptive logging statements directly to the console.
