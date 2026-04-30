#1
class Student:
    def __init__(self):
        self.name = None
        self.age = None

    def get_info(self):
        print("The name of this Student is", self.name)
        print("The age of this Student is", self.age)


# main equivalent
s1 = Student()
s1.name = "Aman"
s1.age = 24
s1.get_info()

s2 = Student()

#2
class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


s1 = Student("Arpreet", 20)
s1.get_info()

#3🟢 1. Non-Parameterized Constructor (No Arguments)
class Student:
    def __init__(self):
        print("Constructor called")
        self.name = None
        self.age = None

s1 = Student()

#4🟡 2. Parameterized Constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Arpreet", 20)
s2 = Student("Rahul", 22)

#5🔴 3. Copy Constructor (Python Way)
#Python doesn’t have a built-in copy constructor like Java/C++, but you can simulate it:
#✅ Method 1: Custom Copy Constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def copy(cls, other):
        return cls(other.name, other.age)


s1 = Student("Arpreet", 20)
s2 = Student.copy(s1)

print(s2.name, s2.age)

#6✅ Method 2: Using copy module (Advanced)
import copy

s2 = copy.copy(s1)      # shallow copy
s3 = copy.deepcopy(s1)  # deep copy

#7🧠 Destructor in Python
#Python DOES have something similar:

class Student:
    def __del__(self):
        print("Object destroyed")
#⚠️ But:
# Not reliable for memory management
# Python uses Garbage Collector automatically

#7
class Student:
    def display_info(self, name=None, age=None):
        if name is not None and age is None:
            print(name)
        elif age is not None and name is None:
            print(age)
        elif name is not None and age is not None:
            print(name)
            print(age)
        else:
            print("No data provided")


s = Student()

s.display_info("Arpreet")     # name only
s.display_info(age=20)        # age only
s.display_info("Arpreet", 20) # both

#8
class Student:
    def display_info(self, *args):
        if len(args) == 1:
            print(args[0])
        elif len(args) == 2:
            print(args[0])
            print(args[1])
        else:
            print("Invalid input")


s = Student()

s.display_info("Arpreet")
s.display_info(20)
s.display_info("Arpreet", 20)

#9
class Student:
    def display_info(self, name):
        print(f"Name: {name}")
    
    def display_info(self, age):  # This overrides the previous method
        print(f"Age: {age}")

s = Student()
s.display_info(20)  # Works
# s.display_info("John")  # Error! Because display_info now expects age parameter

#10Workarounds for Method Overloading in Python
# Method 1: Use Default Parameters
class Student:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    
    def display_info(self, name=None, age=None):
        if name is not None and age is not None:
            print(f"Name: {name}, Age: {age}")
        elif name is not None:
            print(f"Name: {name}")
        elif age is not None:
            print(f"Age: {age}")
        else:
            print("No information provided")

# Usage
s = Student()
s.display_info("Alice")
s.display_info(25)
s.display_info("Bob", 30)
s.display_info()
#11 Method 2: Use *args and **kwargs
class Calculator:
    def add(self, *args):
        """Accepts variable number of arguments"""
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return sum(args)

calc = Calculator()
print(calc.add(5, 10))        # 2 parameters → 15
print(calc.add(5, 10, 15))    # 3 parameters → 30
print(calc.add(1, 2, 3, 4))   # many parameters → 10
#12 Method 3: Use singledispatch (Function Overloading)
from functools import singledispatch

@singledispatch
def process(value):
    print(f"Default: {value}")

@process.register(int)
def _(value):
    print(f"Integer: {value * 2}")

@process.register(str)
def _(value):
    print(f"String: {value.upper()}")

@process.register(list)
def _(value):
    print(f"List length: {len(value)}")

# Usage
process(10)        # Integer: 20
process("hello")   # String: HELLO
process([1, 2, 3]) # List length: 3
process(3.14)      # Default: 3.14
# Operator Overloading (Python's form of compile-time polymorphism)
# Python allows operators to have different meanings based on the operands.

