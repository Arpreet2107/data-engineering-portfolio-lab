# ==========================================
# PYTHON DICTIONARIES - COMPLETE CHEATSHEET
# DATA ENGINEERING / PRODUCTION STYLE
# ==========================================

# -------------------------------
# 1. CREATE DICTIONARIES
# -------------------------------
empty_dict = {}

user = {
    "id": 101,
    "name": "Alice",
    "role": "data engineer"
}

print("Initial dict:", user)


# -------------------------------
# 2. ACCESS VALUES
# -------------------------------
print("\nAccess values:")
print(user["name"])          # direct access

# safe access (VERY IMPORTANT IN PRODUCTION)
print(user.get("salary", "Not Found"))


# -------------------------------
# 3. ADD / UPDATE VALUES
# -------------------------------
user["city"] = "Singapore"   # add new key
user["role"] = "senior DE"   # update existing

print("\nAfter update:")
print(user)


# -------------------------------
# 4. DELETE OPERATIONS
# -------------------------------
data = {"a": 1, "b": 2, "c": 3}

del data["a"]               # delete by key
removed = data.pop("b")     # remove + return value

print("\nAfter deletion:")
print(data, "removed:", removed)


# -------------------------------
# 5. keys(), values(), items()
# -------------------------------
print("\nKeys:", user.keys())
print("Values:", user.values())

print("\nIteration using items():")
for k, v in user.items():
    print(k, "->", v)


# -------------------------------
# 6. update() - MERGE DICTS
# -------------------------------
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

a.update(b)

print("\nAfter merge:")
print(a)


# -------------------------------
# 7. setdefault() - GROUPING PATTERN
# -------------------------------
logs = {}

logs.setdefault("error", []).append("DB failed")
logs.setdefault("info", []).append("job started")

print("\nsetdefault grouping:")
print(logs)


# -------------------------------
# 8. DICTIONARY COMPREHENSION
# -------------------------------
nums = [1, 2, 3, 4]

squares = {x: x*x for x in nums}

print("\nDict comprehension:")
print(squares)


# -------------------------------
# 9. NESTED DICTIONARY (REAL DATA MODEL)
# -------------------------------
user_profile = {
    "id": 1,
    "profile": {
        "name": "Alice",
        "location": "SG"
    }
}

print("\nNested access:")
print(user_profile["profile"]["name"])


# -------------------------------
# 10. FLATTEN JSON (ETL USE CASE)
# -------------------------------
raw_data = {
    "user": {
        "id": 1,
        "name": "Alice"
    }
}

flattened = {
    "id": raw_data["user"]["id"],
    "name": raw_data["user"]["name"]
}

print("\nFlattened dict:")
print(flattened)


# -------------------------------
# 11. GROUPING DATA (VERY IMPORTANT IN DE)
# -------------------------------
events = [
    {"type": "error", "msg": "DB failed"},
    {"type": "info", "msg": "job started"},
    {"type": "error", "msg": "timeout"}
]

grouped = {}

for event in events:
    t = event["type"]
    grouped.setdefault(t, []).append(event["msg"])

print("\nGrouped logs:")
print(grouped)


# -------------------------------
# 12. SORT DICTIONARY
# -------------------------------
scores = {"a": 3, "b": 1, "c": 2}

sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1]))

print("\nSorted dict:")
print(sorted_scores)


# -------------------------------
# 13. SAFE HANDLING (get + default)
# -------------------------------
config = {}

timeout = config.get("timeout", 30)

print("\nConfig timeout:", timeout)


# -------------------------------
# 14. COPY (SHALLOW COPY)
# -------------------------------
original = {"x": 1, "y": {"z": 2}}

shallow = original.copy()

shallow["x"] = 100

print("\nShallow copy:")
print(original, shallow)


# -------------------------------
# 15. DEEP COPY (IMPORTANT FOR REAL SYSTEMS)
# -------------------------------
import copy

deep = copy.deepcopy(original)

deep["y"]["z"] = 999

print("\nDeep copy:")
print(original, deep)


# -------------------------------
# 16. JSON ↔ DICT (API / ETL CORE)
# -------------------------------
import json

json_str = '{"name": "Alice", "age": 25}'

dict_data = json.loads(json_str)

print("\nJSON to dict:")
print(dict_data)


# -------------------------------
# 17. MERGE DICTS (MODERN PYTHON 3.9+)
# -------------------------------
a = {"x": 1}
b = {"y": 2}

c = a | b

print("\nModern merge:")
print(c)


# -------------------------------
# 18. FREQUENCY COUNT (REAL USE CASE)
# -------------------------------
logs = ["error", "info", "error", "debug", "error"]

freq = {}

for log in logs:
    freq[log] = freq.get(log, 0) + 1

print("\nFrequency count:")
print(freq)


# -------------------------------
# 19. REAL ETL PIPELINE EXAMPLE
# -------------------------------
pipeline_logs = [
    {"level": "ERROR", "msg": "DB failed"},
    {"level": "INFO", "msg": "Job started"},
    {"level": "ERROR", "msg": "Timeout"}
]

# Step 1: group by level
log_store = {}

for log in pipeline_logs:
    level = log["level"]
    log_store.setdefault(level, []).append(log["msg"])

# Step 2: analytics
error_count = len(log_store.get("ERROR", []))

print("\nETL Pipeline Output:")
print("Grouped Logs:", log_store)
print("Error Count:", error_count)


# -------------------------------
# END OF DICTIONARY CHEATSHEET
# -------------------------------