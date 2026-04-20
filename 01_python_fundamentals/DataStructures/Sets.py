# ==========================================
# PYTHON SETS - COMPLETE CHEATSHEET
# DATA ENGINEERING / PRODUCTION STYLE
# ==========================================

# -------------------------------
# 1. CREATE SETS
# -------------------------------
empty_set = set()

data = {1, 2, 3, 4, 4, 5}  # duplicates removed automatically

print("Initial set:", data)


# -------------------------------
# 2. ADD ELEMENT
# -------------------------------
s = {1, 2, 3}

s.add(4)

print("\nAfter add:", s)


# -------------------------------
# 3. UPDATE (ADD MULTIPLE ELEMENTS)
# -------------------------------
s.update([5, 6, 7])

print("\nAfter update:", s)


# -------------------------------
# 4. REMOVE ELEMENT (ERROR IF NOT FOUND)
# -------------------------------
s.remove(7)

print("\nAfter remove:", s)


# -------------------------------
# 5. DISCARD (SAFE REMOVE)
# -------------------------------
s.discard(100)  # no error

print("\nAfter discard:", s)


# -------------------------------
# 6. POP (REMOVE RANDOM ELEMENT)
# -------------------------------
popped = s.pop()

print("\nPopped element:", popped)
print("After pop:", s)


# -------------------------------
# 7. CLEAR SET
# -------------------------------
temp = {1, 2, 3}

temp.clear()

print("\nAfter clear:", temp)


# -------------------------------
# 8. MEMBERSHIP TEST (VERY IMPORTANT)
# -------------------------------
check_set = {10, 20, 30}

print("\n20 in set?", 20 in check_set)
print("100 in set?", 100 in check_set)


# -------------------------------
# 9. UNION (|) - COMBINE SETS
# -------------------------------
a = {1, 2, 3}
b = {3, 4, 5}

print("\nUnion:", a | b)


# -------------------------------
# 10. INTERSECTION (&) - COMMON ELEMENTS
# -------------------------------
print("Intersection:", a & b)


# -------------------------------
# 11. DIFFERENCE (-) - LEFT ONLY
# -------------------------------
print("Difference A-B:", a - b)


# -------------------------------
# 12. SYMMETRIC DIFFERENCE (^)
# -------------------------------
print("Symmetric difference:", a ^ b)


# -------------------------------
# 13. SET COMPREHENSION
# -------------------------------
nums = [1, 2, 3, 4, 5]

squares = {x * x for x in nums}

print("\nSet comprehension:", squares)


# -------------------------------
# 14. LIST → SET (DEDUPLICATION)
# -------------------------------
logs = ["a", "b", "a", "c", "b"]

unique_logs = set(logs)

print("\nUnique logs:", unique_logs)


# -------------------------------
# 15. SET → LIST (ORDERED PROCESSING)
# -------------------------------
unique_list = list(unique_logs)

print("\nConverted back to list:", unique_list)


# -------------------------------
# 16. GROUPING / FILTERING PATTERN
# -------------------------------
blacklist = {"user3", "user5"}

incoming = ["user1", "user2", "user3", "user4"]

filtered = [u for u in incoming if u not in blacklist]

print("\nFiltered users:", filtered)


# -------------------------------
# 17. SET OPERATIONS REAL DATA COMPARISON
# -------------------------------
systemA = {"error", "info", "debug"}
systemB = {"error", "warning", "trace"}

print("\nCommon logs:", systemA & systemB)
print("Only A:", systemA - systemB)
print("Only B:", systemB - systemA)


# -------------------------------
# 18. SUBSET / SUPERSET / DISJOINT
# -------------------------------
x = {1, 2}
y = {1, 2, 3, 4}

print("\nSubset:", x <= y)
print("Superset:", y >= x)
print("Disjoint:", x.isdisjoint({5, 6}))


# -------------------------------
# 19. REAL DATA ENGINEERING PIPELINE (DEDUP + ANALYTICS)
# -------------------------------
events = [
    "user1",
    "user2",
    "user1",
    "user3",
    "user2",
    "user4"
]

# Step 1: deduplicate
unique_users = set(events)

# Step 2: convert for processing
processed = list(unique_users)

# Step 3: analytics
print("\nUnique users:", processed)
print("Total unique users:", len(unique_users))


# -------------------------------
# 20. FREQUENT PATTERN - FAST LOOKUP CACHE
# -------------------------------
cache = set()

def is_processed(item):
    if item in cache:
        return True
    cache.add(item)
    return False


print("\nCache check:")
print(is_processed("A"))
print(is_processed("A"))


# -------------------------------
# END OF SET CHEATSHEET
# -------------------------------