#13 
# Same + operator works with different data types
print(10 + 5)        # Integer addition → 15
print("Hello" + " " + "World")  # String concatenation → Hello World
print([1, 2] + [3, 4])  # List concatenation → [1, 2, 3, 4]

# Overloading operators in custom classes
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):  # Overloads + operator
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Vector(6, 8)

#14 Runtime Polymorphism (Dynamic) in Python
class Shape:
    def area(self):
        print("Displays Area of Shape (Parent method)")
        return 0

class Triangle(Shape):
    def area(self, base=None, height=None):  # Overriding
        if base and height:
            result = 0.5 * base * height  # Note: 1/2 in Python 3 works correctly
            print(f"Triangle Area: {result}")
            return result
        else:
            print("Triangle area needs base and height")
            return 0
    
    def area(self):  # Simpler override matching parent signature
        print("Triangle: Area calculation requires base and height")

class Circle(Shape):
    def area(self, radius=None):
        if radius:
            result = 3.14 * radius * radius
            print(f"Circle Area: {result}")
            return result
        else:
            print("Circle area needs radius")
            return 0

class Rectangle(Shape):
    def area(self, length=None, breadth=None):
        if length and breadth:
            result = length * breadth
            print(f"Rectangle Area: {result}")
            return result
        else:
            print("Rectangle area needs length and breadth")
            return 0

# Runtime polymorphism - same method call behaves differently
shapes = [Triangle(), Circle(), Rectangle()]

# This demonstrates runtime polymorphism
for shape in shapes:
    shape.area()  # Different implementations called at runtime

#15 Complete Example with Proper Method Overriding
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} makes a generic sound")
    
    def move(self):
        print(f"{self.name} moves")

class Dog(Animal):
    def make_sound(self):  # Overriding parent method
        print(f"{self.name} barks: Woof! Woof!")
    
    def move(self):
        print(f"{self.name} runs on four legs")

class Cat(Animal):
    def make_sound(self):  # Overriding parent method
        print(f"{self.name} meows: Meow! Meow!")
    
    def move(self):
        print(f"{self.name} walks gracefully")

class Bird(Animal):
    def make_sound(self):  # Overriding parent method
        print(f"{self.name} chirps: Tweet! Tweet!")
    
    def move(self):
        print(f"{self.name} flies in the sky")

# Runtime polymorphism in action
def animal_activity(animal):
    """Same function works with different animal types"""
    animal.make_sound()  # Runtime decides which version to call
    animal.move()
    print("-" * 30)

# Different objects, same interface
animals = [Dog("Buddy"), Cat("Whiskers"), Bird("Tweety")]

for animal in animals:
    animal_activity(animal)

#16 Duck Typing (Python's Unique Approach to Polymorphism)
class Duck:
    def sound(self):
        return "Quack!"
    
    def walk(self):
        return "Walks like a duck"

class Person:
    def sound(self):
        return "I can quack too!"
    
    def walk(self):
        return "Walks like a human pretending to be a duck"

class Robot:
    def sound(self):
        return "Beep boop - quack sequence initiated"
    
    def walk(self):
        return "Walks mechanically"

# Polymorphic function - doesn't care about object type
def make_it_quack_and_walk(obj):
    """Any object with sound() and walk() methods works"""
    print(obj.sound())
    print(obj.walk())
    print("-" * 30)

# All different types work because they have the required methods
duck = Duck()
person = Person()
robot = Robot()

make_it_quack_and_walk(duck)
make_it_quack_and_walk(person)
make_it_quack_and_walk(robot)

#17 Polymorphism with Built-in Functions
# len() function works with different types
print(len("Python"))        # String → 6
print(len([1, 2, 3, 4]))    # List → 4
print(len({"a": 1, "b": 2})) # Dict → 2
print(len((10, 20, 30)))    # Tuple → 3

