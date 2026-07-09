# Topic 8: Advanced Data Structures & Collections in Python

Python provides built-in lists, tuples, dicts, and sets, but for optimized performance and cleaner code, the standard library includes specialized data structure modules like `collections`, `heapq`, and `bisect`.

---

## 1. The `collections` Module

### A. `defaultdict`
A dictionary subclass that calls a factory function to supply missing values, avoiding `KeyError`.
```python
from collections import defaultdict
d = defaultdict(list)
d['key'].append(1)  # Automatically initializes 'key' to a list
```

### B. `Counter`
A dict subclass for counting hashable objects.
```python
from collections import Counter
c = Counter(['a', 'b', 'a'])  # Counter({'a': 2, 'b': 1})
```

### C. `deque`
Double-ended queue. Supports thread-safe, memory-efficient appends and pops from either side in $O(1)$ time (unlike list, which has $O(N)$ pops from the left).
```python
from collections import deque
q = deque()
q.append(1)
q.appendleft(2)
q.popleft()
```

### D. `namedtuple` & `NamedTuple`
Returns a new tuple subclass with named fields, combining the tuple memory efficiency with object attribute readability.

---

## 2. Heap Queue Algorithm (`heapq`)

The `heapq` module provides an implementation of the min-heap queue algorithm.
- Heaps are binary trees where each parent node is less than or equal to its children.
- Useful for implementing **priority queues** and finding the $K$ smallest/largest elements.
- Insertion and deletion take $O(\log N)$ time, and finding the minimum takes $O(1)$ time.

---

## 3. Array Bisection Algorithm (`bisect`)

The `bisect` module provides support for keeping a list in sorted order without having to sort the list after each insertion.
- It uses binary search underneath.
- `bisect.bisect_left(a, x)`: Find the index where `x` should be inserted to maintain sorted order.
- `bisect.insort_left(a, x)`: Insert `x` in sorted order.
- Highly efficient for binary searching sorted arrays.
