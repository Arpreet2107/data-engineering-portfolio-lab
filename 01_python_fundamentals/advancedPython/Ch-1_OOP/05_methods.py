class MyClass:
    my_var = 100
    # Dunder method or magic method 
    # Dunder methods are special methods in Python that have double underscores at the beginning and end of their names. They are also known as magic methods because they have special behavior and are called automatically by Python in certain situations. For example, the __init__ method is a dunder method that is called when an object is created from a class, and it is used to initialize the object's attributes. The __str__ method is another dunder method that is called when the str() function is used on an object, and it is used to return a string representation of the object. Dunder methods allow us to define how our objects behave in different situations and can be used to implement operator overloading, custom string representations, and more.
    def __init__(self):
        print("This is the constructor method")

    # Dunder method for str 
    # The __str__ method is a dunder method in Python that is used to define the string representation of an object. It is called when the str() function is used on an object, or when the object is printed. The __str__ method should return a string that represents the object in a human-readable format. For example, if we have a class called MyClass and we want to define how it should be represented as a string, we can implement the __str__ method like this:
    def __str__(self):
        return "This is the string representation of the object"
    # Dunder method for repr
    # The __repr__ method is a dunder method in Python that is used to define the official string representation of an object. It is called when the repr() function is used on an object, or when the object is printed in the interactive shell. The __repr__ method should return a string that represents the object in a way that can be used to recreate the object. For example, if we have a class called MyClass and we want to define how it should be represented as a string for debugging purposes, we can implement the __repr__ method like this:
    def __repr__(self):
        return "MyClass()"
    
    # For example, if we have a class called MyClass and we want to define a class method that changes the value of a class variable, we can implement it like this:
    @classmethod# Class method is a method that is bound to the class and not the instance of the class. It can be called on the class itself or on an instance of the class. The first parameter of a class method is always the class itself, which is conventionally named cls. Class methods are
    # defined using the @classmethod decorator and can be used to access and modify class variables, as well as to create alternative constructors for the class.
    # In this example, the change_value class method takes a new value as an argument and assigns it to the class variable my_var using the cls parameter. This allows us to change the value of my_var for all instances of the class, since it is a class variable.
    def _change_value(cls,new_value):
        cls.my_var = new_value
    # Static method is a method that is bound to the class and not the instance of the class. It does not take any special first parameter like self or cls. Static methods are defined using the @staticmethod decorator and can be called on the class itself or on an instance of the class. Static methods are used to define utility functions that are related to the class but do not need access to any instance or class variables.
    # For example, if we have a class called MyClass and we want to define a static method that prints a message, we can implement it like this:    
    class MyClass:
        @staticmethod
        def dummy():
            print("This is a dummy method")       
    # In this example, the dummy static method simply prints a message and does not require access to any instance or class variables. We can call this method using the class name or an instance of the class, like this:
    MyClass.dummy() # This will print "This is a dummy method"
    obj = MyClass()
    obj.dummy() # This will also print "This is a dummy method"
    # Static methods are often used for utility functions that are related to the class but do not need to access any instance or class variables. They can be called without creating an instance of the class, which can be useful in certain situations. 
    # For example, if we have a class called MathUtils and we want to define a static method that calculates the square of a number, we can implement it like this:
    class MathUtils:
        @staticmethod
        def square(x):
            return x * x
    # In this example, the square static method takes a number as an argument and returns its square. We can call this method using the class name without creating an instance of the class, like this:
    result = MathUtils.square(5) # This will return 25    

    @staticmethod
    def dummy():
        print("This is a dummy method")

obj = MyClass()
print(obj.my_var) # 100
obj._change_value(200)
print(obj.my_var) # 200
obj2 = MyClass()
print(obj2.my_var) # 200
obj3 = MyClass()
print(obj3.dummy())
obj4 = MyClass()
print(obj4)