# Custom class with __len__ method
class Library:
    def __init__(self, books):
        self.books = books
    
    def __len__(self):
        return len(self.books)

lib = Library(["Book1", "Book2", "Book3"])
print(len(lib))  # 3

#15 1. Single Inheritance
#Definition: When one class inherits from another class (one parent, one child).
# Parent class (Base class)
class Shape:
    def area(self):
        print("Displays Area of Shape")
        return 0

# Child class (Derived class) inheriting from Shape
class Triangle(Shape):
    def area(self, h, b):
        result = (1/2) * b * h
        print(f"Triangle Area: {result}")
        return result

# Usage
shape = Shape()
triangle = Triangle()

shape.area()                    # Calls parent method
triangle.area(5, 10)            # Calls child method (overrides)
#Output:
# Displays Area of Shape
# Triangle Area: 25.0
#Complete Single Inheritance Example

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking: Woof! Woof!")

# Usage
dog = Dog("Buddy")
dog.eat()      # Inherited from Animal
dog.sleep()    # Inherited from Animal
dog.bark()     # Defined in Dog

#17 Hierarchical Inheritance
#Definition: When multiple child classes inherit from the same parent class.
# Parent class (Base class)
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        print(f"{self.name} - Displaying area (parent method)")
        return 0

# Child class 1
class Triangle(Shape):
    def area(self, h, b):
        result = (1/2) * b * h
        print(f"{self.name} - Triangle Area: {result}")
        return result

# Child class 2
class Circle(Shape):
    def area(self, r):
        result = 3.14 * r * r
        print(f"{self.name} - Circle Area: {result}")
        return result

# Child class 3
class Rectangle(Shape):
    def area(self, l, w):
        result = l * w
        print(f"{self.name} - Rectangle Area: {result}")
        return result

# Usage
triangle = Triangle("Triangle Shape")
circle = Circle("Circle Shape")
rectangle = Rectangle("Rectangle Shape")

triangle.area(5, 10)    # 0.5 * 10 * 5 = 25.0
circle.area(7)          # 3.14 * 49 = 153.86
rectangle.area(4, 6)    # 4 * 6 = 24

#18Real-world Example: Employee Hierarchy

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(f"{self.name} is working")
    
    def get_salary(self):
        print(f"{self.name}'s salary: ${self.salary}")

class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code")
    
    def debug(self):
        print(f"{self.name} is debugging")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing team")
    
    def conduct_meeting(self):
        print(f"{self.name} is conducting meeting")

class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing UI/UX")
    
    def create_mockup(self):
        print(f"{self.name} is creating mockups")

# All inherit from same parent
dev = Developer("Alice", 80000)
mgr = Manager("Bob", 100000)
designer = Designer("Carol", 75000)

dev.work()          # Alice is writing code
mgr.work()          # Bob is managing team
designer.work()     # Carol is designing UI/UX
#Multilevel Inheritance
# Definition: When a class inherits from another derived class (forming a chain of inheritance).

# Level 1: Grandparent class
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        print(f"{self.name} - Displaying area")
        return 0

# Level 2: Parent class (inherits from Shape)
class Triangle(Shape):
    def __init__(self, name, sides=3):
        super().__init__(name)  # Call parent constructor
        self.sides = sides
    
    def area(self, h, b):
        result = (1/2) * b * h
        print(f"{self.name} - Triangle Area: {result}")
        return result

# Level 3: Child class (inherits from Triangle)
class EquilateralTriangle(Triangle):
    def __init__(self, name, side_length):
        super().__init__(name)  # Calls Triangle's constructor
        self.side = side_length
    
    def area(self, h=None, b=None):
        # Equilateral triangle specific formula
        result = (3**0.5 / 4) * (self.side ** 2)
        print(f"{self.name} - Equilateral Triangle Area: {result}")
        return result
    
    def display_properties(self):
        print(f"Shape: {self.name}")
        print(f"Number of sides: {self.sides}")
        print(f"Side length: {self.side}")

