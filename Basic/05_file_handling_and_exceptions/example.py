# Demonstration of File Handling and Exception Management in Python

# 1. File Handling
filename = "scratch_test.txt"

# Writing to file
with open(filename, "w") as f:
    f.write("Line 1: Learning Python Basics\n")
    f.write("Line 2: File Handling Demo\n")

# Reading from file
with open(filename, "r") as f:
    content = f.read()
    print("--- File Content ---")
    print(content)

# 2. Exceptions Handling
print("--- Exception Handling Demo ---")
try:
    # Try block with potential errors
    numbers = [1, 2]
    print(numbers[5]) # Raises IndexError
except IndexError as e:
    print(f"Handled IndexError: {e}")
except ZeroDivisionError as e:
    print(f"Handled ZeroDivisionError: {e}")
finally:
    print("Finally block: Execution finished.")
    
# Clean up file
import os
if os.path.exists(filename):
    os.remove(filename)
