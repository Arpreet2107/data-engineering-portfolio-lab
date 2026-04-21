# ==========================================
# COMPLETE PYTHON FUNCTIONS (DATA ENGINEERING STYLE)
# ==========================================

# 1. BASIC FUNCTION
def add(a, b):
    return a + b


# 2. DEFAULT ARGUMENT
def greet(name="User"):
    return f"Hello {name}"


# 3. KEYWORD ARGUMENTS
def user_info(name, age):
    return f"{name} is {age} years old"


# 4. *args
def total_sum(*numbers):
    return sum(numbers)


# 5. **kwargs
def user_details(**data):
    return data


# 6. LAMBDA FUNCTION
square = lambda x: x * x


# 7. RECURSION
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# 8. HIGHER ORDER FUNCTION
def apply_function(func, value):
    return func(value)


# 9. DECORATOR
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper


@logger
def sample_task(x):
    return x * 2


# 10. GENERATOR FUNCTION
def read_large_file(lines):
    for line in lines:
        yield line.strip()


# 11. DATA CLEANING FUNCTION
def clean_record(record):
    return record.strip().lower()


# 12. PARSE LOG FUNCTION
def parse_log(line):
    parts = line.split(",")
    return {
        "user": parts[0],
        "action": parts[1]
    }


# 13. ETL PIPELINE FUNCTIONS
def extract(data):
    return data


def transform(data):
    return [parse_log(clean_record(d)) for d in data]


def load(data):
    print("Loading data...")
    for record in data:
        print(record)


def etl_pipeline(data):
    extracted = extract(data)
    transformed = transform(extracted)
    load(transformed)


# 14. ERROR HANDLING FUNCTION
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero error"


# 15. FILE PROCESSING FUNCTION (SIMULATED)
def process_file(lines):
    for line in lines:
        yield clean_record(line)


# ==========================================
# TEST EXECUTION
# ==========================================

if __name__ == "__main__":
    data = ["Alice,Login", "Bob,Logout", "Charlie,Login"]

    print(add(5, 3))
    print(greet())
    print(user_info(name="Arpreet", age=22))
    print(total_sum(1, 2, 3, 4))
    print(user_details(name="Arpreet", role="Engineer"))
    print(square(5))
    print(factorial(5))

    print(apply_function(lambda x: x + 10, 5))

    print(sample_task(10))

    print(list(read_large_file(data)))

    etl_pipeline(data)

    print(safe_divide(10, 0))