# Usage
shape = Shape("Generic Shape")
triangle = Triangle("Right Triangle")
equilateral = EquilateralTriangle("Equilateral Triangle", 6)

shape.area()                      # Generic Shape - Displaying area
triangle.area(5, 10)              # Right Triangle - Triangle Area: 25.0
equilateral.area()                # Equilateral Triangle Area: 15.588
equilateral.display_properties()  # Shows all properties from all levels

# Level 1: Grandparent
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model} is starting")
    
    def stop(self):
        print(f"{self.brand} {self.model} is stopping")

# Level 2: Parent
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def honk(self):
        print(f"{self.brand} {self.model} honks: Beep Beep!")

# Level 3: Child
class ElectricCar(Car):
    def __init__(self, brand, model, doors, battery_capacity):
        super().__init__(brand, model, doors)
        self.battery_capacity = battery_capacity
    
    def start(self):  # Overriding
        print(f"{self.brand} {self.model} starts silently (electric motor)")
    
    def charge(self):
        print(f"Charging {self.brand} {self.model} - {self.battery_capacity}kWh battery")

# Usage
tesla = ElectricCar("Tesla", "Model 3", 4, 75)
tesla.start()    # Overridden method
tesla.honk()     # Inherited from Car
tesla.charge()   # Defined in ElectricCar
tesla.stop()     # Inherited from Vehicle

#Multiple Inheritance (Python-specific)
#Definition: When a class inherits from multiple parent classes.
#Python fully supports multiple inheritance.
# Parent class 1
class Flyable:
    def fly(self):
        print("Can fly")
    
    def speed(self):
        print("Can travel at high speed")

# Parent class 2
class Swimmable:
    def swim(self):
        print("Can swim")
    
    def speed(self):
        print("Can travel at moderate speed in water")

# Child class inheriting from both parents
class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
    
    def display_abilities(self):
        print(f"{self.name} can:")
        self.fly()
        self.swim()

# Usage
duck = Duck("Donald")
duck.display_abilities()
duck.fly()
duck.swim()

# Method Resolution Order (MRO)
print(Duck.__mro__)  # Shows the order Python uses to find methods

#Multiple Inheritance with Method Resolution

class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):  # A comes first, so A's show() is used
    pass

class D(B, A):  # B comes first, so B's show() is used
    pass

c = C()
c.show()  # Output: Class A (because A is first in inheritance order)

d = D()
d.show()  # Output: Class B (because B is first in inheritance order)

# Check Method Resolution Order
print(C.__mro__)  # (C, A, B, object)
print(D.__mro__)  # (D, B, A, object)
#Hybrid Inheritance
# Definition: Combination of two or more types of inheritance (e.g., multiple + multilevel).

# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print(f"{self.name} is breathing")

# Hierarchical inheritance from Animal
class Mammal(Animal):
    def feed_milk(self):
        print(f"{self.name} is feeding milk")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")

# Multiple inheritance (combining Mammal and Bird)
class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)
    
    def display_info(self):
        print(f"{self.name} is a mammal that can fly")

# Multilevel inheritance from Bat
class VampireBat(Bat):
    def drink_blood(self):
        print(f"{self.name} drinks blood")

# Usage
bat = Bat("Fruit Bat")
bat.breathe()    # From Animal
bat.feed_milk()  # From Mammal
bat.fly()        # From Bird

vampire = VampireBat("Dracula Bat")
vampire.display_info()
vampire.drink_blood()

class Engine:
    def start_engine(self):
        print("Engine started")

class Wheels:
    def rotate_wheels(self):
        print("Wheels rotating")

class Vehicle(Engine, Wheels):
    def move(self):
        print("Vehicle moving")

class ElectricSystem:
    def charge_battery(self):
        print("Battery charging")

class ElectricCar(Vehicle, ElectricSystem):
    def __init__(self, model):
        self.model = model
    
    def display(self):
        print(f"Electric Car: {self.model}")
        self.start_engine()
        self.rotate_wheels()
        self.charge_battery()
        self.move()

