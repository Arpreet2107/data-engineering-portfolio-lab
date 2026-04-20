# ==========================================
# PYTHON TUPLES - COMPLETE CHEATSHEET
# DATA ENGINEERING / PRODUCTION STYLE
# ==========================================

# -------------------------------
# 1. CREATE TUPLES
# -------------------------------
empty_tuple = ()

numbers = (1, 2, 3, 4)

mixed = (1, "Alice", 25, True)

single_element = (5,)   # IMPORTANT: comma required

not_a_tuple = (5)       # ❌ This is just an integer

print("Tuples created:")
print(numbers, mixed, single_element)


# -------------------------------
# 2. ACCESS ELEMENTS
# -------------------------------
data = (10, 20, 30, 40)

print("\nAccessing elements:")
print(data[0])
print(data[-1])


# -------------------------------
# 3. IMMUTABILITY DEMO (VERY IMPORTANT)
# -------------------------------
immutable = (1, 2, 3)

# immutable[0] = 100   # ❌ ERROR (tuples cannot be modified)

print("\nTuple is immutable:", immutable)


# -------------------------------
# 4. CONCATENATION
# -------------------------------
a = (1, 2)
b = (3, 4)

result = a + b

print("\nConcatenation:")
print(result)


# -------------------------------
# 5. REPETITION
# -------------------------------
repeat = (1, 2) * 3

print("\nRepetition:")
print(repeat)


# -------------------------------
# 6. MEMBERSHIP TEST
# -------------------------------
t = (1, 2, 3, 4)

print("\nMembership test:")
print(2 in t)
print(10 in t)


# -------------------------------
# 7. LENGTH
# -------------------------------
print("\nLength of tuple:")
print(len(t))


# -------------------------------
# 8. TUPLE UNPACKING (VERY IMPORTANT)
# -------------------------------
record = (101, "Alice", "Data Engineer")

id, name, role = record

print("\nUnpacking:")
print(id, name, role)


# -------------------------------
# 9. SWAPPING VARIABLES
# -------------------------------
a = 10
b = 20

a, b = b, a

print("\nSwapping:")
print(a, b)


# -------------------------------
# 10. RETURN MULTIPLE VALUES (FUNCTIONS)
# -------------------------------
def get_user():
    return 1, "Alice", 25

user = get_user()

print("\nFunction returning tuple:")
print(user)


# -------------------------------
# 11. NESTED TUPLES
# -------------------------------
nested = (1, (2, 3), 4)

print("\nNested tuple access:")
print(nested[1])
print(nested[1][0])


# -------------------------------
# 12. EXTENDED UNPACKING (*)
# -------------------------------
data = (1, 2, 3, 4, 5)

a, *middle, b = data

print("\nExtended unpacking:")
print(a)
print(middle)
print(b)


# -------------------------------
# 13. TUPLE METHODS
# -------------------------------
t = (1, 2, 2, 3, 4)

print("\nCount method:")
print(t.count(2))

print("Index method:")
print(t.index(3))


# -------------------------------
# 14. TUPLE AS DICTIONARY KEY (VERY IMPORTANT)
# -------------------------------
location_map = {}

location_map[(28.6, 77.2)] = "Delhi"
location_map[(1.3, 103.8)] = "Singapore"

print("\nTuple as dict key:")
print(location_map)


# -------------------------------
# 15. LIST → TUPLE CONVERSION
# -------------------------------
lst = [1, 2, 3, 4]

tup = tuple(lst)

print("\nList to tuple:")
print(tup)


# -------------------------------
# 16. TUPLE → LIST CONVERSION
# -------------------------------
back_to_list = list(tup)

print("\nTuple to list:")
print(back_to_list)


# -------------------------------
# 17. REAL DATA ENGINEERING EXAMPLE (EVENT PIPELINE)
# -------------------------------
events = [
    (1, "login", "2026-01-01"),
    (2, "click", "2026-01-01"),
    (3, "logout", "2026-01-01")
]

print("\nProcessing event stream:")

for event in events:
    user_id, action, timestamp = event
    print(user_id, action, timestamp)


# -------------------------------
# 18. IMMUTABLE PIPELINE RECORDS
# -------------------------------
def process_record(record):
    user_id, event, ts = record
    return f"Processed {user_id} - {event}"

record = (101, "login", "2026-01-01")

print("\nPipeline processing:")
print(process_record(record))


# -------------------------------
# 19. CACHE KEY USING TUPLE (REAL SYSTEM DESIGN)
# -------------------------------
cache = {}

key = ("user123", "profile", 2026)

cache[key] = "cached_data"

print("\nCache system using tuple keys:")
print(cache)


# -------------------------------
# 20. REAL ETL PIPELINE SIMULATION
# -------------------------------
raw_data = [
    (1, "error", "DB failed"),
    (2, "info", "job started"),
    (3, "error", "timeout")
]

print("\nETL Pipeline:")

for row in raw_data:
    user_id, level, message = row

    if level == "error":
        print("ERROR LOG:", user_id, message)


# -------------------------------
# END OF TUPLE CHEATSHEET
# -------------------------------   