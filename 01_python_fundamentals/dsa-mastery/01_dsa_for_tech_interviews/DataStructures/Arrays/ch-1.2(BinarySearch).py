# 📌 BINARY SEARCH (WITH ALL CASES EXPLAINED)

# Binary Search:
# Works ONLY on sorted arrays
# Divide the search space into half every time

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # ✅ Found the element
        if arr[mid] == x:
            return mid
        
        # 🔍 Search in right half
        elif arr[mid] < x:
            left = mid + 1
        
        # 🔍 Search in left half
        else:
            right = mid - 1
    
    return -1  # ❌ Element not found



# 🟢 BEST CASE → O(1)
# Condition: Element is exactly at middle

arr_best = [1, 3, 5, 7, 9]
x_best = 5  # Middle element

result_best = binary_search(arr_best, x_best)

print("Best Case:")
print(f"Array: {arr_best}")
print(f"Searching: {x_best}")
print(f"Result Index: {result_best}")
print("Time Complexity: O(1)\n")



# 🟡 AVERAGE CASE → O(log n)
# Condition: Element found after few divisions

arr_avg = [1, 3, 5, 7, 9, 11, 13]
x_avg = 11

result_avg = binary_search(arr_avg, x_avg)

print("Average Case:")
print(f"Array: {arr_avg}")
print(f"Searching: {x_avg}")
print(f"Result Index: {result_avg}")
print("Time Complexity: O(log n)\n")



# 🔴 WORST CASE → O(log n)

# Condition 1: Element at extreme end
arr_worst_1 = [1, 3, 5, 7, 9, 11, 13]
x_worst_1 = 13

result_worst_1 = binary_search(arr_worst_1, x_worst_1)

# Condition 2: Element NOT present
arr_worst_2 = [1, 3, 5, 7, 9]
x_worst_2 = 100

result_worst_2 = binary_search(arr_worst_2, x_worst_2)

print("Worst Case (Last Position):")
print(f"Array: {arr_worst_1}")
print(f"Searching: {x_worst_1}")
print(f"Result Index: {result_worst_1}\n")

print("Worst Case (Not Present):")
print(f"Array: {arr_worst_2}")
print(f"Searching: {x_worst_2}")
print(f"Result Index: {result_worst_2}")
print("Time Complexity: O(log n)\n")



# 📊 FINAL SUMMARY

# Best Case    → O(1)     → Element at middle
# Average Case → O(log n) → Few divisions needed
# Worst Case   → O(log n) → Max divisions / Not found

# 👉 Overall Time Complexity = O(log n)