# Usage
tesla = ElectricCar("Tesla Model S")
tesla.display()
#Important Python Inheritance Features
# super() Function
# Used to call parent class methods.
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent init: {name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls Parent's __init__
        self.age = age
        print(f"Child init: {age}")

child = Child("John", 10)
#Method Overriding
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):  # Overrides parent method
        print("Child method")

c = Child()
c.show()  # Child method
#Checking Inheritance
class A: pass
class B(A): pass
class C(B): pass

print(issubclass(B, A))     # True (B is subclass of A)
print(issubclass(C, A))     # True (C is subclass of A)
print(isinstance(B(), A))   # True (B instance is A type)
print(isinstance(C(), A))   # True
#Method Resolution Order (MRO)

class X: pass
class Y: pass
class Z: pass
class A(X, Y): pass
class B(Y, Z): pass
class M(B, A, Z): pass

print(M.__mro__)
# Good practice
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

# Better alternative (composition when inheritance doesn't fit)
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

## 1. Math module
import math
print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.141592653589793
print(math.factorial(5))  # 120

# 2. Random module
import random
print(random.randint(1, 10))  # Random number between 1-10
print(random.choice(['apple', 'banana', 'cherry']))  # Random choice

# 3. DateTime module
from datetime import datetime, date
print(datetime.now())        # Current date and time
print(date.today())          # Today's date

# 4. OS module (similar to Java's java.io)
import os
print(os.getcwd())           # Current working directory
print(os.listdir('.'))       # List files in current directory

# 5. Sys module (system-specific parameters)
import sys
print(sys.version)           # Python version
print(sys.platform)          # Operating system

# 6. JSON module
import json
data = {"name": "John", "age": 30}
json_string = json.dumps(data)
print(json_string)           # '{"name": "John", "age": 30}'

# 1. Public Members (Default in Python)
# Everything in Python is public by default - accessible from anywhere.

class Account:
    def __init__(self):
        self.name = "Default Name"      # Public attribute
        self.email = "default@email.com" # Public attribute
    
    def display_info(self):              # Public method
        print(f"Name: {self.name}, Email: {self.email}")

# Accessing public members from anywhere
account = Account()
account.name = "Apna College"            # Accessible outside class
account.email = "hello@apnacollege.com"  # Accessible outside class
account.display_info()                   # Accessible outside class

print(account.name)  # Apna College

# 2. Protected Members (Single Underscore _)
# Convention: Protected members should not be accessed outside the class and its subclasses. But Python doesn't enforce this - it's just a warning to other developers.

class Account:
    def __init__(self):
        self.name = "Default Name"           # Public
        self._email = "default@email.com"    # Protected (convention)
        self.__password = "default123"       # Private (name mangling)
    
    def _internal_method(self):              # Protected method
        print("This is an internal method")
    
    def get_password(self):                  # Public getter method
        return self.__password

class ChildAccount(Account):
    def access_protected(self):
        # Can access protected members (by convention)
        print(f"Accessing protected email from child: {self._email}")
        self._internal_method()
        
        # Cannot access private members directly
        # print(self.__password)  # This would cause AttributeError

# Usage
account = Account()
# Protected member - accessible but not recommended
print(account._email)  # Works but violates convention
account._internal_method()  # Works but violates convention

# Child class accessing protected members
child = ChildAccount()
child.access_protected()

# 3. Private Members (Double Underscore __)
# Name Mangling: Python internally changes the name to _ClassName__membername to prevent accidental access.

class Account:
    def __init__(self):
        self.name = "Apna College"           # Public
        self._email = "hello@apnacollege.com" # Protected
        self.__password = "abcd"             # Private
    
    def set_password(self, password):        # Public setter method
        self.__password = password
    
    def get_password(self):                  # Public getter method
        return self.__password
    
    def __private_method(self):              # Private method
        print("This is a private method")

# Usage
account = Account()

