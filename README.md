# 🐍 Advanced Python: Topics, Notes & Codes

Welcome to the **Advanced Python Learning Repository**! This repository has been upgraded from a basic collection of scripts to a comprehensive reference suite of advanced Python concepts, design patterns, testing strategies, concurrency paradigms, and internals.

---

## 📂 Repository Structure

The repository is organized into two primary tracks:
- **`Basic/`**: Focuses on foundational Python principles, where each module contains a `notes.md` file for syntax & theory and an executable `example.py` file to demonstrate concepts.
- **`Advanced/`**: Focuses on advanced principles, where each topic contains a `notes.md` file for deep technical theory and an executable `example.py` file to demonstrate the concepts.

---

## 📚 Basic Topics Curriculum

| Module | Topic Name | Description | Key Subtopics Covered |
| :--- | :--- | :--- | :--- |
| **01** | [Variables & Types](file:///Users/akshit/Desktop/CODE/python/Basic/01_variables_and_types) | Variables and casting | Primitive types (int, float, str, bool), dynamic typing, casting, introspection |
| **02** | [Control Flow](file:///Users/akshit/Desktop/CODE/python/Basic/02_control_flow) | Loops and conditionals | if-elif-else, for loops, while loops, loop controls (break, continue, pass) |
| **03** | [Collections](file:///Users/akshit/Desktop/CODE/python/Basic/03_collections) | High-level data grouping | Lists, tuples, sets, dictionaries, mutability, indexing, basic operations |
| **04** | [Functions & Scope](file:///Users/akshit/Desktop/CODE/python/Basic/04_functions_and_scope) | Reusable logic blocks | Function def, default arguments, variable-length parameters (*args, **kwargs), local vs global scope |
| **05** | [File I/O & Exceptions](file:///Users/akshit/Desktop/CODE/python/Basic/05_file_handling_and_exceptions) | Resource and error safety | with statement, reading/writing files, try-except-finally blocks |

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
| **08** | [Advanced Data Structures](file:///Users/akshit/Desktop/CODE/python/Advanced/08_advanced_data_structures) | High-performance container data types | Collections (`defaultdict`, `Counter`, `deque`, `NamedTuple`), Min-heaps (`heapq`), Sorted insertions (`bisect`) |
| **09** | [Database Integration & ORMs](file:///Users/akshit/Desktop/CODE/python/Advanced/09_database_integration) | SQL integrations and transaction safety | DB-API specifications, Built-in SQLite (`sqlite3`), Preventing SQL injection, Rollback context managers, ORM patterns |
| **10** | [System & Networking](file:///Users/akshit/Desktop/CODE/python/Advanced/10_system_and_networking) | Low-level execution and TCP socket streams | OS/Sys/Shutil functions, Subprocess pipeline management (`subprocess`), Concurrent TCP socket server-client communication |

---

## 🚀 How to Run the Code

To execute any of the advanced python demonstration files, run them using Python 3:

```bash
# Example: Running the Advanced OOP examples
python3 Advanced/01_advanced_oop/example.py

# Example: Running the Concurrency and Asyncio examples
python3 Advanced/04_concurrency_and_asyncio/example.py

# Example: Running the Database Transactions rollback examples
python3 Advanced/09_database_integration/example.py
```
Each file is completely self-contained and outputs descriptive logging statements directly to the console.
