class Myclass:
    #class variables
    var1 = "Arpreet"
    var2 = "Mahala"
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1 = dyn1
        self.dyn2 = dyn2
        self.dyn3 = dyn3
    #class methods
    def func1(self):
        print(f"Hello World, {self.dyn1}")
    def func2(self):
        print(f"Welcome to OOPs! {self.dyn2}")
    def func3(self):
        print(f"Have a nice day! {self.dyn3}")
#Creating an object of the class
object1 = Myclass("Arpreet","Mahala","Have a nice day") 
object2 = Myclass("Python","Programming","Is fun")
object3 = Myclass("Welcome","To","OOPs")
#Accessing class variables using the object
print(object1.var1)
print(object2.var2)

#Another way to access class variables using the class name
Myclass.var1 = "Python"
print(Myclass.var1)
#Accessing class methods using the object
object1.func1()
object2.func2()
object3.func3()

#Modifying class variables using the object
object_new = Myclass("New","Object","For testing")
object_new.var2 = "Changed value"
print(object_new.var2) #Output: Changed value