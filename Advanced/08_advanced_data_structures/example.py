import bisect
from collections import defaultdict, Counter, deque
import heapq
from typing import NamedTuple

# ----------------------------------------------------
# 1. Collections: defaultdict, Counter, deque, NamedTuple
# ----------------------------------------------------
print("--- 1. Collections Module ---")

# A. defaultdict
word_groups = defaultdict(list)
words = ["apple", "banana", "apricot", "cherry", "blueberry"]
for word in words:
    first_char = word[0]
    word_groups[first_char].append(word)
print("defaultdict (grouped by first character):", dict(word_groups))

# B. Counter
text = "apple banana apple cherry banana banana"
counter = Counter(text.split())
print("Counter values:", counter)
print("Top 2 most common:", counter.most_common(2))

# C. deque
dq = deque(maxlen=3)  # Fixed-size buffer
dq.append(1)
dq.append(2)
dq.append(3)
print("deque fully loaded:", list(dq))
dq.append(4)  # Drops 1 from left automatically
print("deque after appending 4:", list(dq))
dq.appendleft(9)  # Drops 4 from right
print("deque after appendleft 9:", list(dq))

# D. NamedTuple
class UserProfile(NamedTuple):
    id: int
    username: str
    role: str

user = UserProfile(1, "aksh_dev", "administrator")
print(f"NamedTuple: User {user.username} (ID: {user.id}) has role '{user.role}'.")
print()


# ----------------------------------------------------
# 2. Heapq (Min-Heap / Priority Queue)
# ----------------------------------------------------
print("--- 2. Heapq (Priority Queue) ---")

# List of tuple tasks: (priority, task_name)
tasks = []
heapq.heappush(tasks, (3, "Code review"))
heapq.heappush(tasks, (1, "Fix production bug"))
heapq.heappush(tasks, (2, "Write documentation"))
heapq.heappush(tasks, (5, "Check emails"))

print("Priority order tasks pop:")
while tasks:
    priority, task_name = heapq.heappop(tasks)
    print(f"  [Priority {priority}] {task_name}")

# Finding K smallest or largest elements in a list
numbers = [42, 10, 85, 23, 7, 66]
print("3 smallest numbers:", heapq.nsmallest(3, numbers))
print("3 largest numbers:", heapq.nlargest(3, numbers))
print()


# ----------------------------------------------------
# 3. Bisect (Binary Search and Sorted Insertion)
# ----------------------------------------------------
print("--- 3. Bisect (Sorted Array Utility) ---")

sorted_list = [10, 20, 30, 40, 50]
# Find index where 25 should be inserted
index = bisect.bisect_left(sorted_list, 25)
print(f"Index to insert 25 in {sorted_list}: {index}")

# Insert keeping sorted order
bisect.insort_left(sorted_list, 25)
print("Sorted list after insort 25:", sorted_list)
