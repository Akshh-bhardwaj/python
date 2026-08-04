# Demonstration of Functions and Scope in Python

# 1. Basic & Default Parameters
def greet(name, greeting="Welcome"):
    return f"{greeting}, {name}!"

print(greet("Aksh"))
print(greet("Akshit", "Hello"))

# 2. Variable-length Arguments (*args, **kwargs)
def print_details(*args, **kwargs):
    print(f"Args (tuple): {args}")
    print(f"Kwargs (dict): {kwargs}")

print_details("C++", "Java", "Python", editor="VS Code", system="Mac")

# 3. Scope Demonstration
count = 10 # Global variable

def increment():
    global count
    count += 1 # Modifying global variable

increment()
print(f"Global Count after modification: {count}")
