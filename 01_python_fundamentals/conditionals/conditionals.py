# ================================
# PYTHON CONDITIONALS COMPLETE
# ================================

# 1. BASIC IF
age = 18
if age >= 18:
    print("Eligible to vote")

# 2. IF-ELSE
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. IF-ELIF-ELSE
score = 82
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
else:
    print("Grade C")

# 4. NESTED
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible for voting")

# 5. LOGICAL OPERATORS
salary = 60000
if age > 18 and salary > 30000:
    print("Loan Eligible")

# 6. COMPARISON
x = 10
y = 20

if x != y:
    print("Different values")

# 7. TERNARY
num = 4
result = "Even" if num % 2 == 0 else "Odd"
print(result)

# 8. MEMBERSHIP
text = "error occurred in system"
if "error" in text:
    print("Error detected")

# 9. IDENTITY
a = None
if a is None:
    print("Value is None")

# 10. TRUTHY / FALSY
data = []
if not data:
    print("Empty list")

# 11. MULTIPLE CONDITIONS
value = 15
if 10 < value < 20:
    print("Between 10 and 20")