# Accessing public members
account.name = "Apna College"
print(account.name)  # Apna College

# Accessing via getter/setter
account.set_password("abcd")
print(account.get_password())  # abcd

# Attempting to access private members directly (fails)
# print(account.__password)     # AttributeError
# account.__private_method()    # AttributeError

# But private members are accessible via name mangling (not recommended)
print(account._Account__password)     # abcd (name mangled)
account._Account__private_method()    # This is a private method

#
class Student:
    def __init__(self, name, age, percentage):
        self.name = name                    # Public attribute
        self.__age = age                    # Private attribute
        self.__percentage = percentage      # Private attribute
    
    # Getter for age (read-only)
    @property
    def age(self):
        """Age can be read but not modified directly"""
        return self.__age
    
    # Getter for percentage
    @property
    def percentage(self):
        return self.__percentage
    
    # Setter for percentage (with validation)
    @percentage.setter
    def percentage(self, value):
        if 0 <= value <= 100:
            self.__percentage = value
            print(f"Percentage updated to {value}%")
        else:
            raise ValueError("Percentage must be between 0 and 100")
    
    # Deleter (optional)
    @percentage.deleter
    def percentage(self):
        print("Cannot delete percentage!")
    
    # Compute grade based on percentage
    def get_grade(self):
        if self.__percentage >= 90:
            return "A+"
        elif self.__percentage >= 80:
            return "A"
        elif self.__percentage >= 70:
            return "B"
        elif self.__percentage >= 60:
            return "C"
        else:
            return "F"

# Usage
student = Student("Alice", 20, 85)

# Accessing attributes
student.name = "Alice Smith"  # Direct access (public)
print(student.name)            # Alice Smith

# Using property getter (looks like attribute access)
print(student.age)             # 20 (read-only)
# student.age = 21             # AttributeError: can't set attribute

# Using property setter
student.percentage = 92        # Percentage updated to 92%
print(student.percentage)      # 92
print(student.get_grade())     # A+

# Validation in action
# student.percentage = 105     # ValueError: Percentage must be between 0 and 100

#Python Equivalent with Full Encapsulation
class Account:
    """Bank Account class demonstrating encapsulation"""
    
    def __init__(self, name, email, initial_password):
        # Public attribute - accessible anywhere
        self.name = name
        
        # Protected attribute - convention: accessible within class & subclasses
        self._email = email
        
        # Private attribute - name mangling: accessible only within class
        self.__password = initial_password
        
        # Private attribute for account balance
        self.__balance = 0
    
    # ========== Public Methods ==========
    def set_password(self, password):
        """Public setter for private password"""
        if len(password) >= 4:
            self.__password = password
            print("Password updated successfully")
        else:
            print("Password must be at least 4 characters")
    
    def get_password(self):
        """Public getter (usually you wouldn't expose password)"""
        return "********"  # Hide actual password
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. Balance: ${self.__balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.__balance}")
            return True
        else:
            print("Insufficient balance")
            return False
    
    def get_balance(self):
        """Public getter for balance"""
        return self.__balance
    
    def display_info(self):
        """Public method showing account info"""
        print(f"Account Holder: {self.name}")
        print(f"Email: {self._email}")
        print(f"Balance: ${self.__balance}")
        print(f"Password: {self.get_password()}")
    
    # ========== Protected Methods ==========
    def _validate_email(self):
        """Protected method for internal use"""
        return "@" in self._email and "." in self._email
    
    # ========== Private Methods ==========
    def __encrypt_data(self):
        """Private method for internal encryption"""
        return "Encrypted_" + self.__password
    
    def __log_transaction(self, transaction_type, amount):
        """Private method to log transactions"""
        print(f"[LOG] {transaction_type}: ${amount}")

