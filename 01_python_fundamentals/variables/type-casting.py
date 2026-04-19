# 1. Implicit Type Casting
# Implicit type casting occurs when Python automatically converts one data type to another without any user intervention. This typically happens to avoid data loss by promoting a "lower" data type (like an integer) to a "higher" one (like a float). 
# Medium
# Medium
#  +3
# Example: Adding an Integer and a Float
# python
num_int = 10     # <class 'int'>
num_flo = 5.5    # <class 'float'>

# Python automatically converts num_int to float before addition
result = num_int + num_flo 

print(result)       # Output: 15.5
print(type(result)) # Output: <class 'float'>
# Use code with caution.
# In this case, Python promotes the integer to a float so that the addition can be completed accurately. 

# 2. Explicit Type Casting
# Explicit type casting (also called Type Conversion) is when a programmer manually changes
# a data type using built-in constructor functions like int(), float(), or str(). 
# This is necessary when Python cannot automatically resolve mixed types, 
# such as adding a number to a string. 
# Example: Converting String to Integer
num_str = "25"   # <class 'str'>
num_int = 10     # <class 'int'>

# This would cause a TypeError: result = num_str + num_int

# Manually convert string to int to allow math
converted_num = int(num_str) 
result = converted_num + num_int

print(result) # Output: 35
Use code with caution.
# Common Explicit Casting Functions:
# int(x): Converts x to a whole number. If x is a float, it truncates the decimal (e.g., int(3.9) becomes 3).
# float(x): Converts x to a floating-point number (e.g., float(10) becomes 10.0).
# str(x): Converts x to its string representation (e.g., str(42) becomes "42").