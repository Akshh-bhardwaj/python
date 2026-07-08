import gc
import sys
import time
import weakref

# ----------------------------------------------------
# 1. Reference Counting & sys.getrefcount
# ----------------------------------------------------
print("--- 1. Reference Counting & Deallocation ---")

a = [1, 2, 3]
# sys.getrefcount includes the temporary reference passed to the function itself!
print("Initial ref count of 'a':", sys.getrefcount(a) - 1)

b = a
print("Ref count after 'b = a':", sys.getrefcount(a) - 1)

c = [a]
print("Ref count after putting 'a' in a list:", sys.getrefcount(a) - 1)

del b
del c
print("Ref count after deleting b and c references:", sys.getrefcount(a) - 1)
print()


# ----------------------------------------------------
# 2. Reference Cycles & Cyclic Garbage Collector
# ----------------------------------------------------
print("--- 2. Circular References and Manual Garbage Collection ---")

class Node:
    def __init__(self, name):
        self.name = name
        self.partner = None

    def __del__(self):
        print(f"Node {self.name} deallocated.")

# Disable automatic GC to demonstrate cycles explicitly
gc.disable()

node1 = Node("A")
node2 = Node("B")

# Create a cyclic reference
node1.partner = node2
node2.partner = node1

# Delete our strong local handles to nodes
del node1
del node2

print("Strong references deleted. Has Node __del__ been called yet?")
# Since they form a cycle, ref counts are still > 0.

# Manually trigger the garbage collection cycle
print("Manually running gc.collect()...")
collected = gc.collect()
print(f"GC collected {collected} unreachable objects.")

# Re-enable GC
gc.enable()
print()


# ----------------------------------------------------
# 3. Memory Optimization with slots
# ----------------------------------------------------
print("--- 3. Performance & Memory: __slots__ comparison ---")

class RegularClass:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class SlottedClass:
    __slots__ = ['name', 'score']
    def __init__(self, name, score):
        self.name = name
        self.score = score

# Let's check size differences by instantiating many instances
count = 100000

# Regular class timing
start_reg = time.perf_counter()
regular_objects = [RegularClass("Student", i) for i in range(count)]
time_reg = time.perf_counter() - start_reg

# Slotted class timing
start_slot = time.perf_counter()
slotted_objects = [SlottedClass("Student", i) for i in range(count)]
time_slot = time.perf_counter() - start_slot

print(f"Created {count} regular objects in: {time_reg:.4f} seconds.")
print(f"Created {count} slotted objects in: {time_slot:.4f} seconds.")

# Try setting dynamic attribute
try:
    slotted_objects[0].new_attribute = "Not allowed"
except AttributeError as e:
    print(f"Slotted class attribute insertion restricted: {e}")
print()


# ----------------------------------------------------
# 4. Weak References
# ----------------------------------------------------
print("--- 4. Weak References (weakref) ---")

class TargetObject:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"TargetObject({self.value})"

strong_ref = TargetObject(42)
weak_ref = weakref.ref(strong_ref)

print("Accessing object via weak reference:", weak_ref())

# Let's delete the strong reference
del strong_ref
print("Deleted strong reference. Checking weak reference status...")
print("Accessing object via weak reference now:", weak_ref())