# Subclass demonstrating protected access
class PremiumAccount(Account):
    def __init__(self, name, email, password, premium_id):
        super().__init__(name, email, password)
        self.premium_id = premium_id
    
    def upgrade_benefits(self):
        # Can access protected members from parent
        if self._validate_email():
            print(f"Premium benefits activated for {self.name}")
            return True
        else:
            print("Invalid email format. Cannot activate premium")
            return False
    
    # Cannot access private members directly
    # def show_password(self):
    #     print(self.__password)  # This would fail

# Usage
print("=" * 50)
print("DEMONSTRATING ENCAPSULATION")
print("=" * 50)

# Create account
account = Account("Apna College", "hello@apnacollege.com", "abcd123")

# Accessing public member
account.name = "Apna College Updated"
print(f"Public name: {account.name}")  # Direct access

# Accessing protected member (possible but not recommended)
print(f"Protected email (direct access - not recommended): {account._email}")

# Accessing private member through public methods
account.set_password("newPassword123")
print(f"Password: {account.get_password()}")

# Banking operations
account.deposit(1000)
account.withdraw(250)
account.display_info()

# Premium account
print("\n" + "=" * 50)
print("PREMIUM ACCOUNT DEMO")
print("=" * 50)
premium = PremiumAccount("VIP User", "vip@example.com", "vip123", "PR-001")
premium.upgrade_benefits()
premium.deposit(5000)

#Data Hiding Demonstration
class DataHidingDemo:
    def __init__(self):
        self.public_var = "Anyone can see me"
        self._protected_var = "I'm for internal use only (convention)"
        self.__private_var = "I'm truly hidden (name mangling)"
    
    def public_method(self):
        return "Public method called"
    
    def _protected_method(self):
        return "Protected method called"
    
    def __private_method(self):
        return "Private method called"
    
    def access_private_inside_class(self):
        """Private members are accessible inside the class"""
        print(self.__private_var)
        print(self.__private_method())

# Create object
demo = DataHidingDemo()

# Public - works fine
print(demo.public_var)          # Anyone can see me
print(demo.public_method())     # Public method called

# Protected - works but violates convention
print(demo._protected_var)      # I'm for internal use only (convention)
print(demo._protected_method()) # Protected method called

# Private - direct access fails
# print(demo.__private_var)      # AttributeError
# print(demo.__private_method()) # AttributeError

# But private members are name-mangled, not truly hidden
print(demo._DataHidingDemo__private_var)     # I'm truly hidden (name mangling)
print(demo._DataHidingDemo__private_method()) # Private method called

# Proper way: access through public methods
demo.access_private_inside_class()  

#1. Static Variables (Class Variables)
class Student:
    # Class variable (static in Java terms)
    school = "JMV"  # Shared across all instances
    
    def __init__(self, name):
        # Instance variable (unique to each object)
        self.name = name
    
    def display(self):
        print(f"{self.name} studies at {Student.school}")

# Accessing class variable through class name (recommended)
print(Student.school)  # JMV

# Creating instances
s1 = Student("Meena")
s2 = Student("Beena")

# Access class variable through instances (also works)
print(s1.school)  # JMV
print(s2.school)  # JMV

# Changing class variable affects all instances
Student.school = "New School"
print(s1.school)  # New School
print(s2.school)  # New School

# Instance variable vs class variable
s1.school = "Instance School"  # Creates instance variable, doesn't change class
print(s1.school)   # Instance School (instance variable)
print(s2.school)   # New School (class variable)
print(Student.school)  # New School (class variable)

