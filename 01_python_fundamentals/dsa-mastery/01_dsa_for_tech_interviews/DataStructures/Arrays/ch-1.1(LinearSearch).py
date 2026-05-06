# 📌 LINEAR SEARCH (WITH ALL CASES EXPLAINED)

# Linear Search:
# Check each element one by one until we find the target

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i   # ✅ Found → return index
    return -1          # ❌ Not found



# 🟢 BEST CASE → O(1)
# Condition: Element is at FIRST position

arr_best = [15, 1, 8, 9, 12]
x_best = 15

result_best = linear_search(arr_best, x_best)

# Only 1 comparison → constant time
print("Best Case:")
print(f"Array: {arr_best}")
print(f"Searching: {x_best}")
print(f"Result Index: {result_best}")
print("Time Complexity: O(1)\n")


# 🟡 AVERAGE CASE → O(n)

# Condition: Element is somewhere in the middle

arr_avg = [2, 1, 8, 9, 12, 15]
x_avg = 9

result_avg = linear_search(arr_avg, x_avg)

# About n/2 comparisons → still O(n)
print("Average Case:")
print(f"Array: {arr_avg}")
print(f"Searching: {x_avg}")
print(f"Result Index: {result_avg}")
print("Time Complexity: O(n)\n")


# 🔴 WORST CASE → O(n)

# Condition 1: Element is at LAST position
arr_worst_1 = [2, 1, 8, 9, 12, 15]
x_worst_1 = 15

result_worst_1 = linear_search(arr_worst_1, x_worst_1)

# Condition 2: Element NOT present
arr_worst_2 = [2, 1, 8, 9, 12]
x_worst_2 = 100

result_worst_2 = linear_search(arr_worst_2, x_worst_2)

print("Worst Case (Last Position):")
print(f"Array: {arr_worst_1}")
print(f"Searching: {x_worst_1}")
print(f"Result Index: {result_worst_1}\n")

print("Worst Case (Not Present):")
print(f"Array: {arr_worst_2}")
print(f"Searching: {x_worst_2}")
print(f"Result Index: {result_worst_2}")
print("Time Complexity: O(n)\n")

# 📊 FINAL SUMMARY

# Best Case    → O(1)  → First element
# Average Case → O(n)  → Middle element
# Worst Case   → O(n)  → Last / Not found

# 👉 Overall Time Complexity = O(n)