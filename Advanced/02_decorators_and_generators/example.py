import functools
import time

# ----------------------------------------------------
# 1. Parameterized Decorator with functools.wraps
# ----------------------------------------------------
print("--- 1. Parameterized Decorator (Logging Execution Time) ---")

def timer(label="Default"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"[{label}] Function '{func.__name__}' took {end - start:.6f} seconds to execute.")
            return result
        return wrapper
    return decorator

@timer(label="Database Query")
def mock_db_query(n):
    """Simulates a database fetch."""
    time.sleep(0.1)
    return list(range(n))

print("Executing mock query...")
data = mock_db_query(5)
print("Function Name preserved:", mock_db_query.__name__)
print("Docstring preserved:", mock_db_query.__doc__)
print()


# ----------------------------------------------------
# 2. Class-Based Decorator
# ----------------------------------------------------
print("--- 2. Class-Based Decorator ---")

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.calls = 0
        functools.update_wrapper(self, func)  # Preserves function metadata in class-based decorators

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Call {self.calls} to '{self.func.__name__}'")
        return self.func(*args, **kwargs)

@CallCounter
def compute_square(x):
    return x * x

print("Result:", compute_square(4))
print("Result:", compute_square(5))
print(f"Total calls tracked: {compute_square.calls}")
print()


# ----------------------------------------------------
# 3. Custom Iterator Protocol
# ----------------------------------------------------
print("--- 3. Custom Iterator (Powers of Two) ---")

class PowerOfTwo:
    def __init__(self, max_exponent):
        self.max_exponent = max_exponent
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_exponent:
            raise StopIteration
        result = 2 ** self.current
        self.current += 1
        return result

# Using custom iterator
for val in PowerOfTwo(5):
    print(val, end=" ")
print("\n")


# ----------------------------------------------------
# 4. Generators (Lazy Evaluation)
# ----------------------------------------------------
print("--- 4. Generators (Large Dataset Generator) ---")

def large_range_generator(limit):
    """Generates numbers one by one without loading all into memory."""
    num = 0
    while num < limit:
        yield num
        num += 1

gen = large_range_generator(1000000)
print("Generator instance created:", gen)
# Get first few items
print("Next item:", next(gen))
print("Next item:", next(gen))
print("Next item:", next(gen))
