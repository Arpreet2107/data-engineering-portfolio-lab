# ================================
# PYTHON LISTS - COMPLETE CHEATSHEET
# DATA ENGINEERING STYLE IMPLEMENTATION
# ================================

# -------------------------------
# 1. CREATE LISTS
# -------------------------------
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "log", 3.14, True]

print("Initial Lists:")
print(empty_list, numbers, mixed)


# -------------------------------
# 2. APPEND (ADD SINGLE ELEMENT)
# Used in streaming ingestion
# -------------------------------
logs = []

logs.append("INFO: pipeline started")
logs.append("ERROR: DB connection failed")

print("\nAfter append:")
print(logs)


# -------------------------------
# 3. EXTEND (ADD MULTIPLE ELEMENTS)
# Used in batch ingestion
# -------------------------------
batch1 = [1, 2, 3]
batch2 = [4, 5, 6]

batch1.extend(batch2)

print("\nAfter extend:")
print(batch1)


# -------------------------------
# 4. INSERT (ADD AT INDEX)
# Used in priority reordering
# -------------------------------
data = [1, 3, 4]

data.insert(1, 2)

print("\nAfter insert:")
print(data)


# -------------------------------
# 5. REMOVE (DELETE BY VALUE)
# Used in data cleaning
# -------------------------------
data_remove = [10, 20, 30, 20]

data_remove.remove(20)

print("\nAfter remove:")
print(data_remove)


# -------------------------------
# 6. POP (DELETE BY INDEX)
# Used in queue processing
# -------------------------------
queue = [100, 200, 300]

last = queue.pop()
first = queue.pop(0)

print("\nPop results:")
print("last:", last, "first:", first)
print("queue:", queue)


# -------------------------------
# 7. CLEAR (EMPTY LIST)
# Used in ETL batch reset
# -------------------------------
temp = [1, 2, 3]
temp.clear()

print("\nAfter clear:")
print(temp)


# -------------------------------
# 8. INDEX (FIND POSITION)
# Used in debugging pipelines
# -------------------------------
positions = [10, 20, 30, 40]

print("\nIndex of 30:")
print(positions.index(30))


# -------------------------------
# 9. COUNT (FREQUENCY ANALYSIS)
# Used in log analytics
# -------------------------------
logs_count = ["ERROR", "INFO", "ERROR", "DEBUG", "ERROR"]

print("\nError count:")
print(logs_count.count("ERROR"))


# -------------------------------
# 10. SORT (ASCENDING ORDER)
# Used in ranking, time-series
# -------------------------------
values = [5, 2, 9, 1]

values.sort()

print("\nSorted ascending:")
print(values)

values.sort(reverse=True)

print("Sorted descending:")
print(values)


# -------------------------------
# 11. REVERSE
# Used in LIFO / latest-first processing
# -------------------------------
order = [1, 2, 3, 4]

order.reverse()

print("\nReversed:")
print(order)


# -------------------------------
# 12. COPY (VERY IMPORTANT)
# Avoids reference bugs in pipelines
# -------------------------------
a = [1, 2, 3]
b = a.copy()

b.append(4)

print("\nCopy test:")
print("a:", a)
print("b:", b)


# -------------------------------
# 13. LIST COMPREHENSION
# CORE DATA ENGINEERING TOOL
# -------------------------------
nums = [1, 2, 3, 4, 5]

squares = [x * x for x in nums]
evens = [x for x in nums if x % 2 == 0]

print("\nComprehensions:")
print("squares:", squares)
print("evens:", evens)


# -------------------------------
# 14. NESTED LISTS (REAL DATA ROWS)
# -------------------------------
records = [
    ["user1", 25],
    ["user2", 30],
    ["user3", 28]
]

print("\nNested list access:")
print(records[0])      # first row
print(records[0][0])   # first column


# -------------------------------
# 15. FLATTEN LIST (VERY COMMON IN ETL)
# -------------------------------
nested = [[1, 2], [3, 4], [5, 6]]

flattened = [x for sublist in nested for x in sublist]

print("\nFlattened list:")
print(flattened)


# -------------------------------
# 16. CHUNKING (BATCH PROCESSING)
# Used in ETL pipelines / API pagination
# -------------------------------
data_stream = list(range(10))

chunk_size = 3

chunks = [
    data_stream[i:i + chunk_size]
    for i in range(0, len(data_stream), chunk_size)
]

print("\nChunks:")
print(chunks)


# -------------------------------
# 17. REAL WORLD PIPELINE EXAMPLE
# LOG PROCESSING SYSTEM
# -------------------------------
logs_stream = [
    "INFO:user login",
    "ERROR:db failure",
    "INFO:data loaded",
    "ERROR:timeout",
    "DEBUG:cache hit"
]

# Step 1: Filter errors
error_logs = [log for log in logs_stream if "ERROR" in log]

# Step 2: Extract messages
error_messages = [log.split(":")[1] for log in error_logs]

# Step 3: Clean data
clean_errors = [msg.strip().upper() for msg in error_messages]

# Step 4: Batch for DB insertion
batch_size = 2

batches = [
    clean_errors[i:i + batch_size]
    for i in range(0, len(clean_errors), batch_size)
]

print("\nPipeline Output:")
print("Errors:", error_logs)
print("Clean:", clean_errors)
print("Batches:", batches)


# -------------------------------
# END OF CHEATSHEET
# -------------------------------