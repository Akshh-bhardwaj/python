# Demonstration of Control Flow in Python

# 1. Conditionals
value = 25
if value > 50:
    print("High value")
elif value >= 20:
    print("Medium value")
else:
    print("Low value")

# 2. Loops and Break/Continue
print("\n--- Iteration Demo ---")
for i in range(1, 6):
    if i == 3:
        print("Skipping 3 (continue)")
        continue
    if i == 5:
        print("Breaking loop at 5")
        break
    print(f"Number: {i}")

# 3. While Loop
print("\n--- While Loop Demo ---")
limit = 3
while limit > 0:
    print(f"Limit remaining: {limit}")
    limit -= 1
