# ============================================
# MAP, FILTER, REDUCE — COMPLETE GUIDE
# ============================================

from functools import reduce
import operator
import json
from multiprocessing import Pool
from typing import List

# ============================================
# 1. MAP — BASIC USAGE
# ============================================

numbers = [1, 2, 3, 4, 5]

# Using lambda
squared = list(map(lambda x: x * x, numbers))
print("Squared (map):", squared)

# Using function
def square(x):
    return x * x

squared_func = list(map(square, numbers))
print("Squared (function):", squared_func)


# ============================================
# 2. MAP WITH MULTIPLE ITERABLES
# ============================================

a = [1, 2, 3]
b = [4, 5, 6]

added = list(map(lambda x, y: x + y, a, b))
print("Map with multiple iterables:", added)


# ============================================
# 3. FILTER — BASIC USAGE
# ============================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers (filter):", even_numbers)


# ============================================
# 4. FILTER WITH NONE (REMOVE FALSY VALUES)
# ============================================

data = [0, 1, "", "hello", None, 5]

cleaned = list(filter(None, data))
print("Filtered truthy values:", cleaned)


# ============================================
# 5. REDUCE — BASIC USAGE
# ============================================

numbers = [1, 2, 3, 4]

sum_result = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce:", sum_result)


# ============================================
# 6. REDUCE WITH INITIALIZER
# ============================================

sum_with_init = reduce(lambda a, b: a + b, numbers, 10)
print("Reduce with initializer:", sum_with_init)


# ============================================
# 7. USING OPERATOR MODULE (BEST PRACTICE)
# ============================================

sum_op = reduce(operator.add, numbers)
product_op = reduce(operator.mul, numbers)

print("Sum using operator:", sum_op)
print("Product using operator:", product_op)


# ============================================
# 8. ITEMGETTER (DATA ENGINEERING USE CASE)
# ============================================

from operator import itemgetter

records = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
]

ages = list(map(itemgetter("age"), records))
print("Extracted ages:", ages)


# ============================================
# 9. ITERATOR EXHAUSTION
# ============================================

mapped = map(lambda x: x * 2, [1, 2, 3])

print("First consumption:", list(mapped))
print("Second consumption (empty):", list(mapped))  # ❌ Empty


# ============================================
# 10. LIST COMPREHENSION (PREFERRED)
# ============================================

squared_lc = [x * x for x in numbers]
print("Squared (list comprehension):", squared_lc)


# ============================================
# 11. GENERATOR EXPRESSION (MEMORY EFFICIENT)
# ============================================

gen = (x * x for x in numbers)
print("Generator values:", list(gen))


# ============================================
# 12. FUNCTION COMPOSITION
# ============================================

def clean(x):
    return x.strip()

def to_int(x):
    return int(x)

data = [" 1 ", " 2 ", " 3 "]

result = list(map(lambda x: to_int(clean(x)), data))
print("Function composition:", result)


# ============================================
# 13. REAL-WORLD PIPELINE (LOG PROCESSING)
# ============================================

logs = [
    '{"user": "A", "status": 200, "response_time": 120}',
    '{"user": "B", "status": 500, "response_time": 300}',
    '{"user": "C", "status": 200, "response_time": 150}',
    '{"user": "D", "status": 404, "response_time": 80}'
]

# Step 1: Parse logs
parsed_logs = map(json.loads, logs)

# Step 2: Filter successful requests
successful_logs = filter(lambda x: x["status"] == 200, parsed_logs)

# Step 3: Extract response times
response_times = map(lambda x: x["response_time"], successful_logs)

# Step 4: Aggregate
total_time = reduce(lambda a, b: a + b, response_times)

print("Total Response Time:", total_time)


# ============================================
# 14. OPTIMIZED PIPELINE (GENERATOR + BUILT-IN)
# ============================================

logs = [
    '{"user": "A", "status": 200, "response_time": 120}',
    '{"user": "B", "status": 500, "response_time": 300}',
    '{"user": "C", "status": 200, "response_time": 150}',
]

pipeline = (
    json.loads(log)["response_time"]
    for log in logs
    if json.loads(log)["status"] == 200
)

total_time_optimized = sum(pipeline)
print("Optimized Total Time:", total_time_optimized)


# ============================================
# 15. PARALLEL MAP (MULTIPROCESSING)
# ============================================

def square_parallel(x):
    return x * x

if __name__ == "__main__":
    with Pool() as p:
        result = p.map(square_parallel, [1, 2, 3, 4])
    print("Parallel map:", result)


# ============================================
# 16. EDGE CASES
# ============================================

# Safe reduce with empty list
empty_safe = reduce(lambda a, b: a + b, [], 0)
print("Safe reduce on empty list:", empty_safe)

# Type error example (uncomment to test)
# list(map(lambda x: x + 1, ["a", "b"]))  # ❌ Error


# ============================================
# 17. TYPE HINTS (PRODUCTION STYLE)
# ============================================

def sum_list(nums: List[int]) -> int:
    return reduce(operator.add, nums, 0)

print("Typed sum function:", sum_list([1, 2, 3, 4]))


# ============================================
# END OF FILE
# ============================================