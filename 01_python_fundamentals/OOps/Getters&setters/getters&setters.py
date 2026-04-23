"""
=========================================================
GETTERS & SETTERS - COMPLETE PRODUCTION STYLE MODULE
(Data Engineering Focus)
=========================================================

Covers:
- Traditional getters/setters
- @property (Pythonic way)
- Validation
- Read-only properties
- Computed properties
- Lazy loading
- Caching (manual + cached_property)
- @deleter
- Private vs protected
- Dataclasses + properties
- Descriptor protocol (advanced)
- Immutability design
- Thread safety basics
"""

from functools import cached_property
from dataclasses import dataclass
import threading


# =========================================================
# 1. TRADITIONAL GETTERS & SETTERS
# =========================================================

class Employee:
    def __init__(self, salary: float):
        self._salary = salary  # protected attribute

    def get_salary(self):
        return self._salary

    def set_salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value


# =========================================================
# 2. PYTHONIC GETTERS & SETTERS USING @property
# =========================================================

class EmployeeProperty:
    def __init__(self, salary: float):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value


# =========================================================
# 3. READ-ONLY PROPERTY
# =========================================================

class Config:
    def __init__(self):
        self._version = "1.0"

    @property
    def version(self):
        return self._version


# =========================================================
# 4. COMPUTED PROPERTY
# =========================================================

class DataStats:
    def __init__(self, values):
        self.values = values

    @property
    def average(self):
        return sum(self.values) / len(self.values)


# =========================================================
# 5. VALIDATION (DATA ENGINEERING STYLE)
# =========================================================

class UserRecord:
    def __init__(self, age):
        self.age = age  # triggers setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be int")
        if value < 0:
            raise ValueError("Invalid age")
        self._age = value


# =========================================================
# 6. LAZY LOADING (PERFORMANCE OPTIMIZATION)
# =========================================================

class BigDataLoader:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            print("Loading heavy data...")
            self._data = [i for i in range(10**6)]  # simulate heavy load
        return self._data


# =========================================================
# 7. MANUAL CACHING
# =========================================================

class CachedData:
    def __init__(self, values):
        self.values = values
        self._sum = None

    @property
    def total(self):
        if self._sum is None:
            print("Computing sum...")
            self._sum = sum(self.values)
        return self._sum


# =========================================================
# 8. cached_property (ADVANCED)
# =========================================================

class CachedDataAdvanced:
    def __init__(self, values):
        self.values = values

    @cached_property
    def total(self):
        print("Computing once...")
        return sum(self.values)


# =========================================================
# 9. @deleter
# =========================================================

class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name


# =========================================================
# 10. PRIVATE vs PROTECTED
# =========================================================

class PrivateExample:
    def __init__(self):
        self._protected = "I am protected"
        self.__private = "I am private"

    def get_private(self):
        return self.__private


# =========================================================
# 11. DATACLASS + PROPERTY
# =========================================================

@dataclass
class Product:
    price: float

    @property
    def price_with_tax(self):
        return self.price * 1.18


# =========================================================
# 12. DESCRIPTOR PROTOCOL (ADVANCED)
# =========================================================

class Descriptor:
    def __get__(self, obj, objtype=None):
        return "Getting value from descriptor"

    def __set__(self, obj, value):
        print(f"Setting value {value}")


class DescriptorExample:
    x = Descriptor()


# =========================================================
# 13. IMMUTABILITY DESIGN (READ-ONLY OBJECT)
# =========================================================

class ImmutableConfig:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


# =========================================================
# 14. THREAD SAFETY (BASIC)
# =========================================================

class ThreadSafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()

    @property
    def count(self):
        return self._count

    def increment(self):
        with self._lock:
            self._count += 1


# =========================================================
# 15. REAL-WORLD DATA PIPELINE EXAMPLE
# =========================================================

class DataPipelineRecord:
    def __init__(self, record: dict):
        self.record = record

    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, value):
        if not isinstance(value, dict):
            raise TypeError("Record must be a dictionary")

        # Example validation
        if "id" not in value:
            raise ValueError("Missing 'id' field")

        self._record = value

    @property
    def processed(self):
        """Computed property simulating transformation"""
        return {
            "id": self._record["id"],
            "status": "processed"
        }


# =========================================================
# TESTING / DEMO USAGE
# =========================================================

if __name__ == "__main__":

    # Basic usage
    emp = EmployeeProperty(50000)
    emp.salary = 60000
    print(emp.salary)

    # Validation
    user = UserRecord(25)
    print(user.age)

    # Lazy loading
    loader = BigDataLoader()
    print(loader.data[:5])

    # Cached property
    data = CachedDataAdvanced([1, 2, 3])
    print(data.total)
    print(data.total)  # cached

    # Dataclass
    product = Product(100)
    print(product.price_with_tax)

    # Descriptor
    d = DescriptorExample()
    print(d.x)

    # Thread-safe counter
    counter = ThreadSafeCounter()
    counter.increment()
    print(counter.count)

    # Data pipeline record
    record = DataPipelineRecord({"id": 1})
    print(record.processed)