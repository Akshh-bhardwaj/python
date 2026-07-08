import inspect
from typing import Protocol

# ----------------------------------------------------
# 1. Introspection using the inspect module
# ----------------------------------------------------
print("--- 1. Introspection (inspect) ---")

def calculate_salary(base: float, bonus: float = 500.0, tax_rate: float = 0.2) -> float:
    """Calculates dynamic net salary based on tax and bonus."""
    gross = base + bonus
    return gross * (1 - tax_rate)

# Inspect the signature of calculate_salary
sig = inspect.signature(calculate_salary)
print("Function Name: calculate_salary")
print("Parameters details:")
for param_name, param in sig.parameters.items():
    print(f"  Parameter: {param_name}")
    print(f"    Default value: {param.default}")
    print(f"    Annotation: {param.annotation}")
    print(f"    Kind: {param.kind}")
print()


# ----------------------------------------------------
# 2. Dynamic Execution (eval & exec)
# ----------------------------------------------------
print("--- 2. Dynamic Execution (eval/exec) ---")

# A. eval: evaluates single expressions and returns a result
expression = "3 * 10 + 5 / 2"
result = eval(expression)
print(f"eval result for '{expression}': {result}")

# B. exec: executes multi-line code blocks
dynamic_code = """
def dynamic_hello(name):
    return f"Hello dynamically, {name}!"
"""
# Execute code inside global context dict
globals_dict = {}
exec(dynamic_code, globals_dict)

# Retrieve and execute the dynamically defined function
dynamic_func = globals_dict["dynamic_hello"]
print(dynamic_func("Akshit"))
print()


# ----------------------------------------------------
# 3. Protocols (Static Duck Typing)
# ----------------------------------------------------
print("--- 3. Protocols (Static Duck Typing) ---")

# Define Protocol
class Streamer(Protocol):
    def stream_data(self) -> str:
        ...

# Implementing classes (no explicit inheritance of Streamer protocol needed)
class VideoStream:
    def stream_data(self) -> str:
        return "Streaming high-definition video track..."

class AudioStream:
    def stream_data(self) -> str:
        return "Streaming stereo audio track..."

class InvalidStream:
    # Does not fit the protocol (missing stream_data method)
    def play(self):
        print("Playing...")

def play_stream(stream: Streamer):
    # This function expects objects that conform to the Streamer Protocol
    print("Stream output:", stream.stream_data())

v = VideoStream()
a = AudioStream()
invalid = InvalidStream()

# Correct executions
play_stream(v)
play_stream(a)

print("Classes conforms to Protocol dynamically at runtime based on structure.")
