# ============================================
# 🧠 DECORATORS PRACTICE — BASIC → ADVANCED
# ============================================

# --------------------------------------------
# 🟢 LEVEL 1: BASIC DECORATOR
# --------------------------------------------

# Q1: Create a decorator that prints "Start" before a function
# and "End" after the function runs.

def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@start_end_decorator
def say_hello():
    print("Hello!")

say_hello()


# --------------------------------------------
# 🟡 LEVEL 2: HANDLE ARGUMENTS
# --------------------------------------------

# Q2: Modify decorator to work with functions that take arguments

def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        func(*args, **kwargs)
        print("After execution")
    return wrapper

@decorator_with_args
def greet(name):
    print(f"Hello {name}")

greet("Arpreet")


# --------------------------------------------
# 🟡 LEVEL 3: RETURN VALUES
# --------------------------------------------

# Q3: Create decorator that returns result of function

def return_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@return_decorator
def add(a, b):
    return a + b

print(add(3, 5))


# --------------------------------------------
# 🔴 LEVEL 4: TIMER DECORATOR
# --------------------------------------------

# Q4: Measure execution time of function

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.5f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Function complete")

slow_function()


# --------------------------------------------
# 🔴 LEVEL 5: AUTHENTICATION DECORATOR
# --------------------------------------------

# Q5: Allow function only if user is "admin"

def require_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access Denied")
            return
        return func(user)
    return wrapper

@require_admin
def delete_data(user):
    print("Data deleted!")

delete_data("guest")
delete_data("admin")


# --------------------------------------------
# 🔴 LEVEL 6: REPEAT FUNCTION (DECORATOR WITH ARGUMENT)
# --------------------------------------------

# Q6: Repeat function N times

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()


# --------------------------------------------
# 🔴 LEVEL 7: LOGGING DECORATOR
# --------------------------------------------

# Q7: Log function name and arguments

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def multiply(a, b):
    return a * b

print(multiply(4, 5))


# --------------------------------------------
# 🔴 LEVEL 8: CACHING (MEMOIZATION)
# --------------------------------------------

# Q8: Store results to avoid recomputation

def cache(func):
    memory = {}
    def wrapper(n):
        if n in memory:
            print("Returning from cache")
            return memory[n]
        result = func(n)
        memory[n] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(10))  # cached


# --------------------------------------------
# 🔴 LEVEL 9: USING functools.wraps
# --------------------------------------------

# Q9: Preserve original function metadata

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def sample():
    """This is a sample function"""
    pass

print(sample.__name__)  # should print 'sample'


# --------------------------------------------
# 🔴 LEVEL 10: STACKING DECORATORS
# --------------------------------------------

# Q10: Apply multiple decorators

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def final_function():
    print("Final Function")

final_function()
