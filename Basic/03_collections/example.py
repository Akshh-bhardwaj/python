# Demonstration of Collections in Python

# 1. Lists
tech_stack = ["React", "Node.js"]
tech_stack.append("Next.js")
print(f"List: {tech_stack}, First Item: {tech_stack[0]}")

# 2. Tuples
dimension = (1920, 1080)
print(f"Tuple: {dimension}, Width: {dimension[0]}")

# 3. Sets
numbers = {1, 2, 2, 3, 3, 3}
print(f"Set (duplicates removed): {numbers}")

# 4. Dictionaries
profile = {"name": "Akshit", "role": "Dev"}
profile["level"] = 1
print(f"Dict: {profile}")
print(f"Keys: {list(profile.keys())}, Values: {list(profile.values())}")
