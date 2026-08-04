# Demonstration of Variables and Types in Python

# 1. Variables and Dynamic Typing
x = 10
print(f"Value: {x}, Type: {type(x)}")

x = "Akshit"
print(f"Value: {x}, Type: {type(x)}")

# 2. Type Introspection
print(f"Is x a string? {isinstance(x, str)}")

# 3. Type Casting
y = "123"
y_int = int(y)
print(f"String converted to Integer: {y_int} (Type: {type(y_int)})")

z = 0
z_bool = bool(z)
print(f"Integer 0 converted to Boolean: {z_bool} (Type: {type(z_bool)})")