#2. Static Methods
class MathUtils:
    # Class variable
    pi = 3.14159
    
    def __init__(self):
        # Instance method
        self.instance_var = "I belong to instance"
    
    @staticmethod
    def add(a, b):
        """Static method - no self or cls parameter"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
    @classmethod
    def get_pi(cls):
        """Class method - receives class as first parameter"""
        return cls.pi

# Calling static methods (no instance needed)
print(MathUtils.add(10, 5))        # 15
print(MathUtils.multiply(4, 3))    # 12
print(MathUtils.is_even(7))        # False

# Can also call through instance (but not recommended)
utils = MathUtils()
print(utils.add(5, 3))              # 8 (works but not preferred)

# Class method
print(MathUtils.get_pi())           # 3.14159

#
class Student:
    # Static/Class variables
    school = "JMV"  # Default value
    total_students = 0
    
    def __init__(self, name):
        # Instance variables
        self.name = name
        Student.total_students += 1
        self.roll_number = Student.total_students
    
    # Instance method (can access both instance and class variables)
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"School: {Student.school}")
        print("-" * 20)
    
    # Static method - doesn't access instance or class
    @staticmethod
    def is_valid_name(name):
        """Validation logic - doesn't need class/instance"""
        return len(name) > 0 and name.replace(" ", "").isalpha()
    
    # Class method - works with class variables
    @classmethod
    def change_school(cls, new_school):
        """Change school for all students"""
        old_school = cls.school
        cls.school = new_school
        print(f"School changed from '{old_school}' to '{new_school}'")
    
    @classmethod
    def get_total_students(cls):
        return f"Total students enrolled: {cls.total_students}"
    
    @classmethod
    def create_anonymous_student(cls):
        """Alternative constructor - creates student without name"""
        return cls("Anonymous")

# Static block equivalent (executed when class is defined)
print("Loading Student class...")
Student.school = "JMV International"  # Like static initialization

# Usage
print("=" * 50)
print("STUDENT DEMO")
print("=" * 50)

# Create students
s1 = Student("Meena")
s2 = Student("Beena")

# Access class/static variable through class name
print(f"School name: {Student.school}")

# Display individual students
s1.display_info()
s2.display_info()

# Use static method
print(f"Is 'John' a valid name? {Student.is_valid_name('John')}")
print(f"Is '' a valid name? {Student.is_valid_name('')}")

# Use class method to change school
Student.change_school("Python University")

# See updated school for existing and new students
s1.display_info()
s3 = Student("Charlie")
s3.display_info()

# Get total students
print(Student.get_total_students())

# Alternative constructor
anonymous = Student.create_anonymous_student()
anonymous.display_info()

#Static Block (Class-Level Initialization)
class DatabaseConnection:
    # Class variables
    connection_pool = []
    config = {}
    
    # Static block equivalent (executed when class is defined)
    print("Initializing DatabaseConnection class...")
    
    # Class-level initialization
    config = {
        "host": "localhost",
        "port": 3306,
        "user": "admin"
    }
    
    # Initialize connection pool
    for i in range(3):
        connection_pool.append(f"Connection_{i+1}")
    
    @classmethod
    def get_connection(cls):
        if cls.connection_pool:
            return cls.connection_pool.pop()
        return "No connections available"
    
    @classmethod
    def release_connection(cls, conn):
        cls.connection_pool.append(conn)

# Class initialization happens when module loads
print(f"Config: {DatabaseConnection.config}")
print(f"Initial pool: {DatabaseConnection.connection_pool}")

# Using the class
conn = DatabaseConnection.get_connection()
print(f"Got: {conn}")
print(f"Remaining: {DatabaseConnection.connection_pool}")

#Static Nested Class
class Outer:
    outer_var = "I'm outer"
    
    def __init__(self, value):
        self.value = value
    
    class StaticNestedClass:
        """Like static nested class in Java"""
        @staticmethod
        def display():
            print("Inside static nested class")
        
        @staticmethod
        def calculate(x, y):
            return x + y
    
    class InnerClass:
        """Non-static inner class - has reference to outer"""
        def __init__(self, outer_instance):
            self.outer = outer_instance
        
        def display_outer(self):
            print(f"Accessing outer value: {self.outer.value}")

# Access static nested class directly (no outer instance needed)
Outer.StaticNestedClass.display()
result = Outer.StaticNestedClass.calculate(10, 5)
print(f"Calculation: {result}")

# Inner class needs outer instance
outer_obj = Outer("Hello")
inner_obj = Outer.InnerClass(outer_obj)
inner_obj.display_outer()