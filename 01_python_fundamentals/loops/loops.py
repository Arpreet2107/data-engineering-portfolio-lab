# ================================
# PYTHON LOOPS COMPLETE
# ================================

# 1. FOR LOOP
for i in range(5):
    print("For:", i)

# 2. WHILE LOOP
count = 0
while count < 3:
    print("While:", count)
    count += 1

# 3. BREAK
for i in range(10):
    if i == 5:
        break
    print("Break:", i)

# 4. CONTINUE
for i in range(5):
    if i == 2:
        continue
    print("Continue:", i)

# 5. PASS
for i in range(3):
    pass

# 6. RANGE
for i in range(1, 10, 2):
    print("Range:", i)

# 7. ITERATING TYPES
# List
nums = [1, 2, 3]
for n in nums:
    print("List:", n)

# String
for ch in "data":
    print("Char:", ch)

# Dictionary
data = {"a": 1, "b": 2}
for k, v in data.items():
    print("Dict:", k, v)

# 8. NESTED LOOPS
for i in range(2):
    for j in range(2):
        print("Nested:", i, j)

# 9. LOOP ELSE
for i in range(3):
    print("Loop:", i)
else:
    print("Completed without break")

# 10. ENUMERATE
names = ["Alice", "Bob"]
for i, name in enumerate(names):
    print("Enumerate:", i, name)

# 11. ZIP
names = ["A", "B"]
scores = [90, 80]
for n, s in zip(names, scores):
    print("Zip:", n, s)

# 12. LIST COMPREHENSION
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# 13. GENERATOR
gen = (x**2 for x in range(5))
for val in gen:
    print("Generator:", val)