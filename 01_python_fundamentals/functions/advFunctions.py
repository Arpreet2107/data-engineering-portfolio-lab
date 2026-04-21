# ==========================================
# ADVANCED FUNCTIONS MASTER FILE
# ==========================================

from functools import partial, lru_cache
import asyncio
import time

# 1. TYPE HINT + DOCSTRING
def clean_data(data: str) -> str:
    """Clean string data"""
    return data.strip().lower()


# 2. CLOSURE
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply


# 3. FIRST-CLASS FUNCTION
def process(func, data):
    return [func(x) for x in data]


# 4. PARTIAL FUNCTION
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)


# 5. MEMOIZATION
@lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# 6. DECORATOR - RETRY
def retry(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                return func(*args, **kwargs)
            except Exception:
                time.sleep(1)
        return None
    return wrapper


@retry
def unstable():
    raise ValueError("Error!")


# 7. GENERATOR
def read_stream(data):
    for item in data:
        yield clean_data(item)


# 8. FUNCTION COMPOSITION
def transform_pipeline(data):
    return [clean_data(x) for x in data]


# 9. ASYNC FUNCTION
async def fetch():
    await asyncio.sleep(1)
    return "data"


async def async_main():
    result = await fetch()
    print(result)


# 10. IDEMPOTENT FUNCTION
def update_record(record, key, value):
    record[key] = value
    return record


# 11. ETL DESIGN
def extract(data):
    return data

def transform(data):
    return transform_pipeline(data)

def load(data):
    print("Loaded:", data)

def etl(data):
    load(transform(extract(data)))


# ==========================================
# RUN
# ==========================================
if __name__ == "__main__":
    data = [" Alice ", "Bob ", " CHARLIE"]

    print(process(lambda x: x*2, [1,2,3]))
    print(square(5))
    print(fibonacci(10))

    print(list(read_stream(data)))

    etl(data)

    asyncio.run(async_main())